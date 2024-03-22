import editdistance


def calculate(predictions: list[str], trues: list[str]):
    num = len(predictions)
    if num == 0:
        return {'num': 0, 'correct': 0, 'cer': 0, 'ned': 0}

    correct, cer = 0, 0
    for pred, true in zip(predictions, trues):
        if pred == true:
            correct += 1
        cer += calc_cer(pred, true)
    return {
        'num': num,
        'correct': correct,
        'cer': cer,
    }


def accumulate(metrics):
    n = len(metrics)
    num = sum(metric.get('num') for metric in metrics)
    correct = sum(metric.get('correct') for metric in metrics)
    acc = correct / num
    cer = sum(metric.get('cer') for metric in metrics) / n

    return {'acc': acc, 'cer': cer}


def calc_cer(pred: str, true: str):
    pred_len = len(pred)
    if pred_len == 0:
        return 0
    return editdistance.eval(true, pred) / pred_len
