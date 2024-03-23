#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/23
# @Author  : yanxiaodong
# @File    : classify.py
"""
import os
import json
from argparse import ArgumentParser

from gaea_tracker import ExperimentTracker
from logit.base_logger import setup_logger
from windmillmodelv1.client.model_api_model import parse_model_name, get_model_name
from windmillmodelv1.client.model_api_modelstore import parse_modelstore_name
from windmillclient.client.windmill_client import WindmillClient
import logit

from gaea_operator.dataset import ImageNetDataset
from gaea_operator.config import ClassifyConfig
from gaea_operator.trainer import Trainer
from gaea_operator.model import Model
from gaea_operator.metric import get_score_from_file
from gaea_operator.utils import write_file


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--windmill-project-name", type=str, default=os.environ.get("WINDMILL_PROJECT_NAME"))
    parser.add_argument("--windmill-public-modelstore",
                        type=str,
                        default=os.environ.get("WINDMILL_PUBLIC_MODELSTORE", "workspaces/public/modelstores/public"))
    parser.add_argument("--windmill-tracking-uri", type=str, default=os.environ.get("WINDMILL_TRACKING_URI"))
    parser.add_argument("--windmill-experiment-name", type=str, default=os.environ.get("WINDMILL_EXPERIMENT_NAME"))
    parser.add_argument("--windmill-experiment-kind", type=str, default=os.environ.get("WINDMILL_EXPERIMENT_KIND"))
    parser.add_argument("--windmill-train-dataset-name",
                        type=str,
                        default=os.environ.get("WINDMILL_TRAIN_DATASET_NAME"))
    parser.add_argument("--windmill-val-dataset-name", type=str, default=os.environ.get("WINDMILL_VAL_DATASET_NAME"))
    parser.add_argument("--windmill-model-name", type=str, default=os.environ.get("WINDMILL_MODEL_NAME"))
    parser.add_argument("--windmill-model-display-name",
                        type=str,
                        default=os.environ.get("WINDMILL_MODEL_DISPLAY_NAME"))
    parser.add_argument("--advanced-parameters", type=str, default=os.environ.get("ADVANCED_PARAMETERS", "{}"))

    parser.add_argument("--output-model-uri", type=str, default=os.environ.get("OUTPUT_MODEL_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))

    args, _ = parser.parse_known_args()

    return args


def classify_train(args):
    """
    Train component for classify model.
    """
    windmill_client = WindmillClient(ak=args.windmill_ak,
                                     sk=args.windmill_sk,
                                     endpoint=args.windmill_endpoint)
    tracker_client = ExperimentTracker(windmill_client=windmill_client,
                                       tracking_uri=args.windmill_tracking_uri,
                                       experiment_name=args.windmill_experiment_name,
                                       experiment_kind=args.windmill_experiment_kind,
                                       project_name=args.windmill_project_name)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))

    dataset_uri = "/home/windmill/tmp/dataset"
    classify_dataset = ImageNetDataset(windmill_client=windmill_client, work_dir=tracker_client.work_dir)
    # 1. 合并train分片数据集
    classify_dataset.concat_dataset(dataset_name=args.windmill_train_dataset_name,
                                output_dir=dataset_uri,
                                mode=ImageNetDataset.mode_keys[0])

    # 2. 合并val分片数据集
    classify_dataset.concat_dataset(dataset_name=args.windmill_val_dataset_name,
                                output_dir=dataset_uri,
                                mode=ImageNetDataset.mode_keys[1])

    # 3. 下载预训练模型
    pretrain_name = get_model_name(parse_modelstore_name(args.windmill_public_modelstore).workspace_id,
                                   parse_modelstore_name(args.windmill_public_modelstore).local_name,
                                   "ResNet18_pretrained")
    pretrain_model_uri = "/home/windmill/tmp/pretrain"
    windmill_client.download_artifact(object_name=pretrain_name, version="latest", output_uri=pretrain_model_uri)

    # 4. 生成训练配置文件，固定名字 train_config.yaml，保存在 model_uri
    ClassifyConfig(windmill_client=windmill_client).write_train_config(
        dataset_uri=dataset_uri,
        model_uri=args.output_model_uri,
        advanced_parameters=json.loads(args.advanced_parameters),
        pretrain_model_uri=pretrain_model_uri)

    # 5. 训练
    trainer = Trainer(framework="PaddlePaddle", tracker_client=tracker_client)
    metric_names = ["ACC"]
    trainer.track_model_score(metric_names=metric_names)
    trainer.launch()

    # 6. 创建模型
    metric_name: str = "boundingBoxMeanAveragePrecision" # need modify
    current_score = get_score_from_file(filepath=os.path.join(args.output_model_uri, "metric.json"),
                                        metric_name=metric_name)
    best_score, version = Model(windmill_client=windmill_client). \
        get_best_model_score(model_name=args.windmill_model_name, metric_name=metric_name)
    tags = {metric_name: current_score}
    alias = None
    if current_score >= best_score and version is not None:
        alias = ["best"]
        logit.info(
            f"{metric_name.capitalize()} current score {current_score} >= {best_score}, update [best]")
        tags.update(
            {f"bestReason": f"current.score({current_score}) greater than {version}.score({best_score})"})
    if version is None:
        alias = ["best"]
        logit.info(f"First alias [best] score: {current_score}")
        tags.update({f"bestReason": "current.score({current_score})"})

    model_name_instance = parse_model_name(args.windmill_public_modelstore)
    workspace_id = model_name_instance.workspace_id
    model_store_name = model_name_instance.model_store_name
    local_name = model_name_instance.local_name
    response = windmill_client.create_model(workspace_id=workspace_id,
                                            model_store_name=model_store_name,
                                            local_name=local_name,
                                            display_name=args.windmill_model_display_name,
                                            category="Image/ImageClassification/MultiClass",
                                            model_formats=["PaddlePaddle"],
                                            artifact_alias=alias,
                                            artifact_tags=tags,
                                            artifact_uri=args.model_uri)

    # 7. 输出文件
    write_file(obj=response, output_dir=args.output_model_uri)


if __name__ == "__main__":
    args = parse_args()
    classify_train(args=args)
