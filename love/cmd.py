#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod
import utils

class BaseInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self,argv=utils.Command.HELP):
        pass

    @abstractmethod
    def help(self,argv=utils.Command.HELP):
        pass

    @abstractmethod
    def updatehtml(self,argv=utils.Command.HELP):
        pass

    @abstractmethod
    def htmltoxml(self,argv=utils.Command.HELP):
        pass

    @abstractmethod
    def xmltoscript(self,argv=utils.Command.HELP):
        pass