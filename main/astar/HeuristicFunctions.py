# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:00:31 2019

@author: Aung David Moe
"""

def manhattan(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return 1 * (dx + dy)

