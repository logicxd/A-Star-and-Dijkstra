# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:04:43 2019

@author: Aung David Moe
"""
import numpy as np
import operator

class Navigator():
    @staticmethod
    def cost(startPosition, endPosition, maze):
        # TODO this only assumes startPosition and endPosition are neighbors.
        # Might be worth it to check again later if this needs to account across 
        # multiple distances but most likely not. 
        row = endPosition[1]
        col = endPosition[0]
        return maze[row][col]
    
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
        row = position[1]
        col = position[0]
        shape = np.array(maze).shape
        isValid = row >= 0 and col >= 0
        isValid = isValid and row < shape[1] and col < shape[0]
        isValid = isValid and maze[row][col] > 0
        return isValid
        
    # Helper functions
    
    @staticmethod
    def applyOffset(position, offset):
        return tuple(map(operator.add, position, offset))
    
    ####################