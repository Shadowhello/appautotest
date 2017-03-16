#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DataTpl(object):
    HTML_INFO_JSON ={
        "info":{"time":"", "count":"", "path":""},
        "all_app":{},
         "update_app":{}
    }

class Command(object):
    HELP          = "help"
    UPDATE_HTML   = "updatehtml"
    HTML_TO_XML   = "htmltoxml"
    XML_TO_SCRIPT = "xmltoscript"
    RUN           = "run"

    USAGE_INFO="""
        其中选项包括：

        -help           
                    python manage.py help
                    help信息，当命令或参数有误，或这命令为help时

        -updatehtml 
                    python manage.py updatehtml /file/path/htmldir 
                    更新html文件接口，执行后生成html.json                       

        -htmltoxml   
                    python manage.py htmltoxml /file/path/html.json    
                    更新html.json文件接口，html文件转换成[app.xml]文件

        -xmltoscript     
                    python manage.py xmltoscript /file/path/xml.json  
                    解析xml.json，生成可执行的python脚本                                 

        -run             
                    python manage.py run  /file/path/run.json         
                    执行run.json,依次执行文件里的配置脚本
        
        """