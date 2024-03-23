#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/21
# @Author  : yanxiaodong
# @File    : eval_metric.py
"""
from typing import List, Dict
from collections import defaultdict

from .function import MeanAveragePrecision, Accuracy, PrecisionRecallF1score, ConfusionMatrix, MeanIoU


class EvalMetric(object):
    """
    Eval metric.
    """

    def __init__(self, category: str, labels: List, images: List[Dict]):
        self.labels = labels
        self.images = images

        self.image_dict = {item["image_id"]: item for item in self.images}
        self.img_id_str2int = {key: idx + 1 for idx, key in enumerate(self.image_dict)}

        if category == "Image/ObjectDetection":
            self.metric_name = [MeanAveragePrecision(categories=self.labels,
                                                     num_classes=len(self.labels),
                                                     classwise=True)]
            self.format_function = self._format_to_object_detection
        elif category == "Image/Classification":
            self.metric_name = [Accuracy(num_classes=len(self.labels)),
                                PrecisionRecallF1score(num_classes=len(self.labels)),
                                ConfusionMatrix(num_classes=len(self.labels))]
            self.format_function = None
        elif category == "Image/SemanticSegmentation":
            self.metric_name = [MeanIoU(num_classes=len(self.labels))]
            self.format_function = None
        else:
            raise ValueError(f"Unknown category: {category}")

    def update(self, predictions: List[Dict], references: List[Dict]):
        """
        Update metric.
        """
        predictions, references = self.format_function(predictions, references)

        for metric in self.metric_name:
            metric.update(predictions={"bbox": predictions}, references={"bbox": references})

    def _format_to_object_detection(self, predictions: List[Dict], references: List[Dict]):
        """
        Format to object detection metric.
        """
        new_predictions = []
        for item in predictions:
            im_id = item["image_id"]
            im_id_int = self.img_id_str2int[im_id]
            for anno in item["annotations"]:
                anno["image_id"] = im_id_int
                anno['category_id'] = anno["labels"][0]["id"]
                anno['score'] = anno["labels"][0]["confidence"]
                new_predictions.append(anno)

        new_references = defaultdict(list)
        for item in references:
            im_id = item["image_id"]
            img = self.image_dict[im_id]
            im_id_int = self.img_id_str2int[im_id]
            for anno in item["annotations"]:
                anno["image_id"] = im_id_int
                anno["width"] = img["width"]
                anno["height"] = img["height"]
                anno['ignore'] = anno['ignore'] if 'ignore' in anno else 0
                anno['ignore'] = "iscrowd" in anno and anno["iscrowd"]
                anno['category_id'] = anno["labels"][0]["id"]
                new_references[im_id_int].append(anno)

        return new_predictions, new_references

    def _format_object_detection_result(self, metric_result: Dict):
        metric = ObjectDetectionMetric(createdAt=format_time(), labels=self.labels)
        return metric_result

    def _format_to_classification(self, predictions: List[Dict], references: List[Dict]):
        """
        Format to classification metric.
        """
        pass

    def compute(self):
        """
        Compute metric.
        """
        results = {}
        for metric in self.metric_name:
            results[metric.name] = metric.compute()

        return results

    def save(self, metric_result: Dict, output_uri: str = None):
        """
        Save metric.
        """
        if output_uri is None:
            output_uri = os.path.join(self.tracker_client.job_work_dir, DEFAULT_METRIC_FILE_NAME)

        metric_result = self._format_object_detection_result(metric_result=metric_result)

        write_file(obj=metric_result, output_dir=os.path.dirname(output_uri), file_name=os.path.basename(output_uri))

    def __call__(self, predictions: List[Dict], references: List[Dict], output_uri: str):
        self.update(predictions=predictions, references=references)
        results = self.compute()
        self.save(metric_result=results, output_uri=output_uri)