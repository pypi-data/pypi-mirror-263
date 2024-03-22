"""
Ref:
 - 2020-Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics
 - 2020-Identifying Mislabeled Data using the Area Under the Margin Ranking
"""
import glob
from collections import defaultdict, namedtuple
from enum import Enum
from functools import partial

import hao
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from hao.namespaces import attr, from_args
from scipy.special import softmax

LOGGER = hao.logs.get_logger(__name__)


MetricAttrs = namedtuple('MetricAttrs', ['name', 'ascending'])
SelectionParams = namedtuple('SelectionParams', ['metric', 'lowest'])


class Metric(Enum):
    THRESHOLD_CLOSENESS = MetricAttrs('threshold_closeness', False)
    CONFIDENCE = MetricAttrs('confidence', True)
    VARIABILITY = MetricAttrs('variability', False)
    CORRECTNESS = MetricAttrs('correctness', True)
    FORGETFULNESS = MetricAttrs('forgetfulness', False)

    @classmethod
    def names(cls):
        return [m.name.lower() for m in cls]


class Selection(Enum):
    HARD = SelectionParams(Metric.CONFIDENCE, False)
    EASY = SelectionParams(Metric.CONFIDENCE, True)
    AMBIGUOUS = SelectionParams(Metric.VARIABILITY, False)

    @classmethod
    def names(cls):
        return [m.name.lower() for m in cls]

@from_args
class Conf:
    path: str = attr(str, required=True, help='folder that contains dynamics-*.pkl')
    label_id: int = attr(int, help='optional label-id for multilabel classification')
    threshold: float = attr(float, default=0.0, help='threshold for true prediction')
    select: str = attr(str, choices=Selection.names())
    select_ratio: float = attr(float, default=0.3)
    plot_path: str = attr(str)


def process(conf: Conf | None = None):
    conf = conf or Conf()
    LOGGER.info(conf)
    dynamics = load_dynamics(conf.path)
    metrics = calculate_metrics(dynamics, conf.label_id, conf.threshold)
    if conf.select:
        selection = Selection[conf.select.upper()]
        guids = select(metrics, selection.value.metric, selection.value.lowest, conf.select_ratio)
        for guid in guids:
            print(guid)
    if conf.plot_path:
        plot(metrics, conf.plot_path)


def load_dynamics(path: str, epochs: list[int] | None = None):
    files = sorted(glob.glob(f"{path}/dynamics-*.pkl"))
    if epochs is not None:
        files = [file for file in files if int(file[-6:-4]) in epochs]
    dfs = [pd.read_pickle(file).drop_duplicates('guid') for file in files]
    df = pd.concat([d.set_index('epoch') for d in dfs], axis = 0).reset_index()
    groups = df.groupby(['guid'])
    dynamics = defaultdict(dict)
    for guid in groups.groups:
        group = groups.get_group(guid)
        dynamics[guid]['logits'] = group.logits.values
        dynamics[guid]['gold'] = group.gold.values
    dynamics.default_factory = None
    return dynamics


def calculate_metrics(dynamics: dict[str, dict[str, np.array]], label_id: int | None = None, threshold: float = .0):
    metrics = []
    for guid, entry in dynamics.items():
        logits, gold = entry.get('logits'), entry.get('gold')
        true_prob_trends, correctness_trends = get_trends(logits, gold, label_id, threshold)

        correctness = calc_correctness(correctness_trends)
        confidence = calc_confidence(true_prob_trends)
        variability = calc_variability(true_prob_trends)
        forgetfulness = calc_forgetfulness(correctness_trends)
        threshold_closeness = calc_threshold_closeness(confidence)
        metrics.append([guid, threshold_closeness, confidence, variability, correctness, forgetfulness])
    columns=['guid'] + Metric.names()
    return pd.DataFrame(metrics, columns=columns)


def get_trends(logits, gold, label_id: int | None = None, threshold: float = .0):
    is_multilabel = isinstance(gold[0], list)
    logits, gold = np.stack(logits, axis=0), np.stack(gold, axis=0)
    if is_multilabel:
        if label_id is not None:
            label_logits = logits[:, label_id]
            true_prob_trends = label_logits
            predictions = (label_logits > threshold).astype(int)
            truths = gold[:, label_id]
            correctness_trends = predictions == truths
        else:
            true_prob_trends = np.array([np.sum(_logits[np.nonzero(_gold)]) for _logits, _gold in zip(logits, gold)])
            correctness_trends = np.all((logits > threshold).astype(int) == gold, axis=1)
    else:
        true_prob_trends = softmax(logits)[np.arange(len(logits)), np.argmax(gold, axis=1)]
        predictions = np.argmax(logits, axis=1)
        truths = gold
        correctness_trends = predictions == truths

    return true_prob_trends, correctness_trends


def select(metrics: pd.DataFrame, metric: Metric, lowest: bool = False, ratio: float = 0.3):
    ascending = not metric.value.ascending if lowest else metric.value.ascending
    sorted_metrics = metrics.sort_values(by=metric.value.name, ascending=ascending)
    selection = sorted_metrics.head(n=int(ratio * len(sorted_metrics)))
    return list(selection['guid'])


