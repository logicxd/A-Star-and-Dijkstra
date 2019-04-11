# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:22:54 2019

For reference, logging levels are: 
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

@author: Aung David Moe
"""
import logging

# setup AStar logger
logger = logging.getLogger('AStar')
logger.setLevel(logging.WARNING)    
#logger.setLevel(logging.DEBUG)      

# setup test logger
logger = logging.getLogger('test')
logger.setLevel(logging.WARNING)    
logger.setLevel(logging.INFO)  
#logger.setLevel(logging.DEBUG)

def astarLogger():
    return logging.getLogger('AStar')

def testLogger():
    return logging.getLogger('test')