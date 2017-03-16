#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Command(object):
    HELP          = "help"
    UPDATE_HTML   = "updatehtml"
    HTML_TO_XML   = "htmltoxml"
    XML_TO_SCRIPT = "xmltoscript"
    RUN           = "run"

    USAGE_INFO="""
        < subcommand >            < parameter >       description

        updatehtml

        htmltoxml

        toscript

        run
    """