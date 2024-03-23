#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/1
# @Author  : yanxiaodong
# @File    : Trainer.py
"""
import logit
from typing import List
import os
import time
import threading

from gaea_tracker import ExperimentTracker

from gaea_operator.metric import get_score_from_metric_raw
from gaea_operator.utils import read_file, DEFAULT_PADDLEPADDLE_MODEL_FILE_NAME


class Trainer(object):
    """
    Trainer class for different framework.
    """
    framework_paddlepaddle = "PaddlePaddle"
    framework_pytorch = "PyTorch"

    def __init__(self, framework: str, tracker_client: ExperimentTracker):
        self.framework = framework
        self.tracker_client = tracker_client

        self.training_exit_flag = False
        self._framework_check(framework=self.framework)

    def launch(self):
        """
        Launch the training process.
        """
        getattr(self, f"{self.framework.lower()}_launch")()

    def paddlepaddle_launch(self):
        """
        Launch the PaddleDetection training process.
        """
        from paddle.distributed.launch.main import launch
        launch()
        self.training_exit_flag = True

    def paddledet_export(self, model_dir: str):
        """
        Export the model to static.
        """
        from paddledet.tools import export_model
        weights = os.path.join(model_dir, DEFAULT_PADDLEPADDLE_MODEL_FILE_NAME)
        export_model.main(weights=weights, output_dir=model_dir)

    @classmethod
    def _framework_check(cls, framework: str):
        frameworks = [cls.framework_paddlepaddle, cls.framework_pytorch]
        logit.info(f"framework: {framework}")

        assert framework in frameworks, f"framework must be one of {frameworks}, but get framework {framework}"

    def _track_thread(self, metric_names: List):
        last_epoch, last_step = -1, -1
        while True:
            metric_filepath = os.path.join(self.tracker_client.job_work_dir, f"{self.tracker_client.run_id}.json")
            if self.training_exit_flag:
                _, _ = self._track_by_file(metric_filepath, metric_names, last_epoch, last_step)
                break
            last_epoch, last_step = self._track_by_file(metric_filepath, metric_names, last_epoch, last_step)
            time.sleep(30)

    def _track_by_file(self, filepath: str, metric_names: List, last_epoch: int, last_step: int):
        if os.path.exists(filepath):
            metric_data = read_file(input_dir=os.path.dirname(filepath), file_name=os.path.basename(filepath))
            epoch, step = metric_data["epoch"], metric_data["step"]
            if epoch == last_epoch and step == last_step:
                return epoch, step
            for name in metric_names:
                metric = get_score_from_metric_raw(metric_data=metric_data, metric_name=name)
                if metric is not None:
                    logit.info(f"Track metric {name} with value: {metric} on step {step} or epoch {epoch}")
                    self.tracker_client.log_metrics(metrics={name: metric}, epoch=epoch, step=step)

            return epoch, step
        return last_epoch, last_step

    def track_model_score(self, metric_names):
        """
        Track the score of model.
        """
        thread = threading.Thread(target=self._track_thread, args=(metric_names, ))
        thread.start()
