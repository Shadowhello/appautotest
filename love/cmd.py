#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from abc import ABCMeta, abstractmethod
import settings

class BaseInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self,argv=settings.Command.HELP):
        pass

    @abstractmethod
    def usage(self,argv=settings.Command.HELP):
        pass

    @abstractmethod
    def updatehtml(self,argv=settings.Command.HELP):
        pass

    @abstractmethod
    def htmltoxml(self,argv=settings.Command.HELP):
        pass

    @abstractmethod
    def xmltoscript(self,argv=settings.Command.HELP):
        pass