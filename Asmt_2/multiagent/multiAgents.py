# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions, Game
import random, util
from game import Agent

#added
from pacman import GameState
import itertools

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        #more
        newNumFood = successorGameState.getNumFood()

        #info from current state
        ghostPos = currentGameState.getGhostPositions()
        capsulePos = currentGameState.getCapsules()
        walls = currentGameState.getWalls()
        numFood = currentGameState.getNumFood()
        curPos = currentGameState.getPacmanPosition()

        #prep
        foodList = self.grid2List(currentGameState.getFood())
        #print(str(len(foodList)))

        #add 1 if new eats a food
        #go towards nearest food unless 1 move from a ghost
        score = 0

        #figure out if moving away from nearest ghost
        curDistGhost = self.findClosest(curPos,ghostPos)[0]
        newDistGhost = self.findClosest(newPos,ghostPos)[0]
        deltaDistGhost = newDistGhost - curDistGhost
        #print("Ghost delta: " + str(deltaDistGhost))

        # #figure out if moving towards nearest food
        distFood, closestFoodPos = self.findClosest(curPos, foodList)
        newDistFood = self.dist(newPos,closestFoodPos)
        deltaDistFood = distFood - newDistFood
        # print("Food current dist:" +  str(distFood))
        # print("Food new dist:" +  str(newDistFood))
        # print("Food delta:" +  str(deltaDistFood))

        #score = deltaDistGhost * successorGameState.getScore()
        if newDistGhost > 2:
            score = successorGameState.getScore()
        else:
            score = deltaDistGhost
        #if self.isOneAwayFromGhost(newPos, ghostPos):
            #score = -1
            #score += (1/(newNumFood + 1)) + (1/(self.findClosestDistance(newPos,ghostPos) + 1))
        #else:
        #    score = -1

        #return successorGameState.getScore()
        return score

    def dist(self, a, b):
        return ( (a[0] - b[0])**2 + (a[1] - b[1]) ** 2 ) ** 0.5

    #return true if pacman position is one move away from a ghost
    #ghostPos is a list of tuples
    def isOneAwayFromGhost(self, pacmanPos, ghostPos):
        for g in ghostPos:
            dist = self.dist(pacmanPos, g)
            if dist <= (2 ** 0.5):
                print("* One Away: " + str(dist))
                return True
        return False

    #returns distance to closest pos in list and pos in a tuple
    def findClosest(self, pacmanPos, listOfPos):
        if len(listOfPos) == 0:
            print("ERROR")
            return 0.01
        mini = listOfPos[0]
        minDist = self.dist(pacmanPos, listOfPos[0])
        if len(listOfPos) > 1:
            for c in listOfPos[1:]:
                dist = self.dist(pacmanPos,c)
                if dist < minDist:
                    mini = c
                    minDist = dist
        ret =  (minDist, mini)
        #print("findClosest: " + str(ret))
        return ret

    #returns list of the position tuples that are true
    def grid2List(self, grid):
        grid = grid.asList()
        return [ (col, row) for col in range(len(grid)) for row in range(len(grid[col])) if grid[col][row] ]


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        # self.minimaxRunCount = 0
        numAgents = gameState.getNumAgents()
        # print('------------------------------------------')
        # print('numAgents ' + str(numAgents))
        self.actions = []
        self.minimax(gameState, self.depth, 0, numAgents)
        # print('list: ' + str(self.actions))
        self.actions.sort(reverse=True)
        # print('getAction: returning ' + str(self.actions[0]))
        return self.actions[0][1]

    # minimax algo for specified depth and starting state
    # returns float score
    def minimax(self, currentState : GameState, depth, agentIndex, numAgents) -> float:
        # print('Minimax: count: ' + str(self.minimaxRunCount) +
        #       ' agentIndex: ' + str(agentIndex) +
        #       ' depth:' + str(depth))
        # self.minimaxRunCount += 1

        newDepth = depth
        #if last agent, next is a new depth
        if agentIndex == numAgents - 1:
            newDepth -= 1

        #base cases
        if depth == 0 or currentState.isWin() or currentState.isLose():
            val = self.evaluationFunction(currentState)
            # print('terminal: returning ' + str(val))
            return val

        if agentIndex == 0:
            # if pacman, maximize score
            val = float('-inf')
            actions = currentState.getLegalActions(agentIndex)
            for a in actions:
                newState = currentState.generateSuccessor(agentIndex, a)
                newAgentIndex = (agentIndex + 1 ) % numAgents
                retVal = self.minimax(newState, newDepth, newAgentIndex, numAgents)
                # print('recieved: ' + str(retVal))
                # print('val:' + str(val))
                val = max(val, retVal)
                #if root node, save actions and returned scores
                if depth == self.depth:
                    self.actions.append( (retVal, a) )
                    #print('action: ' + a)
        else:
            # if ghost, minimize score
            val = float('inf')
            actions = currentState.getLegalActions(agentIndex)
            for a in actions:
                newState = currentState.generateSuccessor(agentIndex, a)
                newAgentIndex = (agentIndex + 1 ) % numAgents
                retVal = self.minimax(newState, newDepth, newAgentIndex, numAgents)
                val = min(val, retVal)
        return val

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
