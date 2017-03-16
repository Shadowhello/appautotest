from abc import ABCMeta, abstractmethod

class BaseInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self,argv="help"):
        pass

    @abstractmethod
    def usage(self,argv="help"):
        pass

    @abstractmethod
    def updatehtml(self,argv="help"):
        pass

    @abstractmethod
    def htmltoxml(self,argv="help"):
        pass

    @abstractmethod
    def xmltoscript(self,argv="help"):
        pass