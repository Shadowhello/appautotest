#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import os
import sys
import tools
from tools import settings
class ManagementUtility(object):
    """
    Encapsulates the logic of the django-admin and manage.py utilities.

    A ManagementUtility has a number of commands, which can be manipulated
    by editing the self.commands dictionary.
    """
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        self.settings_exception = None
        print self.argv





if __name__ == "__main__":
    # from tools import execute_from_command_line
    # execute_from_command_line(sys.argv)
    utility = ManagementUtility(sys.argv)
    # print sys.argv[1]
    # utility.execute()
    print settings.BASE_DIR