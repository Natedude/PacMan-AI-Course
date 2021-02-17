# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

#from game import Directions
import util
#from searchAgents import PositionSearchProblem
from game import Directions
s = Directions.SOUTH
w = Directions.WEST
n = Directions.NORTH
e = Directions.EAST
stop = Directions.STOP

import pprint

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    #util.raiseNotDefined()
    """
    "*** YOUR CODE HERE ***"

    frontier = util.Stack()
    s = Search(problem, frontier)
    return s.search()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    s = Search(problem, frontier)
    return s.search()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

class Search:

    def __init__(self, problem, frontier) -> None:
        self.problem = problem
        self.frontier = frontier

        print("Start:", problem.getStartState())
        self.start = problem.getStartState()
        frontier.push(self.start)

        # dict[(x,y)] = ( parent (x,y) when discovered, action used to discover)
        self.discoveryMap = {}
        # list of nodes visited
        self.explored = []

    def pop(self):
        return self.frontier.pop()

    def push(self, item, num = None):
        if num == None:
            self.frontier.push(item)
        else:
            self.frontier.push(item, num)

    def search(self):
        while not self.frontier.isEmpty():
            currentState = self.frontier.pop()
            print("Popped: " + str(currentState) + " " + str(type(currentState)))

            # check is already explored
            if currentState in self.explored:
                print()
                continue
            self.explored.append(currentState)

            #check if goal
            if self.problem.isGoalState(currentState):
                print("GOAL FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!! :-) ")
                print("####################################\n")
                #pprint.pprint(self.discoveryMap)
                return self.path(currentState)

            successors = self.problem.getSuccessors(currentState)
            print("Successors: ")
            #print(successors)
            #print()
            for suc in successors:
                pos, action, cost = suc
                if pos not in self.discoveryMap.keys():
                    self.discoveryMap[pos] = (currentState, action)
                    #print suc added to disc
                    print(str(pos) + " added to discoveryMap with values:\n (" +
                        str(currentState) + ", " + str(action) + ")")
                    self.frontier.push(pos)
                else:
                    print(str(pos) + " NOT ADDED - already in discoveryMap")
            print()

        print("No goal found :-(")
        print("####################################")
        return stop

    def explore(self):
        pass

    def path(self, pos):
        p = []
        while pos != self.start:
            parent, action = self.discoveryMap[pos]
            p.insert(0, action)
            pos = parent
        print("Path: \n" + str(p) + "\n")
        return p