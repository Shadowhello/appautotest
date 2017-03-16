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


class CommandHandler(BaseInterface):

    __all__ = ["usage", "run", "updatehtml", "htmltoxml", "xmltoscript"]

    def usage(self,argv=settings.Command.HELP):
        print settings.Command.USAGE_INFO
        

    def run(self,argv=settings.Command.HELP):
        if argv == settings.Command.HELP:
            self.usage()
        print argv

    
    def updatehtml(self,argv=settings.Command.HELP):
        if argv == settings.Command.HELP:
            self.usage()
        
        html_file_path = argv
        html_file_list = []
        json_data = {}
        if os.path.exists(html_file_path):
            html_file_list = FileOperation.get_html_files(html_file_path)
            json_data = FileOperation.load_json(os.path.join(html_file_path, "html.json")) or settings.DataTpl.HTML_INFO_JSON
            json_data["info"]={
                "time": utils.get_current_date() + " " + utils.get_current_time(),
                "count": len(html_file_list),
                "path": html_file_path
            }

            for html_file in html_file_list:
                html_file_name = html_file.split(".")[0]
                html_file_md5 = FileOperation.get_mad5(os.path.join(html_file_path, html_file))
                if html_file_name in json_data["all_app"].keys():                  
                    if not html_file_md5 == json_data["all_app"][html_file_name]["md5"]:
                        json_data["all_app"][html_file_name]["md5"] = html_file_md5
                else:
                    json_data["all_app"][html_file_name]={
                        "name": html_file_name,
                        "md5": html_file_md5
                    }
                    json_data["all_app"][html_file_name]={
                        "name": html_file_name,
                        "md5": html_file_md5
                    }


        else:
            print "Error: File '{0}' not exists !".format(html_file_path)
            return False
    
    def htmltoxml(self,argv=settings.Command.HELP):
        if argv == settings.Command.HELP:
            self.usage()
        translate(argv)

    
    def xmltoscript(self,argv=settings.Command.HELP):
        if argv == settings.Command.HELP:
            self.usage()
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
            subcommand = settings.Command.HELP  # Display help if no arguments were given.

        try:
            parameter = self.argv[2]
        except IndexError:
            parameter = settings.Command.HELP
            
        if subcommand == settings.Command.RUN:
            self.command_handler.run(parameter)
        elif subcommand == settings.Command.UPDATE_HTML:
            self.command_handler.updatehtml(parameter)
        elif subcommand == settings.Command.HTML_TO_XML:
            self.command_handler.htmltoxml(parameter)
        elif subcommand == settings.Command.XML_TO_SCRIPT:
            self.command_handler.xmltoscript(parameter)
        else:
            self.command_handler.usage(parameter)
            

        


def execute_from_command_line(argv=None):
    """
    A simple method that runs a ManagementUtility.
    """
    utility = ManagementUtility(argv)
    utility.execute()
