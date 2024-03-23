#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/26
# @Author  : yanxiaodong
# @File    : config.py
"""
from typing import Dict
import os
from abc import ABCMeta, abstractmethod

from gaea_tracker import ExperimentTracker
from windmillclient.client.windmill_client import WindmillClient
from windmillmodelv1.client.model_api_model import ModelMetadata, InputSize

from gaea_operator.utils import DEFAULT_TRANSFORM_CONFIG_FILE_NAME
from .generate_transform_config import generate_transform_config
from .modify_package_files import ModifyEnsembleFile
from .generate_transform_config import KEY_MAX_BATCH_SIZE, KEY_MAX_BOX_NUM
from .modify_package_files import ModifyPackageFiles


class Config(metaclass=ABCMeta):
    """
    Config write for train, transform and package.
    """
    device_type_t4 = "t4"
    device_type_a100 = "a100"
    device_type_v100 = "v100"
    device_type_r200 = "r200"
    device_type_k200 = "k200"
    device_type2model_format = {device_type_t4: "TensorRT",
                                device_type_a100: "TensorRT",
                                device_type_v100: "TensorRT",
                                device_type_r200: "PaddleLite",
                                device_type_k200: "PaddleLite"}

    def __init__(self, windmill_client: WindmillClient, tracker_client: ExperimentTracker, metadata: Dict = {}):
        self.windmill_client = windmill_client
        self.tracker_client = tracker_client
        self._metadata = metadata

    @property
    def metadata(self):
        """
        Get metadata.
        """
        return self._metadata

    def write_train_config(self,
                           dataset_uri: str,
                           model_uri: str,
                           advanced_parameters: dict,
                           pretrain_model_uri: str):
        """
        Config write for train.
        """
        pass

    def write_eval_config(self, dataset_uri: str, model_uri: str,):
        """
        Config write for eval.
        """
        pass

    def write_transform_config(self, model_uri: str, advanced_parameters: dict):
        """
        Config write for transform.
        """
        cfg_path = os.path.join(model_uri, DEFAULT_TRANSFORM_CONFIG_FILE_NAME)
        self._update_transform_metadata(advanced_parameters)

        generate_transform_config(advanced_parameters, cfg_path, self.metadata)

    def write_sub_model_config(self, transform_model_uri: str, modify_model_names: dict):
        """
        Config write for package.
        """
        pass

    def write_triton_package_config(self,
                                    transform_model_uri: str,
                                    ensemble_model_uri: str,
                                    modify_model_names: dict,
                                    ensemble_local_name: str):
        """
        Config write for package.
        """
        cfg = ModifyPackageFiles(transform_model_uri=transform_model_uri,
                                 ensemble_model_uri=ensemble_model_uri,
                                 modify_model_names=modify_model_names,
                                 ensemble_local_name=ensemble_local_name)
        cfg.modify_ppyoloe()

    def write_ensemble_config(self, ensemble_model_uri: str, model_config: Dict):
        """
        Config write for ensemble.
        """
        cfg = ModifyEnsembleFile(ensemble_model_uri=ensemble_model_uri,
                                 model_config=model_config)
        cfg.modify_ensemble()

    def _update_train_metadata(self, advanced_parameters: Dict):
        meta_data = ModelMetadata(experimentName=self.tracker_client.experiment_name,
                                  experimentRunID=self.tracker_client.run_id)
        self._metadata.update(meta_data.dict())

    def _update_transform_metadata(self, advanced_parameters: Dict):
        meta_data = ModelMetadata(algorithmParameters={
            'inferenceMaxBatchSize': int(advanced_parameters[KEY_MAX_BATCH_SIZE]),
            'maxBoxNum': int(advanced_parameters[KEY_MAX_BOX_NUM])})
        self._metadata.update(meta_data.dict())
