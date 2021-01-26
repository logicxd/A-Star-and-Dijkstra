from astar.AStar import AStar
from astar.HeuristicFunctions import manhattan as heuristicFunction
from my_logger import astar_logger as logger

# import logging
# logger.setLevel(logging.DEBUG)  

maze = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [6, 1, 1, 1, 1]]
startPosition = (0,2)
endPosition = (4,4)

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
logger.info(f"{shortestPath}")