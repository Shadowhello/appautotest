#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import os
import sys
import json
import time
import logging

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


class FileOperation(object):

    @classmethod
    def get_mad5(self, filename):
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
    def store_json(self,filename,date):
        with open('data.json', 'w+') as json_file:
            json_file.write(json.dumps(data))
