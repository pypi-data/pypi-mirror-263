# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
"""
testing.py
"""
import datetime
import hashlib
import json
import os
import time
from abc import ABC, abstractmethod
from argparse import ArgumentParser
from distutils.spawn import find_executable
from subprocess import DEVNULL, Popen, STDOUT, TimeoutExpired
import cv2
import pandas as pd
import ray
import requests
import numpy as np
from ray.data import Preprocessor, Dataset
from tritonclient.utils import triton_to_np_dtype
from tritonclient import http as http_client
from tritonv2.utils import list_stack_ndarray
from windmillclient.client.windmill_client import WindmillClient
from tritonv2.client_factory import TritonClientFactory
from gaea_operator.metric import Metric

time_pattern = "%Y-%m-%dT%H:%M:%SZ"


def read_file(input_dir: str, file_name: str = "response.json"):
    """
    Read the response list from a file.
    """
    with open(os.path.join(input_dir, file_name), "r") as f:
        data = json.load(f)

    return data


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
    args, _ = parser.parse_known_args()
    return args


class TritonServer(ABC):
    """
    Defines the interface for the objects created by
    TritonServerFactory
    """

    @abstractmethod
    def start(self, env=None):
        """
        Starts the tritonserver

        Parameters
        ----------
        env: dict
            The environment to set for this tritonserver launch
        """

    @abstractmethod
    def stop(self):
        """
        Stops and cleans up after the server
        """


class TritonServerConfig:
    """
    TritonServerConfig is a simple container class for the
    """

    def __init__(self, args: dict = None):
        """
        Construct TritonServerConfig
        """
        self._server_args = args

    def to_cli_string(self):
        """
        Returns the server arguments as a string
        """
        return " ".join(
            [f"--{key}={val}" for key, val in self._server_args.items() if val]
        )

    def to_args_list(self):
        """
        Returns the server arguments as a list
        """
        args_list = []
        args = self.to_cli_string().split()
        for arg in args:
            args_list += arg.split("=", 1)
        return args_list


class TritonServerLocal(TritonServer):
    """
    Concrete Implementation of TritonServer interface that runs
    tritonserver locally as as subprocess.
    """

    def __init__(self, server_cmd_path=None, config: TritonServerConfig = None):
        """
        Parameters
        ----------
        server_cmd_path  : str
            The absolute path to the tritonserver executable
        config : TritonServerConfig
            the config object containing arguments for this server instance
        """

        self._server_process = None
        self._server_config = config
        self._server_cmd_path = server_cmd_path
        self._http_base_uri = "http://localhost:8000"

        assert self._server_config[
            "model-repository"
        ], "Triton Server requires --model-repository argument to be set."

    def __getattr__(self, item):
        return f"'{item}' attribute does not exist!"

    def start(self, env=None):
        """
        Starts the tritonserver container locally
        """

        if self._server_cmd_path is None:
            self._server_cmd_path = find_executable("tritonserver")

        if self._server_path:
            # Create command list and run subprocess
            cmd = [self._server_cmd_path]
            cmd += self._server_config.to_args_list()

            # Set environment, update with user config env
            triton_env = os.environ.copy()

            if env:
                # Filter env variables that use env lookups
                for variable, value in env.items():
                    if value.find("$") == -1:
                        triton_env[variable] = value
                    else:
                        # Collect the ones that need lookups to give to the shell
                        triton_env[variable] = os.path.expandvars(value)

            triton_env["CUDA_VISIBLE_DEVICES"] = triton_env["NVIDIA_VISIBLE_DEVICES"]

            # Construct Popen command
            try:
                self._server_process = Popen(
                    cmd,
                    stdout=STDOUT,
                    stderr=STDOUT,
                    start_new_session=True,
                    universal_newlines=True,
                    env=triton_env,
                )
            except Exception as e:
                raise e

    def stop(self):
        """
        Stops the running tritonserver
        """

        # Terminate process, capture output
        if self._server_process is not None:
            self._server_process.terminate()
            try:
                self._server_process.communicate(
                    timeout=60,
                )
            except TimeoutExpired:
                self._server_process.kill()
                self._server_process.communicate()
            self._server_process = None

    def is_ready(self):
        """
        Check if the server is ready
        """
        try:
            response = requests.get(
                f"{self._http_base_uri}/v2/health/ready", timeout=60
            )
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError as e:
            time.sleep(1)
        return False


def _update_image_id_byMD5(df: pd.DataFrame) -> "pd.Series":
    """
    update image_id = MD5(row(file_name))
    :param row:
    :return:
    """
    df["image_id"] = df["file_name"].apply(
        lambda x: hashlib.md5(x.encode()).hexdigest()
    )
    image_id_series = df["image_id"].rename("image_id")
    return image_id_series


