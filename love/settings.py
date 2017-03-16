#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# logger设置
LOG_STREAM_LEVEL = "DEBUG"
LOG_FILE_LEVEL   = "INFO"
LOG_FORMAT = '%(levelname)s  %(asctime)s [ %(filename)s, %(module)s, %(funcName)s, line:%(lineno)d ] : %(message)s' 
LOG_FILE_NAME = "log.log"
LOG_FILE_PATH = os.path.join(BASE_DIR, LOG_FILE_NAME)
LOG_BACKUP_COUNT = 5
LOG_FILE_SIZE_LIMIT = 20480
LOG_WRITE_MODE = "w"
LOG_WHEN = None
