#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("APP_TEST_SETTINGS_MODULE", "sys.settings")
    
    from tools import execute_from_command_line
    execute_from_command_line(sys.argv)