class AnnotationFormatter(Preprocessor):
    """
    AnnotationFormatter
    """

    def __init__(self, annotation_format, artifact_name: str = ""):
        """
        constructor
        :param annotation_format:
        :param artifact_name:
        """
        self._is_fittable = True
        self._annotation_format = annotation_format
        self._artifact_name = artifact_name

    def _fit(self, ds: "Dataset") -> "Preprocessor":
        """
        _fit
        :param ds:
        :return:
        """
        if self._annotation_format == "COCO":
            final_anno_ds = self._fit_coco(ds)
        # if self._annotation_format == "Gaea":
        #     final_anno_ds = self._fit_gaea(ds)
        self.stats_ = final_anno_ds
        return self

    def _group_by_image_id(self, group: pd.DataFrame) -> pd.DataFrame:
        """
        group bu image_id
        :param group:
        :return:
        """
        image_id = group["image_id"][0]
        ids = group["id"].tolist()
        annoations = list()
        for i in range(len(ids)):
            id = ids[i]
            bbox = group["bbox"].tolist()[i]
            segmentation = group["segmentation"].tolist()[i]
            area = group["area"].tolist()[i]
            cate = group["category_id"].tolist()[i]
            iscrowd = group["iscrowd"].tolist()[i]
            anno = {
                "id": id,
                "bbox": bbox,
                "segmentation": segmentation,
                "area": area,
                "labels": [{"id": cate, "confidence": 1}],
                "iscrowd": iscrowd,
            }
            annoations.append(anno)

        annoation_res = {
            "image_id": image_id,
            "created_at": datetime.datetime.utcnow().strftime(time_pattern),
            "annotations": [annoations],
            "doc_type": "annotation",
            "task_kind": "Manual",
            "artifact_name": self._artifact_name,
            "image_created_at": datetime.datetime.utcnow().strftime(time_pattern),
        }
        return pd.DataFrame(annoation_res)

    def _fit_coco(self, ds: "Dataset") -> "Dataset":
        # 展开 images
        image_ds = ds.flat_map(lambda row: row["images"])

        # 展开 annoations
        annoation_ds = ds.flat_map(lambda row: row["annotations"])

        # merge image_ds and annoation_ds on annoation_ds.image_id = image_ds.id
        drop_id_annotaion_ds = annoation_ds.drop_columns(cols=["id"])
        image_df = image_ds.to_pandas()
        annotation_df = drop_id_annotaion_ds.to_pandas()
        merged_df = pd.merge(annotation_df, image_df, left_on="image_id", right_on="id")
        #
        bboxs = merged_df["bbox"].tolist()
        segmentation = merged_df["segmentation"].tolist()
        normal_bbox_list = [arr.tolist() for arr in bboxs]
        normal_segmentation_list = [arr.tolist() for arr in segmentation]
        merged_df["bbox"] = normal_bbox_list
        merged_df["segmentation"] = normal_segmentation_list
        merged_annotaion_ds = ray.data.from_pandas(merged_df).drop_columns(
            cols=["image_id"]
        )

        # # update image_id to md5(file_name)
        updated_annoation_ds = merged_annotaion_ds.add_column(
            "image_id", lambda df: _update_image_id_byMD5(df)
        )
        droped_annoation_ds = updated_annoation_ds.drop_columns(
            cols=["file_name", "height", "width"]
        )
        # groupby and map_groups
        group_data = droped_annoation_ds.groupby("image_id")
        group_anno_ds = group_data.map_groups(lambda g: self._group_by_image_id(g))
        group_anno_ds = group_anno_ds.drop_columns(cols=["image_id"])

        return group_anno_ds


def gaeainfer_to_vistudioV1(raw_data, artifact_name):
    """
    Convert GaeaInfer format to VistudioV1 format
    :param raw_data:
    :param artifact_name:
    :return:
    """
    # 初始化annotations列表
    annotations_list = []

    # 为每个image_id处理annotations
    for item in raw_data:
        annotations = []
        image_id = item["image_id"]  # 假设这是一个递增的标识符

        for pred in item["predictions"]:
            bbox = pred["bbox"]
            area = pred["area"]
            labels = [
                {"id": category["id"], "confidence": category["confidence"]}
                for category in pred["categories"]
            ]

            annotation = {
                "id": image_id,  # 使用image_id作为annotation的id
                "bbox": bbox,
                "labels": labels,
                "area": area,
            }
            annotations.append(annotation)

        # 将每个图片的annotations加入到最终列表中
        annotations_list.append(
            {
                "doc_type": "annotation",
                "artifact_name": artifact_name,
                "task_kind": "Model",
                "annotations": annotations,
            }
        )

    return annotations_list


