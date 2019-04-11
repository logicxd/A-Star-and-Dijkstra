# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:04:43 2019

@author: Aung David Moe
"""

from enum import Enum
import numpy as np
import operator

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Navigator():
    @staticmethod
    def cost(startPosition, endPosition):
        return 1
    
    @staticmethod
    def neighbors(position, maze):
        neighbors = []
        for offset in [(0,-1), (0,1), (-1,0), (1,0)]:
            newPosition = Navigator.applyOffset(position, offset)
            if Navigator.isValidPosition(newPosition, maze):
                neighbors.append(newPosition)
        return neighbors
    
    @staticmethod
    def isValidPosition(position, maze):
        row = position[0]
        col = position[1]
        shape = np.array(maze).shape
        isValid = row >= 0 and col >= 0
        isValid = isValid and row < shape[0] and col < shape[1]
        isValid = isValid and maze[row][col] > 0
        return isValid
        
    # Helper functions
    
    @staticmethod
    def applyOffset(position, offset):
        return tuple(map(operator.add, position, offset))
    
    ####################