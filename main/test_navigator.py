# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:06:04 2019

@author: Aung David Moe
"""
import unittest
from astar.Navigator import Navigator

class TestMyAIMovements(unittest.TestCase):
    def setUp(self):
        self.maze5by5 = [[1, 1, 1, 0, 1],
                         [1, 0, 1, 1, 1],
                         [1, 1, 1, 0, 0],
                         [0, 1, 0, 0, 0],
                         [1, 1, 0, 0, 0]]

    # neighbors
    
    def testNeighborsMiddle(self):
        neighbors = Navigator.neighbors((2,2), self.maze5by5)
        self.assertEqual(len(neighbors), 2)
        self.assertIn((2,1), neighbors)
        self.assertIn((1,2), neighbors)
        
    def testNeighborsTopLeftCorner(self):
        neighbors = Navigator.neighbors((0,0), self.maze5by5)
        self.assertEqual(len(neighbors), 2)
        self.assertIn((0,1), neighbors)
        self.assertIn((1,0), neighbors)
        
    def testNeighborsBottomLeftCorner(self):
        neighbors = Navigator.neighbors((4,0), self.maze5by5)
        self.assertEqual(len(neighbors), 1)
        self.assertIn((4,1), neighbors)
        
    def testNeighborsTopRightCorner(self):
        neighbors = Navigator.neighbors((0,4), self.maze5by5)
        self.assertEqual(len(neighbors), 1)
        self.assertIn((1,4), neighbors)
    
if __name__ == '__main__':
    unittest.main()