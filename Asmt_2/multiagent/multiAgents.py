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
        # newFood = successorGameState.getFood()
        # newGhostStates = successorGameState.getGhostStates()
        # newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"
        #more
        # newNumFood = successorGameState.getNumFood()

        #info from current state
        ghostPos = currentGameState.getGhostPositions()
        # capsulePos = currentGameState.getCapsules()
        # walls = currentGameState.getWalls()
        # numFood = currentGameState.getNumFood()
        curPos = currentGameState.getPacmanPosition()

        #prep

        #figure out if moving away from nearest ghost
        curDistGhost = self.findClosest(curPos,ghostPos)[0]
        newDistGhost = self.findClosest(newPos,ghostPos)[0]
        deltaDistGhost = newDistGhost - curDistGhost
        #print("Ghost delta: " + str(deltaDistGhost))

        # #figure out if moving towards nearest food
        foodList = currentGameState.getFood().asList()
        distFood, closestFoodPos = self.findClosest(curPos, foodList)
        newDistFood = self.dist(newPos,closestFoodPos)
        deltaDistFood = distFood - newDistFood
        # print('curPos: ' + str(curPos) )
        # print('newPos: ' + str(newPos) )
        # print('closestFoodPos: ' + str(closestFoodPos))
        # print('distFood: ' + str(distFood))
        # print('newDistFood: ' + str(newDistFood))
        # print('deltaDistFood: ' + str(deltaDistFood))
        # print('----------------------')

        if newDistGhost > 2:
            # score = successorGameState.getScore()
            score = deltaDistFood
        else:
            score = deltaDistGhost
        #if self.isOneAwayFromGhost(newPos, ghostPos):
            #score = -1
            #score += (1/(newNumFood + 1)) + (1/(self.findClosestDistance(newPos,ghostPos) + 1))
        #else:
        #    score = -1

        #return successorGameState.getScore()
        return score

    @staticmethod
    def dist( a, b):
        return ( (a[0] - b[0])**2 + (a[1] - b[1]) ** 2 ) ** 0.5

    #returns distance to closest pos in list and pos in a tuple
    @staticmethod
    def findClosest(pacmanPos, listOfPos) -> tuple:
        if len(listOfPos) == 0:
            print("ERROR")
            return (0,(-1,-1))
        mini = listOfPos[0]
        minDist = ReflexAgent.dist(pacmanPos, listOfPos[0])
        if len(listOfPos) > 1:
            for c in listOfPos[1:]:
                dist = ReflexAgent.dist(pacmanPos,c)
                if dist < minDist:
                    mini = c
                    minDist = dist
        ret =  (minDist, mini)
        #print("findClosest: " + str(ret))
        return ret

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
        self.algorithm = 'none'
        self.actions = []

    def agentType(self, agentIndex):
        if agentIndex == 0:
            return 'max'
        if self.algorithm == 'minimax':
            return 'min'
        return 'chance'

    def helper(self, currentState : GameState, depth, agentIndex):
        numAgents = currentState.getNumAgents()
        newDepth = depth
        #if last agent, next is a new depth
        if agentIndex == numAgents - 1:
            newDepth -= 1
        #increment agentIndex
        newAgentIndex = (agentIndex + 1 ) % numAgents
        return (newDepth, newAgentIndex)

    def value(self, currentState : GameState, depth, agentIndex) -> float:
        nextData = self.helper(currentState, depth, agentIndex)
        #base cases
        if depth == 0 or currentState.isWin() or currentState.isLose():
            val = self.evaluationFunction(currentState)
            return val

        if self.agentType(agentIndex) == 'max':
            val = self.maxValue(currentState, depth, agentIndex, nextData)
        elif self.agentType(agentIndex) == 'min':
            val = self.minValue(currentState, depth, agentIndex, nextData)
        else: # chance
            val = self.expValue(currentState, depth, agentIndex, nextData)

        return val

    def maxValue(self, currentState : GameState, depth, agentIndex, nextData) -> float:
        newDepth, newAgentIndex = nextData
        val = float('-inf')
        actions = currentState.getLegalActions(agentIndex)
        for a in actions:
            newState = currentState.generateSuccessor(agentIndex, a)
            retVal = self.value(newState, newDepth, newAgentIndex)
            val = max(val, retVal)
            #save actions and scores if root
            if depth == self.depth:
                self.actions.append( (retVal, a) )
        return val

    def minValue(self, currentState : GameState, depth, agentIndex, nextData) -> float:
        newDepth, newAgentIndex = nextData
        val = float('inf')
        actions = currentState.getLegalActions(agentIndex)
        for a in actions:
            newState = currentState.generateSuccessor(agentIndex, a)
            retVal = self.value(newState, newDepth, newAgentIndex)
            val = min(val, retVal)
        return val

    def expValue(self, currentState : GameState, depth, agentIndex, nextData) -> float:
        newDepth, newAgentIndex = nextData
        val = float(0)
        actions = currentState.getLegalActions(agentIndex)
        for a in actions:
            p = 1.0 /( currentState.getNumAgents() - 1)
            newState = currentState.generateSuccessor(agentIndex, a)
            retVal = self.value(newState, newDepth, newAgentIndex)
            val += p * retVal
        return val

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
        self.algorithm = 'minimax'
        # self.minimaxRunCount = 0
        # print('------------------------------------------')
        self.actions = []
        self.value(gameState, self.depth, 0)
        # print('list: ' + str(self.actions))
        self.actions.sort(reverse=True)
        # print('getAction: returning ' + str(self.actions[0]))
        return self.actions[0][1]
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
    i = 0
    def getAction(self, gameState : GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        self.algorithm = 'expectimax'
        self.actions = []
        self.value(gameState, self.depth, 0)
        self.actions.sort(reverse=True)
        ret = self.actions[0][1]
        # print(str(self.i) + ' ret: ' + ret)
        self.i += 1
        return ret

def betterEvaluationFunction(currentGameState:GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    # DESCRIPTION:
    Give inf and -inf scores if win or lose. After that, I wanted
    to choose a number of variables that I could multiply by weights and sum
    to get a score that works better than the normal score. I thought it would
    be cool to be able to play with the weights to find an optimal set of weights.

    ## Variables:
    ### Food: The food left uneaten and the distance to the nearest food should
        both decrease the score. This encourages eating more food and getting closer to
        the nearest food.

    ### Capsules: We want to subtract the number of capsules left uneaten from the score
        so that Pacman will eat one if he gets a chance. I did not include a variable relating
        the distance to the closest capsule so that Pacman wasn't constantly trying to chase them.

    ### Ghosts: I make lists of the scared ghosts and the active ghosts by checking their scaredTimer fields.
        We want to minimize the distance to the closest scared ghost, so the larger the distance,
        the more is subtracted from the score.

        The closer the closest ghost is, the lower the score should be. So we want to subtract the most
        when the distance is smallest. The reciprocal of the distance is used for this.
        Pacman wants to widen the distance to minimize the amount subtracted from the score.

        With these two relations to ghosts, Pacman will be pulled towards scared ghosts,
        but pushed away from active ghosts.


    """
    if currentGameState.isWin():
        return float('inf')
    if currentGameState.isLose():
        return float('-inf')

    curPos = currentGameState.getPacmanPosition()

    # number of food left MIN
    foodList = currentGameState.getFood().asList()
    foodLeft = len(foodList)
    # dist to closest food MIN
    distFood, closestFoodPos = ReflexAgent.findClosest(curPos, foodList)

    # divide ghosts into active and scared lists
    ghostStates = currentGameState.getGhostStates()
    activeGhosts = []
    scaredGhosts = []
    for g in ghostStates:
        if g.scaredTimer > 0:
            scaredGhosts.append(g.configuration.pos)
        else:
            activeGhosts.append(g.configuration.pos)

    #
    w = 1
    # get distance to closest active ghost
    if activeGhosts:
        distActiveGhost, closeActiveGhostPos = ReflexAgent.findClosest(curPos,activeGhosts)
        if distActiveGhost < 3:
            w = 3 #give extra weight that is used to ramp up danger when within a certain range
    else:
        #make infinite so that reciprocal = 0, and doesn't affect the score, when there are no active ghosts
        distActiveGhost = float('inf')

    #dist to closest scared ghost
    if scaredGhosts:
        distScaredGhost, closeScaredGhostPos = ReflexAgent.findClosest(curPos,scaredGhosts)
    else:
        # have no affect on score if there are no scared ghosts
        distScaredGhost = 0

    #capsules
    capsulesLeft = len(currentGameState.getCapsules())

    score =   1   * currentGameState.getScore()
    score += -2   * foodLeft
    score += -1   * distFood
    score += -2   * (1.0/distActiveGhost) * w
    score += -2   * distScaredGhost
    score += -20   * capsulesLeft

    return score

# Abbreviation
better = betterEvaluationFunction
