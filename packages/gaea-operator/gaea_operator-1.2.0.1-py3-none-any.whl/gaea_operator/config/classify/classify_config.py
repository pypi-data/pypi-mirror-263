#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/19
# @Author  : wanggaofei
# @File    : classify_config.py
"""
import os
import json

from gaea_operator.utils import DEFAULT_TRAIN_CONFIG_FILE_NAME
from ..config import Config
from .template.modify_train_parameter import generate_train_config
from ..modify_package_files import ModifyPackageFiles


class ClassifyConfig(Config):
    """
    Config write for train, transform and package.
    """

    def write_train_config(self,
                           dataset_uri: str,
                           model_uri: str,
                           advanced_parameters: dict,
                           pretrain_model_uri: str):
        """
        Config write for train of ppyoloe_plus_m model.
        """
        # 1. get model number
        tran_json_name = os.path.join(dataset_uri, 'labels.json')
        json_data = json.load(open(tran_json_name, "r"))
        num_classes = len(json_data)
        new_advanced_parameters = advanced_parameters.copy()
        new_advanced_parameters['Arch.class_num'] = str(num_classes)

        # 2. set dataset
        new_advanced_parameters['DataLoader.Train.dataset.image_root'] = dataset_uri
        new_advanced_parameters['DataLoader.Train.dataset.cls_label_path'] = os.path.join(dataset_uri, 'train.txt')
        new_advanced_parameters['DataLoader.Eval.dataset.image_root'] = dataset_uri
        new_advanced_parameters['DataLoader.Eval.dataset.cls_label_path'] = os.path.join(dataset_uri, 'val.txt')

        # 2. set pretrain model
        new_advanced_parameters['Global.pretrained_model'] = pretrain_model_uri

        # 2. generate train config file
        if not os.path.exists(model_uri):
            os.makedirs(model_uri, exist_ok=True)
        self._write_meta(model_uri)
        generate_train_config(new_advanced_parameters, json_data,
                              os.path.join(model_uri, DEFAULT_TRAIN_CONFIG_FILE_NAME))

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
                                 ensemble_local_name=ensemble_local_name
                                 )
        cfg.modify_classify()
