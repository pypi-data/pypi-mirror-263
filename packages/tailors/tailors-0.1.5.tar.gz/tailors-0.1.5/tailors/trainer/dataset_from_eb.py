# -*- coding: utf-8 -*-
import itertools
import json
import logging
import operator
import os
import random
from collections import defaultdict

import hao
import requests
from hao.namespaces import attr, from_args
from hao.spinner import Spinner
from hao.stopwatch import Stopwatch

LOGGER = hao.logs.get_logger('trainer-dataset-from-eb')
hao.logs.update_logger_levels({
    "__main__": logging.INFO,
})


@from_args
class Conf(object):
    task: str = attr(str, required=True)
    token: str = attr(str, help='task token or user token', env='token', required=True, secret=True)
    format: str = attr(str, choices=['neat', 'raw'], default='raw')
    selection: str = attr(str, choices=('annotated', 'reviewed', 'all'), default='annotated')
    cases: bool = attr(bool, default=True)
    cases_factor: int = attr(int, default=2, help='n duplicates of the cases')
    cases_starts: int = attr(int, help='No. from which are all cases')
    ignore_user: str = attr(str, help='ignore items annotated by user')
    seed: int = attr(int, required=True, default=1000)
    type: str = attr(str, choices=('SLC', 'MLC', 'NER', 'RE', 'T2T'), help='task types')
    endpoint: str = attr(str, default=hao.config.get('eb.endpoint', 'http://bjb.bl-ai.com'))


def process():
    LOGGER.info('process')
    sw = Stopwatch()
    conf = Conf()
    LOGGER.info(conf)

    labels = get_labels(conf)
    items = get_items(conf)
    items_cases = get_items(conf, is_cases=True) if conf.cases and not conf.task.endswith('cases') else []
    items_train, items_val = group_split(conf, items, items_cases)

    dataset = {'train': convert(items_train), 'val': convert(items_val)}
    log_summary(conf, dataset, labels)
    msgs = [save_to_file(conf.task, split, items) for split, items in dataset.items()]
    LOGGER.info(f'done, took: {sw.took()}')
    for msg in msgs:
        LOGGER.info(msg)


def get_labels(conf: Conf):
    labels_path = hao.paths.get(f"data/raw/{conf.task}-labels.json")
    if os.path.exists(labels_path):
        return json.loads(open(labels_path).read())

    headers = {'API-Token': conf.token}
    url = f"{conf.endpoint}/api/task/{conf.task}/tags"
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    hao.paths.make_parent_dirs(labels_path)
    LOGGER.info(f"[labels.json] saving to: {labels_path}")

    data = res.json().get('data')
    labels = {
        label: {tag.get('name'): tag.get('description') for tag in tags.get('tags')}
        for label, tags in data.items()
    }

    with open(labels_path, 'w') as f:
        f.write(hao.jsons.prettify(labels))
    return labels


def get_items(conf: Conf, *, is_cases: bool = False):
    def qualified(item):
        if item.get('enabled') is False:
            return False
        if item.get('editor_timestamp') is None:
            return False
        if conf.ignore_user is not None and item.get('reviewer_timestamp') is None and item.get('editor') == conf.ignore_user:
            return False
        return True

    task = f"{conf.task}-cases" if is_cases else conf.task

    with Spinner(f"[{task}] fetching from eb") as spinner:
        dataset_raw_path = hao.paths.get(f"data/raw/{task}.jsonl")

        if os.path.exists(dataset_raw_path):
            items = open(dataset_raw_path).readlines()
            items = [json.loads(item) for item in items]
            spinner.msg = f"[{task}] loaded {len(items)} items from local"

        else:
            headers = {'API-Token': conf.token}
            url = f"{conf.endpoint}/api/task/export?name={task}&format={conf.format}&selection={conf.selection}&zip=false"
            res = requests.get(url, headers=headers)
            res.raise_for_status()

            contents = res.text.splitlines()
            if len(contents) == 1 and json.loads(contents[0]).get('message') is not None:
                LOGGER.error(f"[{task}] {res.text}")
                return []

            hao.paths.make_parent_dirs(dataset_raw_path)
            LOGGER.info(f"[raw.jsonl] saving to: {dataset_raw_path}")

            with open(dataset_raw_path, 'w') as f:
                f.write(res.text)
            items = res.text.splitlines()
            items = [json.loads(item) for item in items]
            spinner.msg = f"[{task}] loaded {len(items)} items from eb"

    return list(filter(qualified, items))


def group_split(conf: Conf, items_general: list, items_cases: list):
    items_train = [item for item in items_general if item.get('splits', {}).get(conf.seed) == 'train']
    items_val = [item for item in items_general if item.get('splits', {}).get(conf.seed) == 'val']
    items_general = [item for item in items_general if item.get('splits', {}).get(conf.seed) not in ('train', 'val')]

    if conf.cases_starts:
        _items_cases = items_general[conf.cases_starts:]
        items_cases.extend(_items_cases)
        items_general = items_general[:conf.cases_starts]

    if conf.type in ('T2T', 'NER', 'RE', None):
        groups = {conf.type: items_general}

    else:
        groups = defaultdict(list)

        for item in items_general:
            annotation = item.get('annotation', {})
            annotations = annotation.get(conf.type)
            if annotations is None:
                continue

            if conf.type == 'SLC':
                label = annotations
            elif conf.type == 'MLC':
                random.seed(conf.seed)
                label = random.choice(annotation)
            else:
                LOGGER.error(f"Unsupported type: {conf.type}")
                continue

            groups[label].append(item)

    items_train, items_val = [], []
    for items in groups.values():
        random.seed(conf.seed)
        random.shuffle(items)
        i = len(items) * 8 // 10
        items_train.extend(items[:i])
        items_val.extend(items[i:])
    items_train.extend(items_cases * conf.cases_factor)
    return items_train, items_val


