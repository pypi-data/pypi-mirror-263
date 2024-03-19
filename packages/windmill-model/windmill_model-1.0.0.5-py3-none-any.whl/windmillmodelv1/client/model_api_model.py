#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/29
# @Author  : yanxiaodong
# @File    : model_api_model.py
"""
import re
from pydantic import BaseModel
from typing import Optional, List, Dict

model_name_regex = \
    re.compile("^workspaces/(?P<workspace_id>.+?)/modelstores/(?P<model_store_name>.+?)/models/(?P<local_name>.+?)$")


class ModelName:
    """
    The name of model.
    """
    def __init__(self, workspace_id: str = None, model_store_name: str = None, local_name: str = None):
        self.workspace_id = workspace_id
        self.model_store_name = model_store_name
        self.local_name = local_name


class Label(BaseModel):
    """
    The label of model.
    """
    id: Optional[str] = None
    name: Optional[str] = None


class InputSize(BaseModel):
    """
    The size of input.
    """
    width: Optional[int] = None
    height: Optional[int] = None


class ModelMetadata(BaseModel):
    """
    The metadata of model.
    """
    experimentName: Optional[str] = None
    experimentRunID: Optional[str] = None
    jobName: Optional[str] = None
    labels: Optional[List[Label]] = None
    algorithmParameters: Optional[Dict] = None
    maxBoxNum: Optional[int] = None
    inputSize: Optional[InputSize] = None
    extraLoadModel: Optional[List[str]] = None


def get_model_name(workspace_id: str, model_store_name: str, local_name: str):
    """
    get name
    """
    return "workspaces/" + workspace_id + "/modelstores/" + model_store_name + "/models/" + local_name


def parse_model_name(name: str) -> Optional[ModelName]:
    """
    Get workspace_id model_store_name and local name from model name.
    """
    m = model_name_regex.match(name)
    if m is None:
        return None
    return ModelName(m.group("workspace_id"), m.group("model_store_name"), m.group("local_name"))
