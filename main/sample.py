from astar.AStar import AStar
from astar.HeuristicFunctions import manhattan as heuristicFunction
from my_logger import astar_logger as logger
from enum import Enum

import logging
logger.setLevel(logging.INFO)  

class Traffic(Enum):
        NoTraffic = 0
        BayBridgeTraffic = 1
        SanMateoBridgeTraffic = 2
        NoToll = 3

maze = [[1, 3, 3, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 3, 3, 2, 1],
        [0, 1, 0, 1, 0],
        [0, 2, 2, 1, 0]]

traffic = Traffic.NoToll
if traffic == Traffic.BayBridgeTraffic:
        maze = [[1, 3, 6, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 3, 3, 2, 1],
                [0, 1, 0, 1, 0],
                [0, 2, 2, 1, 0]]
elif traffic == Traffic.SanMateoBridgeTraffic:
        maze = [[1, 3, 3, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 3, 9, 2, 1],
                [0, 1, 0, 1, 0],
                [0, 2, 2, 1, 0]]
elif traffic == Traffic.NoToll:
        maze = [[1, 3, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 3, 0, 2, 1],
                [0, 1, 0, 1, 0],
                [0, 2, 2, 1, 0]]

startPosition = (0,2)
endPosition = (4,2)

# Dijkstra
dijkstra = AStar()
searchMap = dijkstra.findPath(maze, startPosition, endPosition)
shortestPath = dijkstra.pathToNode(searchMap, endPosition)

# logger.info(f"{searchMap}")
logger.info(f"{shortestPath}")

# Astar
astar = AStar(heuristicFunction)
searchMap = astar.findPath(maze, startPosition, endPosition)
shortestPath = astar.pathToNode(searchMap, endPosition)

# logger.info(f"{searchMap}")
# logger.info(f"{shortestPath}")