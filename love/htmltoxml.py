#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import os
import sys
import json
import time
from mylog import log

__author__ = "weiwei.lui"

"""
使用实际的绝对路径
python manage.py htmltoxml /appautotest/files/vivo/html.json

把html.json里面配置的html文件全部转换成xml文件，放到xml目录下
同时，生成xml.json文件，记录xml目录下所有的xml文件

"""

# 流程
# 1 读取argv，获取配置html.json里 "update_app"信息
# 2 根据"update_app"的信息，依次解析里面的html


def translate(argv):
    log.debug(argv)

