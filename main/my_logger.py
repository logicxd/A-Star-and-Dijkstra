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
logging.basicConfig(level=logging.DEBUG)
astar_logger = logging.getLogger('AStar')
test_logger = logging.getLogger('test')

def setupAStarLogger():
    astar_logger.setLevel(logging.WARNING)  
#    astar_logger.setLevel(logging.DEBUG)          

def setupTestLogger():
    test_logger.setLevel(logging.WARNING)    
#    test_logger.setLevel(logging.INFO)  
#    test_logger.setLevel(logging.DEBUG)
    
setupAStarLogger()
setupTestLogger()