#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import os
import sys
from cmd import BaseInterface
import settings


class CommandHandler(BaseInterface):


    def usage(self,argv="help"):
        print settings.Command.USAGE_INFO
        

    def run(self,argv="help"):
        if argv == "help":
            self.usage()

    
    def updatehtml(self,argv="help"):
        if argv == "help":
            self.usage()

    
    def htmltoxml(self,argv="help"):
        if argv == "help":
            self.usage()

    
    def xmltoscript(self,argv="help"):
        if argv == "help":
            self.usage()


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
            subcommand = 'help'  # Display help if no arguments were given.

        try:
            parameter = self.argv[2]
        except IndexError:
            parameter = 'help'
            
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
