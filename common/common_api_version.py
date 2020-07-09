#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
@author：timothy
@file_name: common_api_version.py
@create date: 2019-10-27 13:41
@file_description：
"""
from enum import Enum, unique


@unique
class apiVersion(Enum):
    """
    api 版本枚举
    """
    version1 = 'v1'
    version2 = 'v2'