def image_preprocess(path: str, d_type):
    """
    Image preprocess
    :param path:
    :param d_type:
    :return:
    """
    frame = cv2.imread(path)
    img_resize = cv2.resize(frame, (1920, 1080))
    org_h, org_w, _ = img_resize.shape
    img_encode = cv2.imencode(".jpg", img_resize)[1]
    return np.frombuffer(img_encode.tobytes(), dtype=d_type)


def infer(triton_client, image_id, image_path):
    """
    Infer
    :param triton_client:
    :param image_id:
    :param image_path:
    :return:
    """
    input_metadata, output_metadata, batch_size = (
        triton_client.get_inputs_and_outputs_detail(model_name="ensemble")
    )

    file_names = [image_path]
    repeated_image_data = []
    for file_path in file_names:
        img = image_preprocess(
            file_path, triton_to_np_dtype(input_metadata[0]["datatype"])
        )
        repeated_image_data.append(np.array(img))

    batched_image_data = list_stack_ndarray(repeated_image_data)

    meta_json = json.dumps({"image_id": image_id})
    byte_meta_json = meta_json.encode()
    np_meta_json = np.frombuffer(byte_meta_json, dtype="uint8")
    send_meta_json = np.array(np_meta_json)
    send_meta_json = np.expand_dims(send_meta_json, axis=0)
    # build triton input
    inputs = [
        http_client.InferInput(
            input_metadata[0]["name"],
            list(batched_image_data.shape),
            input_metadata[0]["datatype"],
        ),
        http_client.InferInput(
            input_metadata[1]["name"],
            send_meta_json.shape,
            input_metadata[1]["datatype"],
        ),
    ]
    inputs[0].set_data_from_numpy(batched_image_data, binary_data=False)
    inputs[1].set_data_from_numpy(send_meta_json)
    # build triton output
    output_names = [output["name"] for output in output_metadata]
    outputs = []
    for output_name in output_names:
        outputs.append(http_client.InferRequestedOutput(output_name, binary_data=True))

    # infer
    result = triton_client.model_infer("ensemble", inputs, outputs=outputs)
    # print detailed output
    output_dict = {}
    for output_name in output_names:
        output_dict[output_name] = eval(result.as_numpy(output_name))

    return output_dict["skill_out_json"]


def run_testing(args):
    """
    Testing
    :param args:
    :return:
    """

    windmill_client = WindmillClient(
        ak=args.windmill_ak, sk=args.windmill_sk, endpoint=args.windmill_endpoint
    )

    model = read_file(args.input_model_uri)
    dataset = read_file(args.input_dataset_uri)

    windmill_client.model_dump(model["artifact"]["name"], "/home/model", "ensemble")
    # filesystem = windmill_client.suggest_first_filesystem(workspace_id=model["workspace_id"],
    #                                                       guest_name=model["name"])
    # download_by_filesystem(filesystem, dataset["artifact"]["uri"], "/home/dataset")

    triton_config_args = {
        "model-repository": "/home/model",
    }

    if model["preferModelServerParameters"]["backend"] is not None:
        triton_config_args["backend-config"] = model["preferModelServerParameters"][
            "backend"
        ]

    triton_server_config = TritonServerConfig(args=triton_config_args)

    triton_instance = TritonServerLocal(config=triton_server_config)
    triton_instance.start()

    while True:
        if triton_instance.is_ready():
            break

    triton_client = TritonClientFactory.create_http_client(
        server_url=triton_instance._http_base_uri
    )

    ds = ray.data.read_json(paths=[args.input_dataset_uri + "/val.json"])
    label_ds = ds.flat_map(lambda row: row["categories"])
    image_ds = ds.flat_map(lambda row: row["images"])
    image_ds = image_ds.add_column("image_id", lambda df: _update_image_id_byMD5(df))

    formatter = AnnotationFormatter("Gaea", artifact_name="test")
    references = formatter.fit(ds).stats_
    with open(args.input_dataset_uri + "/jsonls/annotation.jsonl", "w") as f:
        for i in references.iter_rows():
            f.write(json.dumps(i) + "\n")

    infer_raw = []
    for image in image_ds.iter_rows():
        infer_dict = infer(triton_client, image["image_id"], image["file_name"])
        infer_raw.append(infer_dict[0])

    predictions = gaeainfer_to_vistudioV1(infer_raw, model["artifact"]["name"])

    with open(args.input_dataset_uri + "/jsonls/prediction.jsonl", "w") as f:
        for p in predictions:
            f.write(json.dumps(p) + "\n")

    metric = Metric(
        category=model["category"]["category"],
        labels=label_ds.take_all(),
        images=image_ds.take_all(),
    )

    metric(
        predictions=predictions,
        references=references.take_all(),
        output_uri=args.output_uri,
    )

    triton_instance.stop()


if __name__ == "__main__":
    args = parse_args()
    run_testing(args)
