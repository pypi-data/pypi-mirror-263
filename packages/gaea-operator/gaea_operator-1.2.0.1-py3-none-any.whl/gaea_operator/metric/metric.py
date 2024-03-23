#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/7
# @Author  : yanxiaodong
# @File    : metric.py
"""
import os
from typing import Dict

import logit
from gaea_tracker import ExperimentTracker
from windmillclient.client.windmill_client import WindmillClient
from windmilltrainingv1.client.training_api_project import parse_project_name

from gaea_operator.utils import read_file, format_time, write_file, DEFAULT_METRIC_FILE_NAME
from .types.metric import BaseMetric


def update_metric_file(windmill_client: WindmillClient,
                       tracker_client: ExperimentTracker,
                       dataset_name: str,
                       model_object_name: str,
                       model_artifact_name: str):
    """
    Update metric file.
    """
    response = windmill_client.get_artifact(object_name=model_object_name, version="best")
    logit.info(f"Get artifact name {model_object_name} response {response}")

    base_metric = BaseMetric(modelName=model_artifact_name, datasetName=dataset_name, updatedAt=format_time())
    if getattr(response, "name"):
        if response.name != model_artifact_name:
            logit.info(f"Get baseline model name {response.name}")
            baseline_model_name = response.name
            tags = [{"modelName": baseline_model_name}, {"datasetName": dataset_name}]
            workspace_id, project_name = parse_project_name(tracker_client.project_name)
            response = windmill_client.list_job(workspace_id=workspace_id, project_name=project_name, tags=tags)
            if len(response.result) > 0:
                base_metric.baselineJobName = response.result[0]["name"]
            logit.info(f"Base metric dict is {base_metric.dict()}")

    metric_dir = tracker_client.job_work_dir
    metric_data = read_file(input_dir=metric_dir, file_name=DEFAULT_METRIC_FILE_NAME)
    metric_data.update(base_metric.dict())
    write_file(obj=metric_data, output_dir=metric_dir, file_name=DEFAULT_METRIC_FILE_NAME)


def get_score_from_file(filepath: str, metric_name: str):
    """
    Get metric name score from file.
    """
    metric_data = read_file(input_dir=os.path.dirname(filepath), file_name=os.path.basename(filepath))
    return get_score_from_metric_raw(metric_data=metric_data, metric_name=metric_name)


def get_score_from_metric_raw(metric_data: Dict, metric_name: str):
    """
    Get metric name score from raw.
    """
    for metric in metric_data["metrics"]:
        if metric["name"] == metric_name:
            if isinstance(metric["result"], Dict):
                return list(metric["result"].values())[0]
            return metric["result"]

