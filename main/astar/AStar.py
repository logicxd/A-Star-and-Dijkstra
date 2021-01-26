"""
Created on Thu Mar  7 23:45:21 2019

References: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

@author: Aung David Moe
"""
import heapq
from my_logger import astar_logger as logger
from astar.Navigator import Navigator

class Node():
    def __init__(self, currentPosition, parentPosition=None, g=0):
        """
        position is a tuple of integers e.g. (1,2)
        parentPosition is a tuple of integers e.g. (5,5)
        Nodes are equal if they have the same position.
        """
        self.position = currentPosition
        self.parentPosition = parentPosition
        self.g = g
        self.__description = f"Node{self.position} cost: {self.g}, parent: {self.parentPosition}\n"
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.position == other.position
    
    def __hash__(self):
        return hash(self.position)
    
    def __repr__(self):
        return self.__description
    
    def __str__(self):
        return self.__description
    
    def __lt__(self, other):
        return True if self.g < other.g else self.position[0] < other.position[0] 
    
class AStar():
    """
    f(x) is the total cost  of each node. Defined by f(x) = g(x) + h(x).
    g(x) is the real cost to reach a node x.
    h(x) is the approximate cost form node x to goal node. 
      This heuristic function should never overesimate the cost.
      If heuristic is 0, then it's Dijkstra.
    """
    
    def __init__(self, h=lambda start,end:0):
        # TODO type check heuristic function that accepts 2 parameters and returns a value.
        self.h = h       
    
    def findPath(self, maze, startPosition, endPosition):
        costPQ = self.__initializeCostPQ(startPosition)
        searchNodes = self.__initializeSearchNodes(startPosition)
        answerNodes = set()
        
        while len(costPQ) > 0:
            logger.debug(f"Priority Queue: {costPQ}")
            node = self.__nextBestNode(costPQ)
            self.__moveFromSearchToAnswer(node, searchNodes, answerNodes)
            
            if node.position == endPosition:
                break
            else:
                self.__updateCostForNeighborNodes(maze, endPosition, costPQ, searchNodes, answerNodes, node)
                
        return self.__convertSetToDictionary(answerNodes)
    
    def pathToNode(self, answerMap, endPosition):
        route = []
        node = answerMap[endPosition]
        while node.parentPosition != None:
            route.append(node)
            node = answerMap[node.parentPosition]
        route.append(node)
        route.reverse()
        return route
    
    # Private Helper Methods 
    
    def __initializeCostPQ(self, startPosition):
        costPQ = []
        node = Node(startPosition)
        self.__heapPush(costPQ, node, 0)
        return costPQ
    
    def __initializeSearchNodes(self, startPosition):
        node = Node(startPosition)
        return {node:node}
    
    def __nextBestNode(self, costPQ):
        return self.__heapPop(costPQ)
    
    def __moveFromSearchToAnswer(self, node, searchNodes, answerNodes):
        del searchNodes[node]
        answerNodes.add(node)
    
    def __updateCostForNeighborNodes(self, maze, endPosition, costPQ, searchNodes, answerNodes, node):
        for neighborPosition in Navigator.neighbors(node.position, maze):
            neighborNode = self.__getNeighborNode(neighborPosition, searchNodes)
                
            if neighborNode in answerNodes:
                continue
            
            newNode = self.__createNeighborNode(node, neighborPosition, maze)
            if newNode not in searchNodes:
                self.__addNodeToSearch(searchNodes, costPQ, newNode, endPosition)
            elif self.__isNewPathBetterThanOld(newNode, neighborNode, searchNodes, endPosition):
                self.__removeNodeFromSearch(searchNodes, costPQ, neighborNode)
                self.__addNodeToSearch(searchNodes, costPQ, newNode)
            elif neighborNode not in searchNodes:
                self.__addNodeToSearch(searchNodes, costPQ, newNode)

    def __getNeighborNode(self, neighborPosition, searchNodes):
        neighborNode = Node(neighborPosition)
        if neighborNode in searchNodes:
            neighborNode = searchNodes[neighborNode]
        return neighborNode

    def __createNeighborNode(self, node, neighborPosition, maze):
        costToMoveToNeighbor = Navigator.cost(node.position, neighborPosition, maze)
        newCost = node.g + costToMoveToNeighbor
        return Node(neighborPosition, node.position, newCost)

    def __isNewPathBetterThanOld(self, newNode, neighborNode, searchNodes, endPosition):
        totalCostNew = self.__f(newNode.g, newNode.position, endPosition)
        totalCostNeighbor = self.__f(neighborNode.g, neighborNode.position, endPosition)
        logger.debug(f"totalCostNew < totalCostNeighbor: {totalCostNew} < {totalCostNeighbor}\nNew: {newNode}Neighbor: {neighborNode}")
        return totalCostNew < totalCostNeighbor

    def __f(self, costToNode, currentPosition, endPosition):
        return costToNode + self.h(currentPosition, endPosition)

    def __addNodeToSearch(self, searchNodes, costPQ, node, endPosition):
        searchNodes[node] = node
        f = self.__f(node.g, node.position, endPosition)
        self.__heapPush(costPQ, node, f)
        
    def __removeNodeFromSearch(self, searchNodes, costPQ, node):
        del searchNodes[node]
        costPQ.remove(node) 

    def __convertSetToDictionary(self, nodeSet):
        setDictionary = {}
        for node in nodeSet:
            setDictionary[node.position] = node
        return setDictionary
    
    # Heap Helper Functions
        
    def __heapPush(self, costPQ, node, priority):
        heapq.heappush(costPQ, (priority, node))
    
    def __heapPop(self, costPQ):
        return heapq.heappop(costPQ)[1]
        
        
        
        
        
        