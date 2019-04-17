# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:54:42 2019

@author: Aung David Moe
"""
import unittest
from my_logger import test_logger as logger
from astar.AStar import Node 
from astar.AStar import AStar

class Expando():
    pass

class Test5by5Dijkstra1(unittest.TestCase):
    def setUp(self):
        self.search = Test5by5Dijkstra1.search
    
    @classmethod
    def setUpClass(cls):
        cls.setUpSearch()
        logger.debug(f"\n{cls.search.pathMap}")
        logger.debug(f"\n{cls.search.path}")
    
    @classmethod
    def setUpSearch(cls):
        search = Expando()
        search.maze = [[1, 1, 1, 0, 1],
                       [1, 0, 1, 1, 1],
                       [1, 1, 1, 0, 0],
                       [0, 1, 0, 0, 0],
                       [1, 1, 0, 0, 0]]
        search.totalNodes = 14
        search.startPosition = (0,0)
        search.endPosition = (3,1)
        search.astar = AStar()
        search.pathMap = search.astar.findPath(search.maze, search.startPosition, search.endPosition)
        search.path = search.astar.pathToNode(search.pathMap, search.endPosition)
        cls.search = search

    def testCount(self):
        search = self.search
        logger.info(f"Nodes searched: {len(search.pathMap)}/{search.totalNodes}")
        self.assertEqual(len(search.pathMap), 10)        
   
    def testEndNodeInSolution(self):
        search = self.search
        self.assertTrue(search.endPosition in search.pathMap)
    
    def testTotalCostToEndNode(self):
        search = self.search
        endNode = search.pathMap[search.endPosition]
        logger.info(f"Total cost: {endNode.g}")
        self.assertEqual(endNode.g, 4)
        
    def testPathToNode(self):
        search = self.search
        self.assertEqual(len(search.path), 5)
        self.assertEqual(search.path[0], Node(search.startPosition))
        self.assertEqual(search.path[1], Node((1, 0)))
        self.assertEqual(search.path[2], Node((2, 0)))
        self.assertEqual(search.path[3], Node((2, 1)))
        self.assertEqual(search.path[4], Node(search.endPosition))
        
if __name__ == '__main__':
    unittest.main()