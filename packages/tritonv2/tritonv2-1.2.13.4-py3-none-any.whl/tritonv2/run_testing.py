# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
"""
run_testing.py
"""
import os
import time
from argparse import ArgumentParser
from windmillclient.client.windmill_client import WindmillClient
from gaea_operator.metric import Metric
from gaea_tracker import ExperimentTracker
from logit.base_logger import setup_logger

time_pattern = "%Y-%m-%dT%H:%M:%SZ"


def parse_args():
    """
    Parse the command line arguments
    :return:
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK")
    )
    parser.add_argument(
        "--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK")
    )
    parser.add_argument(
        "--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT")
    )

    parser.add_argument(
        "--input-model-uri", type=str, default=os.environ.get("INPUT_MODEL_URI")
    )
    parser.add_argument(
        "--input-dataset-uri", type=str, default=os.environ.get("INPUT_DATASET_URI")
    )
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))

    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    args, _ = parser.parse_known_args()
    return args


def run_testing(args):
    """
    Testing
    :param args:
    :return:
    """

    windmill_client = WindmillClient(
        ak=args.windmill_ak, sk=args.windmill_sk, endpoint=args.windmill_endpoint
    )
    tracker_client = ExperimentTracker(windmill_client=windmill_client,
                                       tracking_uri=args.tracking_uri,
                                       experiment_name=args.experiment_name,
                                       experiment_kind=args.experiment_kind,
                                       project_name=args.project_name)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))

    metric = Metric(tracker_client=tracker_client)
    metric()

    time.sleep(15)


if __name__ == "__main__":
    args = parse_args()
    run_testing(args)
