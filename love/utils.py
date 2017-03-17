#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import os
import sys
import json
import time
import logging
import logging.handlers
from md5 import md5

def get_time_stamp():
    return time.time()

def __format_time_stamp():
    return time.localtime(get_time_stamp())

def get_format_time(format_time = '%H:%M:%S'):
    return time.strftime(format_time, __format_time_stamp())

def get_current_time():
    return get_format_time('%H:%M:%S')

def get_current_date():
    return get_format_time('%Y-%m-%d')

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
                    help信息，当命令或参数有误，或着命令为help时

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

        -clear
                    python manage.py clear
                    清除项目中log和pyc文件
        """


class FileOperation(object):

    @classmethod
    def get_mad5(self, filepath):
        m = md5()
        a_file = open(filepath, 'rb')    #需要使用二进制格式读取文件内容
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()

    @classmethod
    def get_html_files(self, filepath):
        html_list = []
        for html in self.get_files(filepath):
            if ".html" in html:
                html_list.append(html)
        return html_list

    @classmethod
    def get_files(self,filepath):
       return os.listdir(filepath)

    @classmethod
    def load_json(self,filename):
        with open(filename) as json_file:
            data = json.load(json_file)
        return data

    @classmethod
    def store_json(self,filename,data):
        with open(filename, 'w+') as json_file:
            json_file.write(json.dumps(data))