def convert(items: list):
    def transform(e):
        annotation = e.get('annotation')
        if annotation is None or len(annotation) == 0:
            return

        entities, relations = get_entities_and_relations(annotation)
        label, labels = get_classifications(annotation)
        data = {
            'uid': e.get('uid'),
            'es_id': e.get('es_id'),
            'caption': e.get('caption'),
            'text': e.get('text'),
            'html': e.get('html'),
            'label': label,
            'labels': labels,
            'entities': entities,
            'relations': relations,
            'splits': e.get('splits')
        }
        return {k: v for k, v in data.items() if v is not None}
    return list(filter(None, [transform(item) for item in items]))


def get_entities_and_relations(annotation: dict) -> tuple[list, list]:
    annotations_ner, annotations_re = annotation.get("NER"), annotation.get("RE")
    if annotations_ner is None:
        return None, None
    if len(annotations_ner) == 0:
        if annotations_re is None:
            return [], None
        else:
            return [], []

    idx = itertools.count(0)
    annotations_ner = [list(sorted(tags, key=operator.itemgetter('span_start'))) for tags in annotations_ner]
    entities = [[transform_tag(tag, next(idx)) for tag in tags] for tags in annotations_ner]
    entity_id_to_idx = [
        {str(tag.get('id')): {'j': j, 'idx': tag.get('idx')} for j, tag in enumerate(tags)}
        for tags in entities
    ]
    relations = [transform_rel(rel, entity_id_to_idx) for rel in annotations_re] if annotations_re else []
    return entities, relations


def transform_tag(tag, idx):
    return {
        'id': str(tag.get('id')),
        'tag': tag.get('name'),
        'start': tag.get('span_start'),
        'end': tag.get('span_end'),
        'idx': idx,
    }


def transform_rel(rel, entity_id_to_idx):
    s = rel.get('s')
    o = rel.get('o')
    p = rel.get('p')
    s = {'i': s.get('i'), **entity_id_to_idx[s.get('i')].get(str(s.get('id')))}
    o = {'i': o.get('i'), **entity_id_to_idx[o.get('i')].get(str(o.get('id')))}
    p = p.get('name')
    return {'s': s, 'o': o, 'p': p}


def get_classifications(annotation: dict):
    return annotation.get('SLC'), annotation.get('MLC')


def save_to_file(task: str, split: str, items: list[dict]):
    filepath = hao.paths.get(f"data/dataset/{task}/{split}.jsonl")
    hao.paths.make_parent_dirs(filepath)
    with open(filepath, "w") as f:
        for item in items:
            f.write(f"{hao.jsons.dumps(item)}\n")
    return f"saved to {filepath}, size: {len(items)}"


def log_summary(conf: Conf, dataset: dict, mappings: dict):
    if conf.type == 'T2T':
        return
    counters_ner = defaultdict(lambda: defaultdict(int))
    counters_re = defaultdict(lambda: defaultdict(int))
    counters_slc = defaultdict(lambda: defaultdict(int))
    counters_mlc = defaultdict(lambda: defaultdict(int))
    for split, items in dataset.items():
        for item in items:
            entities, relations, label, labels = item.get('entities'), item.get('relations'), item.get('label'), item.get('labels')
            if entities:
                for entries in entities:
                    for entry in entries:
                        counters_ner[entry.get('tag')][split] += 1
            if relations:
                for relation in relations:
                    counters_re[relation.get('p')][split] += 1
            if label:
                counters_slc[label][split] += 1
            if labels:
                for label in labels:
                    counters_mlc[label][split] += 1

    _print_counter('NER', counters_ner, mappings.get('NER'))
    _print_counter('RE', counters_re, mappings.get('RE'))
    _print_counter('SLC', counters_slc, mappings.get('SLC'))
    _print_counter('MLC', counters_mlc, mappings.get('MLC'))


def _print_counter(name, counters: dict, labels: dict):
    if len(counters) == 0:
        return
    lines = [f" {name} ".center(35, '-')]
    size = max(10, max([len(label) for label in labels]) + 1)
    lines.append(f"\t{' ': <{size}} {'train': <10} {'val': <10} {'ratio': <10} (description)")
    for label, description in labels.items():
        counter = counters.get(label)
        if counter is None:
            counts = f"{'-': <10} {'-': <10}"
            ratio = '-'
        else:
            count_train, count_val = counter.get('train', 0), counter.get('val', 0)
            counts = f"{count_train: <10} {count_val: <10}"
            ratio = '0.0' if count_val == 0 else f"{count_train / count_val:0.1f}"
        lines.append(f"\t{label: <{size}} {counts} {ratio: <10} ({description})")
    LOGGER.info('\n'.join(lines))


if __name__ == '__main__':
    try:
        process()
    except KeyboardInterrupt:
        print('[ctrl-c] stopped')
    except Exception as e:
        LOGGER.exception(e)