select_hard = partial(select, metric=Selection.HARD.value.metric, lowest=Selection.HARD.value.lowest)
select_easy = partial(select, metric=Selection.EASY.value.metric, lowest=Selection.EASY.value.lowest)
select_ambiguous = partial(select, metric=Selection.AMBIGUOUS.value.metric, lowest=Selection.AMBIGUOUS.value.lowest)


def plot(dynamics, img_path: str, max_instances_to_plot = 55000):
    """plot confidence-variability and save it into png"""
    sns.set(style='whitegrid', font_scale=1.6, context='paper')
    # Subsample data to plot, so the plot is not too busy.
    dynamics = dynamics.sample(n=max_instances_to_plot if dynamics.shape[0] > max_instances_to_plot else len(dynamics))
    data = dynamics.assign(corr_frac=lambda d: d.correctness / d.correctness.max())
    data['correct.'] = [float(f'{x:.1f}') for x in data['corr_frac']]

    metric_variability = 'variability'
    metric_confidence = 'confidence'
    metric_correct_frac = 'correct.'

    num_correct_frac = len(data[metric_correct_frac].unique().tolist())
    style = metric_correct_frac if num_correct_frac < 8 else None

    fig = plt.figure(figsize=(14, 10), )
    gs = fig.add_gridspec(3, 2, width_ratios=[5, 1])
    ax_confidence_variability = fig.add_subplot(gs[:, 0])

    pal = sns.diverging_palette(260, 15, n=num_correct_frac, sep=10, center='dark')
    plot = sns.scatterplot(
        x=metric_variability, y=metric_confidence, ax=ax_confidence_variability,
        data=data, hue=metric_correct_frac, palette=pal, style=style, s=30
    )

    # annotate Regions
    def fn_bbox(c):
        return dict(boxstyle='round,pad=0.3', ec=c, lw=2, fc='white')

    def fn_annotate(text, xyc, bbc):
        return ax_confidence_variability.annotate(
            text,
            xy=xyc,
            xycoords='axes fraction',
            fontsize=15,
            color='black',
            va='center',
            ha='center',
            rotation=350,
            bbox=fn_bbox(bbc)
        )

    fn_annotate('ambiguous', xyc=(0.9, 0.5), bbc='black')
    fn_annotate('easy-to-learn', xyc=(0.27, 0.85), bbc='r')
    fn_annotate('hard-to-learn', xyc=(0.35, 0.25), bbc='b')

    plot.set_xlabel('variability')
    plot.set_ylabel('confidence')
    plot.set_title('dynamic data-map', fontsize=17)

    # plot the histograms
    ax_hist_confidence = fig.add_subplot(gs[0, 1])
    hist_confidence = data.hist(column=['confidence'], ax=ax_hist_confidence, color='RebeccaPurple')
    hist_confidence[0].set_title('')
    hist_confidence[0].set_xlabel('confidence')
    hist_confidence[0].set_ylabel('density')

    ax_hist_variability = fig.add_subplot(gs[1, 1])
    hist_variability = data.hist(column=['variability'], ax=ax_hist_variability, color='Teal')
    hist_variability[0].set_title('')
    hist_variability[0].set_xlabel('variability')
    hist_variability[0].set_ylabel('density')

    ax_hist_correctness = fig.add_subplot(gs[2, 1])
    hist_correctness = data.hist(column=['correct.'], ax=ax_hist_correctness, color='MediumAquaMarine')
    hist_correctness[0].set_title('')
    hist_correctness[0].set_xlabel('correctness')
    hist_correctness[0].set_ylabel('density')

    fig.tight_layout()

    if img_path:
        fig.savefig(img_path, dpi=300)
        LOGGER.info(f'save figure into {img_path}')


def calc_forgetfulness(correctness_trend: list[float]) -> int:
    """
    Given a epoch-wise trend of train predictions, compute frequency with which
    an example is forgotten, i.e. predicted incorrectly _after_ being predicted correctly.
    Based on: https://arxiv.org/abs/1812.05159
    """
    if not any(correctness_trend):  # Example is never predicted correctly, or learnt!
        return 1000
    learnt = False  # Predicted correctly in the current epoch.
    times_forgotten = 0
    for is_correct in correctness_trend:
        if (not learnt and not is_correct) or (learnt and is_correct):  # nothing changed
            continue
        elif learnt and not is_correct:  # Forgot after learning at some point!
            learnt = False
            times_forgotten += 1
        elif not learnt and is_correct:  # Learnt!
            learnt = True
    return times_forgotten


def calc_correctness(correctness_trends):
    return sum(correctness_trends)


def calc_confidence(true_prob_trends):
    return np.mean(true_prob_trends)


def calc_variability(true_prob_trends):
    return np.std(true_prob_trends)


def calc_threshold_closeness(confidence):
    return confidence * (1 - confidence)
