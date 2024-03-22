from collections.abc import Iterable


def get(obj, names: str | list[str]):
    if isinstance(names, str):
        names = [names]

    is_dict = isinstance(obj, dict)
    is_namedtuple = isinstance(obj, tuple) and hasattr(obj, '_fields')
    assert is_dict or is_namedtuple, f"Expecting 'dict' or 'namedtuple', but found: {type(obj)}"

    for name in names:
        if is_dict:
            if (val := obj.get(name)) is not None:
                return val
        elif is_namedtuple:
            if (val := getattr(obj, name, None)) is not None:
                return val

    return None


def guess_measure_name(metrics: Iterable) -> str | None:
    measures = ('f1', 'acc', 'accuracy', 'precision')
    neg_measures = ('loss',)
    for measure in measures:
        if measure in metrics:
            return measure
    metrics = sorted(list(metrics))
    for metric in metrics:
        for measure in measures:
            if measure in metric:
                return metric
    for metric in metrics:
        if any(non_measure in metric for non_measure in neg_measures):
            continue
        return metric
    return None
