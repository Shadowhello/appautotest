#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import os
import sys
import time
import logging
import logging.handlers
import settings


'''
Use set_logger to change settings 
 
    # Change limit size in bytes of default rotating action 
    log.set_logger(limit = 10240) # 10M 
 
    # Use time-rotated file handler, each day has a different log file, see 
    # logging.handlers.TimedRotatingFileHandler for more help about 'when' 
    log.set_logger(when = 'D', limit = 1) 
 
    # Use normal file handler (not rotated) 
    log.set_logger(backup_count = 0) 
 
    # File log level set to INFO, and stdout log level set to DEBUG 
    log.set_logger(level = 'DEBUG:INFO') 
 
    # Both log level set to INFO 
    log.set_logger(level = 'INFO') 
 
    # Change default log file name and log mode 
    log.set_logger(filename = 'yyy.log', mode = 'w') 
 
    # Change default log formatter 
    log.set_logger(fmt = '[%(levelname)s] %(message)s' 
'''  
  
# Color escape string  
COLOR_RED='\033[1;31m'  
COLOR_GREEN='\033[1;32m'  
COLOR_YELLOW='\033[1;33m'  
COLOR_BLUE='\033[1;34m'  
COLOR_PURPLE='\033[1;35m'  
COLOR_CYAN='\033[1;36m'  
COLOR_GRAY='\033[1;37m'  
COLOR_WHITE='\033[1;38m'  
COLOR_RESET='\033[1;0m'  
  
# Define log color  
LOG_COLORS = {  
    'DEBUG': '%s',  
    'INFO': COLOR_GREEN + '%s' + COLOR_RESET,  
    'WARNING': COLOR_YELLOW + '%s' + COLOR_RESET,  
    'ERROR': COLOR_RED + '%s' + COLOR_RESET,  
    'CRITICAL': COLOR_RED + '%s' + COLOR_RESET,  
    'EXCEPTION': COLOR_RED + '%s' + COLOR_RESET,  
}  
  
# Global logger  
log = None  
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class ColoredFormatter(logging.Formatter):  
    '''''A colorful formatter.'''  
  
    def __init__(self, fmt = None, datefmt = None):  
        logging.Formatter.__init__(self, fmt, datefmt)  
  
    def format(self, record):  
        level_name = record.levelname  
        msg = logging.Formatter.format(self, record)  
  
        return LOG_COLORS.get(level_name, '%s') % msg  
  
def add_handler(cls, level, fmt, colorful, **kwargs):  
    '''''Add a configured handler to the global logger.'''  
    global log  
  
    if isinstance(level, str):  
        level = getattr(logging, level.upper(), logging.DEBUG)  
  
    handler = cls(**kwargs)  
    handler.setLevel(level)  
  
    if colorful:  
        formatter = ColoredFormatter(fmt)  
    else:  
        formatter = logging.Formatter(fmt)  
  
    handler.setFormatter(formatter)  
    log.addHandler(handler)  
  
    return handler  
  
def add_streamhandler(level, fmt):  
    '''''Add a stream handler to the global logger.'''  
    return add_handler(logging.StreamHandler, level, fmt, True)  
  
def add_filehandler(level, fmt, filename , mode, backup_count, limit, when):  
    '''''Add a file handler to the global logger.'''  
    kwargs = {}  
  
    # If the filename is not set, use the default filename  
    if filename is None:  
        filename = getattr(sys.modules['__main__'], '__file__', 'log.py')  
        filename = os.path.basename(filename.replace('.py', '.log'))  
        filename = os.path.join(BASE_DIR, filename)  
  
    kwargs['filename'] = filename  
  
    # Choose the filehandler based on the passed arguments  
    if backup_count == 0: # Use FileHandler  
        cls = logging.FileHandler  
        kwargs['mode' ] = mode  
    elif when is None:  # Use RotatingFileHandler  
        cls = logging.handlers.RotatingFileHandler  
        kwargs['maxBytes'] = limit  
        kwargs['backupCount'] = backup_count  
        kwargs['mode' ] = mode  
    else: # Use TimedRotatingFileHandler  
        cls = logging.handlers.TimedRotatingFileHandler  
        kwargs['when'] = when  
        kwargs['interval'] = limit  
        kwargs['backupCount'] = backup_count  
  
    return add_handler(cls, level, fmt, False, **kwargs)  
  
def init_logger():  
    '''''Reload the global logger.'''  
    global log  
  
    if log is None:  
        log = logging.getLogger()  
    else:  
        logging.shutdown()  
        log.handlers = []  
  
    log.setLevel(logging.DEBUG)  
  
def set_logger(filename = None, mode = 'a', s_level='DEBUG',f_level='DEBUG', 
               fmt = '[%(levelname)s] %(asctime)s %(message)s',  
               backup_count = 5, limit = 20480, when = None, is_add_log_file=False):  
    '''''Configure the global logger.'''  
 
    init_logger()  
    add_streamhandler(s_level, fmt)
    if is_add_log_file:
        add_filehandler(f_level, fmt, filename, mode, backup_count, limit, when)  
  
    # Import the common log functions for convenient  
    import_log_funcs()  
  
def import_log_funcs():  
    '''''Import the common log functions from the global logger to the module.'''  
    global log  
  
    curr_mod = sys.modules[__name__]  
    log_funcs = ['debug', 'info', 'warning', 'error', 'critical',  
                 'exception']  
  
    for func_name in log_funcs:  
        func = getattr(log, func_name)  
        setattr(curr_mod, func_name, func)  
  
# Set a default logger  
set_logger(filename=settings.LOG_FILE_PATH, mode=settings.LOG_WRITE_MODE, s_level=settings.LOG_STREAM_LEVEL,
    f_level=settings.LOG_FILE_LEVEL, fmt=settings.LOG_FORMAT, backup_count=settings.LOG_BACKUP_COUNT,
    limit=settings.LOG_FILE_SIZE_LIMIT, when=settings.LOG_WHEN,is_add_log_file=settings.LOG_IS_FILE)



