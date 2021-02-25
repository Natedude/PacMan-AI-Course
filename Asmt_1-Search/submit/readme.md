# Nathan Hildum = 918 340 844

## ~ Hours spent:
10-16

## ~ Description:

### q1-4:
    *Search class* designed to make searching modular and remove implementation details from the dfs, bfs, ucs, and A* functions.

    The *main difference* between different search algorithms is what type of list with push/pop functionality is used for the frontier of the search tree. *Other differences* include:
        - A boolean,'isUCS', so search knows whether to include a priority numeral when pushing a node to the frontier data structure.
        - The option of passing in a heuristic function.

    Before exploring a node, search pops a it from the frontier, checks if it has been explored, checks if it is a goal. If it is a goal, it returns the path. Paths/action-lists, are tracked by adding a successor's action to the parent node's path as it is pushed onto the frontier.

### q5-6
    CornersProblem uses a state representation of the form
        (x-y-position, [list of corners visited])

    getSuccessors() returns states so that when a corner is visited, it is included in the state representation. This way Pacman won't just repeatedly hit the same corner.

    cornerHeuristic() takes the Manhattan Distance between the current Pacman position and each corner. It sums them together. The sum / 2 is returned so the estimated cost is always less than the optimal path. Also this ensures a move that costs 1 can never change the heuristic by more than 1.

### q7
    foodHeuristic simply returns the number of food positions currently left. This gives 'lower' priority to any move that removes food from the grid.

### q8
    AnyFoodSearchProblem's isGoalState() method returns if it is true that a (x,y) position in the grid has food. findPathToClosestDot() uses a breadth-first-search with an instance of AnyFoodSearchProblem to find the closest dot. BFS is used because it will search radiating from the position.