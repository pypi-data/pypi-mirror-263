#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/17
# @Author  : yanxiaodong
# @File    : metric.py
"""
from typing import Optional
from pydantic import BaseModel


LOSS_METRIC_NAME = "Loss"
MAP_METRIC_NAME = "mAP"
AP50_METRIC_NAME = "AP50"
AR_METRIC_NAME = "AR"
CONFUSION_MATRIX_METRIC_NAME = "confusionMatrix"
BOUNDING_BOX_LABEL_AVERAGE_PRECISION_METRIC_NAME = "boundingBoxLabelAveragePrecision"
BOUNDING_BOX_LABEL_RECALL_METRIC_NAME = "boundingBoxLabelRecall"
BOUNDING_BOX_MEAN_AVERAGE_PRECISION_METRIC_NAME = "boundingBoxMeanAveragePrecision"
BOUNDING_BOX_LABEL_METRIC_NAME = "boundingBoxLabelMetric"


class Label(BaseModel):
    """
    Labeled Object
    """
    id: int
    name: str


class BaseMetric(BaseModel):
    """
    Metric Object
    """
    artifactName: Optional[str] = None
    datasetName: Optional[str] = None
    baselineJobName: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None


class BaseTrainMetric(BaseModel):
    """
    Loss Metric
    """
    name: Optional[str] = None
    displayName: Optional[str] = None
    result: Optional[float] = None
