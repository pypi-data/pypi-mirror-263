import cv2
import numpy as np
from shapely.geometry import Polygon


class IoUEvaluator:

    def __init__(self, is_polygon=False, iou_constraint=0.5, area_precision_constraint=0.5):
        self.is_polygon = is_polygon
        self.iou_constraint = iou_constraint
        self.area_precision_constraint = area_precision_constraint

    @staticmethod
    def iou_rotate(box_a, box_b, method='union'):
        rect_a = cv2.minAreaRect(box_a)
        rect_b = cv2.minAreaRect(box_b)
        r1 = cv2.rotatedRectangleIntersection(rect_a, rect_b)
        if r1[0] == 0:
            return 0
        else:
            inter_area = cv2.contourArea(r1[1])
            area_a = cv2.contourArea(box_a)
            area_b = cv2.contourArea(box_b)
            union_area = area_a + area_b - inter_area
            if union_area == 0 or inter_area == 0:
                return 0
            if method == 'union':
                iou = inter_area / union_area
            elif method == 'intersection':
                iou = inter_area / min(area_a, area_b)
            else:
                raise NotImplementedError
            return iou

    @staticmethod
    def get_union(poly_a, poly_b):
        return Polygon(poly_a).union(Polygon(poly_b)).area

    @staticmethod
    def get_intersection(poly_a, poly_b):
        return Polygon(poly_a).intersection(Polygon(poly_b)).area

    def get_intersection_over_union(self, poly_a, poly_b):
        return self.get_intersection(poly_a, poly_b) / self.get_union(poly_a, poly_b)

    def evaluate_image(self, trues, preds):
        metrics_sample = {}
        total_matched, total_trues, total_preds, n_matched = 0, 0, 0, 0
        precision, recall, f1 = 0, 0, 0

        iou_mat = np.empty([1, 1])

        poly_trues, poly_preds = [], []
        points_trues, points_preds = [], []

        # Array of Ground Truth Polygons' keys marked as don't Care
        # Array of Detected Polygons' matched with a don't Care GT
        poly_keys_ignore_trues, ploy_keys_ignore_preds = [], []

        pairs = []
        matched_nums = []

        eval_logs = []

        for n in range(len(trues)):
            points = trues[n]['points']
            ignore = trues[n]['ignore']

            if not Polygon(points).is_valid or not Polygon(points).is_simple:
                continue

            poly_trues.append(points)
            points_trues.append(points)
            if ignore:
                poly_keys_ignore_trues.append(len(poly_trues) - 1)

        if len(poly_keys_ignore_trues) > 0:
            eval_logs.append(f"GT polygons: {len(poly_trues)} (ignores: {len(poly_keys_ignore_trues)})")
        else:
            eval_logs.append(f"GT polygons: {len(poly_trues)}")

        for n in range(len(preds)):
            points = preds[n]['points']
            if not Polygon(points).is_valid or not Polygon(points).is_simple:
                continue

            poly_preds.append(points)
            points_preds.append(points)
            if len(poly_keys_ignore_trues) > 0:
                for poly_key_ignore in poly_keys_ignore_trues:
                    poly_ignore = poly_trues[poly_key_ignore]
                    intersected_area = self.get_intersection(poly_ignore, points)
                    dims = Polygon(points).area
                    precision = 0 if dims == 0 else intersected_area / dims
                    if (precision > self.area_precision_constraint):
                        ploy_keys_ignore_preds.append(len(poly_preds) - 1)
                        break

        if len(ploy_keys_ignore_preds) > 0:
            eval_logs.append(f"DET polygons: {len(poly_preds)} (ignores: {len(ploy_keys_ignore_preds)})")
        else:
            eval_logs.append(f"DET polygons: {len(poly_preds)}")

        if len(poly_trues) > 0 and len(poly_preds) > 0:
            # Calculate IoU and precision matrixs
            iou_mat = np.empty([len(poly_trues), len(poly_preds)])
            poly_mat_trues = np.zeros(len(poly_trues), np.int8)
            poly_mat_preds = np.zeros(len(poly_preds), np.int8)

            if self.is_polygon:
                for i_trues in range(len(poly_trues)):
                    for i_preds in range(len(poly_preds)):
                        poly_true = poly_trues[i_trues]
                        poly_pred = poly_preds[i_preds]
                        iou_mat[i_trues, i_preds] = self.get_intersection_over_union(poly_pred, poly_true)
            else:
                for i_trues in range(len(poly_trues)):
                    for i_preds in range(len(poly_preds)):
                        poly_true = np.float32(poly_trues[i_trues])
                        poly_pred = np.float32(poly_preds[i_preds])
                        iou_mat[i_trues, i_preds] = self.iou_rotate(poly_pred, poly_true)

            for i_trues in range(len(poly_trues)):
                for i_preds in range(len(poly_preds)):
                    if (
                        poly_mat_trues[i_trues] == 0
                        and poly_mat_preds[i_preds] == 0
                        and i_trues not in poly_keys_ignore_trues
                        and i_preds not in ploy_keys_ignore_preds
                        and iou_mat[i_trues, i_preds] > self.iou_constraint
                    ):
                        poly_mat_trues[i_trues] = 1
                        poly_mat_preds[i_preds] = 1
                        n_matched += 1
                        pairs.append({'gt': i_trues, 'det': i_preds})
                        matched_nums.append(i_preds)
                        eval_logs.append(f"Match GT #{i_trues} with Det #{i_preds}")

        n_trues = (len(poly_trues) - len(poly_keys_ignore_trues))
        n_preds = (len(poly_preds) - len(ploy_keys_ignore_preds))
        if n_trues == 0:
            recall = 1.0
            precision = .0 if n_preds > 0 else 1.0
        else:
            recall = 1.0 * n_matched / n_trues
            precision = .0 if n_preds == 0 else 1.0 * n_matched / n_preds

        f1 = 0 if (precision + recall) == 0 else 2.0 * precision * recall / (precision + recall)

        total_matched += n_matched
        total_trues += n_trues
        total_preds += n_preds

        metrics_sample = {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'pairs': pairs,
            'iou_mat': [] if len(poly_preds) > 100 else iou_mat.tolist(),
            'points_trues': points_trues,
            'points_preds': points_preds,
            'total_trues': total_trues,
            'total_preds': total_preds,
            'ignored_trues': poly_keys_ignore_trues,
            'ignored_preds': ploy_keys_ignore_preds,
            'total_matched': total_matched,
            'logs': '\n'.join(eval_logs)
        }

        return metrics_sample
