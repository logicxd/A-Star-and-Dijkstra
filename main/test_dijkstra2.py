# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:58:00 2019

@author: Aung David Moe
"""
import unittest
from my_logger import test_logger as logger
from astar.AStar import Node 
from astar.AStar import AStar

class Expando():
    pass

class Test5by5Dijkstra2(unittest.TestCase):    
    def setUp(self):
        self.search = Test5by5Dijkstra2.search
    
    @classmethod
    def setUpClass(cls):
        cls.setUpSearch()
        logger.debug(f"\n{cls.search.pathMap}")
        logger.debug(f"\n{cls.search.path}")

    @classmethod
    def setUpSearch(cls):
        search = Expando()
        search.maze = [[1, 1, 1, 1, 1],
                       [1, 0, 1, 0, 1],
                       [1, 1, 1, 1, 1],
                       [0, 1, 0, 1, 0],
                       [1, 1, 1, 1, 1]]
        search.totalNodes = 20
        search.startPosition = (0,0)
        search.endPosition = (4,4)
        search.astar = AStar()
        search.pathMap = search.astar.findPath(search.maze, search.startPosition, search.endPosition)
        search.path = search.astar.pathToNode(search.pathMap, search.endPosition)
        cls.search = search

    def testCount(self):
        search = self.search
        logger.info(f"Nodes searched: {len(search.pathMap)}/{search.totalNodes}")
        self.assertEqual(len(search.pathMap), 20)
   
    def testEndNodeInSolution(self):
        search = self.search
        self.assertTrue(search.endPosition in search.pathMap)
    
    def testTotalCostToEndNode(self):
        search = self.search
        endNode = search.pathMap[search.endPosition]
        logger.info(f"Total cost: {endNode.g}")
        self.assertEqual(endNode.g, 8)
        
    def testPathToNode(self):
        search = self.search
        self.assertEqual(len(search.path), 9)
        self.assertEqual(search.path[0], Node(search.startPosition))
        self.assertEqual(search.path[1], Node((0, 1)))
        self.assertEqual(search.path[2], Node((0, 2)))
        self.assertEqual(search.path[3], Node((1, 2)))
        self.assertEqual(search.path[4], Node((2, 2)))
        self.assertEqual(search.path[5], Node((2, 3)))
        self.assertEqual(search.path[6], Node((3, 3)))
        self.assertEqual(search.path[7], Node((4, 3)))
        self.assertEqual(search.path[8], Node(search.endPosition))
        
if __name__ == '__main__':
    unittest.main()

