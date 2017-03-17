#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import os
import sys
import json
from cmd import BaseInterface
import settings
from utils import FileOperation
from htmltoxml import translate
from mylog import log


class CommandHandler(BaseInterface):

    __all__ = ["help", "run", "updatehtml", "htmltoxml", "xmltoscript", "clear"]


    def clear(self, argv=utils.Command.HELP):
        def rm(path, filepath):
            for filename in filepath:
                if "." in filename:
                    if filename.split('.')[1] in ["log", "pyc"]:
                        log.info("clear "+filename)
                        os.remove(os.path.join(path, filename))
        root_path = settings.BASE_DIR
        root_filepath = os.listdir(root_path) 
        love_path = os.path.join(root_path, "love")
        love_filepath =os.listdir(love_path)
        rm(root_path, root_filepath)
        rm(love_path, love_filepath)


    def help(self,argv=utils.Command.HELP):
        log.info(utils.Command.USAGE_INFO) 
        

    def run(self,argv=utils.Command.HELP):
        if argv == utils.Command.HELP:
            self.help()
        print argv

    
    def updatehtml(self,argv=utils.Command.HELP):
        log.info("updatehtml")
        if argv == utils.Command.HELP:
            self.help()
        
        html_file_path = argv   # html文件路径
        html_file_list = []     # 所有html文件列表
        json_data = {}          # json文件数据
        json_file_path = os.path.join(html_file_path, "html.json") # html.json文件路径

        if os.path.exists(html_file_path):
            html_file_list = FileOperation.get_html_files(html_file_path)
            # log.debug(html_file_list)

            if not os.path.exists(json_file_path):
                json_data = utils.DataTpl.HTML_INFO_JSON
            else:
                json_data=utils.FileOperation.load_json(json_file_path)

            json_data["info"]={
                "time": utils.get_current_date() + " " + utils.get_current_time(),
                "count": len(html_file_list),
                "path": html_file_path
            }
            json_data['update_app']={} #初始化json的update_app信息

            # 遍历html文件列表,更新到json文件中 
            for html_file in html_file_list:
                html_file_name = html_file.split(".")[0] # 去掉html后缀
                # 获取html文件的md5值，用于判断该文件是否更改
                html_file_md5 = FileOperation.get_mad5(os.path.join(html_file_path, html_file))
                if html_file_name in json_data["all_app"].keys(): # json文件中已保存过该文件                 
                    if html_file_md5 != json_data["all_app"][html_file_name]["md5"]: # 如果md5值不同，则说明更改过
                        json_data["all_app"][html_file_name]["md5"] = html_file_md5
                        json_data["update_app"][html_file_name]={
                            "name": html_file,
                            "md5": html_file_md5
                        }
                else:
                    json_data["all_app"][html_file_name]={
                        "name": html_file,
                        "md5": html_file_md5
                    }
                    json_data["update_app"][html_file_name]={
                        "name": html_file,
                        "md5": html_file_md5
                    }
            # 从json中移除已删掉的html文件
            for app in json_data['all_app'].keys():
                if app+".html" not in html_file_list:
                    json_data["all_app"].pop(app)

            # log.info(json_data)
            # 保存
            utils.FileOperation.store_json(json_file_path, json_data)
            log.info("成功更新html.json")
        else:
            log.error("File '{0}' not exists !".format(html_file_path))
            self.help()
            return False
    
    def htmltoxml(self,argv=utils.Command.HELP):
        if argv == utils.Command.HELP:
            self.help()
        translate(argv)

    
    def xmltoscript(self,argv=utils.Command.HELP):
        if argv == utils.Command.HELP:
            self.help()
        print argv


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
        self.command_handler = CommandHandler()
        

    def execute(self):
        """
        Given the command-line arguments, this figures out which subcommand is
        being run, creates a parser appropriate to that command, and runs it.
        """
        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = utils.Command.HELP  # Display help if no arguments were given.

        try:
            parameter = self.argv[2]
        except IndexError:
            parameter = utils.Command.HELP

        if subcommand in self.command_handler.__all__:
            getattr(self.command_handler, subcommand)(parameter)
        else:
            self.command_handler.help()
        


def execute_from_command_line(argv=None):
    """
    A simple method that runs a ManagementUtility.
    """
    utility = ManagementUtility(argv)
    utility.execute()
