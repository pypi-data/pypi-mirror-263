
import numpy as np

from tailors.utils.evaluators import IoUEvaluator


def calculate(polys, scores, targets, box_thresh: float = 0.6, is_polygon: bool = False):
    evaluator = IoUEvaluator(is_polygon=is_polygon)
    results = []
    poly_trues = targets.boxes
    ignores = targets.ignores
    poly_preds = np.array(polys)
    scores_preds = np.array(scores)
    for poly_true, poly_pred, scores_pred, ignore_tags in zip(poly_trues, poly_preds, scores_preds, ignores):
        trues = [dict(points=np.int64(poly_true[i]), ignore=ignore_tags[i]) for i in range(len(poly_true))]
        if is_polygon:
            preds = [dict(points=poly_pred[i]) for i in range(len(poly_pred))]
        else:
            preds = []
            for i in range(poly_pred.shape[0]):
                if scores_pred[i] >= box_thresh:
                    preds.append(dict(points=poly_pred[i, :, :].astype(int)))
        results.append(evaluator.evaluate_image(trues, preds))
    return results


def accumulate(metrics):
    metrics = [image_metrics for batch_metrics in metrics for image_metrics in batch_metrics]
    total_matched = sum(metric.get('total_matched') for metric in metrics)
    total_trues = sum(metric.get('total_trues') for metric in metrics)
    total_preds = sum(metric.get('total_preds') for metric in metrics)

    recall = total_matched / (total_trues + 1e-8)
    precission = total_matched / (total_preds + 1e-8)
    f1 = 2 * recall * precission / (recall + precission + 1e-8)

    return {'precision': precission, 'recall': recall, 'f1': f1}
