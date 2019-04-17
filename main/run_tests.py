#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:36:39 2019

@author: aungmoe
"""

import unittest
import os
import logging
from my_logger import logger
from my_logger import test_logger
logger.setLevel(logging.WARNING)  
test_logger.setLevel(logging.WARNING)

loader = unittest.TestLoader()
start_dir = os.getcwd()
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)