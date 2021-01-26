# A Star and Dijkstra

Easy to modify A* (and Dijkstra) implementation in Python3.

## How to Run It

```python
from astar.AStar import AStar
from astar.HeuristicFunctions import manhattan as heuristicFunction

maze = [[1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1]]
startPosition = (0,0)
endPosition = (4,4)

# Dijkstra
dijkstra = AStar()
searchMap = dijkstra.findPath(maze, startPosition, endPosition)
shortestPath = dijkstra.pathToNode(searchMap, endPosition)

# Astar
astar = AStar(heuristicFunction)
searchMap = astar.findPath(maze, startPosition, endPosition)
shortestPath = astar.pathToNode(searchMap, endPosition)
```

## Running Tests 

Run all tests
```bash
# inside the main/ directory
python run_tests.py
```

Run individual tests
```bash
# inside the main/ directory
python test_astar1.py
```

You can also add your own tests by creating new files similar to existing test files. They will automatically be picked up by `run_tests.py`.

## Logs

Level of information to output is inside `my_logger.py`. See the methods `setupAStarLogger()` and `setupTestLogger()`. The level of information is defined as follow:
* logging.WARNING - no outputs configured
* logging.INFO - some finished product outputs
* logging.DEBUG - all outputs

Comment/uncomment as needed to switch logging level. 
