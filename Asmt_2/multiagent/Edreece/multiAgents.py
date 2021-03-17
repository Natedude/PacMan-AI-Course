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
from game import Directions
import random, util
import math

from game import Agent

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
		score = successorGameState.getScore()

		# We need to find the distance of all the ghosts and insert it into a list using Manhattan
		ghostDistance = []
		for g in newGhostStates:
			ghostDistance.append(manhattanDistance(newPos, g.getPosition()))

		# Now we can insert all the food in the list
		foodList = newFood.asList()

		# Find the distance of all the food and insert it into a list just like above
		foodDistance = []
		for f in foodList:
			foodDistance.append(manhattanDistance(newPos, f))

		# Check to see if there's at least one ghost
		if len(newGhostStates) is not 0:
			score += (min(ghostDistance))

		# Check to see if there's at least one food
		if len(foodDistance) is not 0:
			score -= (min(foodDistance))

		# Return score
		return score

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
		def minimax(state, depth, agent):

			# If we find the bottom nodes or if we don't have any moves or we won/lost: Call the evaluation function and return the result
			if depth == self.depth or state.getLegalActions(agent) == 0 or state.isWin() or state.isLose():
				return (self.evaluationFunction(state), None)

			minfinity = float("-inf")
			value = minfinity
			# If our agent is pacman
			if (agent is 0):
				for a in state.getLegalActions(agent):
					(value1, agent1) = minimax(state.generateSuccessor(agent, a), depth, (agent + 1) % state.getNumAgents())
					#Find the maximum value
					if(value1 > value):
						value = value1
						maxOfa = a
			# Return the value and the action from which we found max
			if value is not minfinity:
				return (value, maxOfa)

			infinity = float("inf")
			value = infinity
			# If our agent is ghost
			if (agent is not 0):
				for a in state.getLegalActions(agent):
					# If it isn't the last ghost keep the same depth
					if(((agent + 1) % state.getNumAgents()) is not 0):
						(value1, agent1) = minimax(state.generateSuccessor(agent, a), depth, (agent + 1) % state.getNumAgents())
					# else if it is next_depth = depth + 1
					else:
						(value1, agent1) = minimax(state.generateSuccessor(agent, a), depth + 1, (agent + 1) % state.getNumAgents())
					# Find the minimum value
					if(value1 < value):
						value = value1
						minOfa = a
			# Return the value and the action from which we found min
			if value is not infinity:
				return (value, minOfa)

		return minimax(gameState, 0, 0)[1]

class AlphaBetaAgent(MultiAgentSearchAgent):
	"""
	Your minimax agent with alpha-beta pruning (question 3)
	"""

	def getAction(self, gameState):
		"""
		Returns the minimax action using self.depth and self.evaluationFunction
		"""
		"*** YOUR CODE HERE ***"
		def alpha_beta(state, depth, agent, A, B):

			# If we find the bottom nodes or if we don't have any moves or we won/lost: Call evaluation function and return the result
			if depth == self.depth or state.getLegalActions(agent) == 0 or state.isWin() or state.isLose():
				return (self.evaluationFunction(state), None)

			minfinity = float("-inf")
			value = minfinity
			# If our agent is pacman
			if (agent is 0):
				for a in state.getLegalActions(agent):
					(value1, agent1) = alpha_beta(state.generateSuccessor(agent, a), depth, (agent + 1) % state.getNumAgents(), A, B)

					# Find the maximum value
					if(value1 > value):
						value = value1
						maxOfa = a

					if value > B:
						return (value, maxOfa)
					A = max(A, value)

			# Return the value and the action from which we found max
			if value is not minfinity:
				return (value, maxOfa)

			infinity = float("inf")
			value = infinity
			# If agent is ghost
			if (agent is not 0):
				for a in state.getLegalActions(agent):
					# If it isn't the last ghost keep the same depth
					if(((agent + 1) % state.getNumAgents()) is not 0):
						(value1, agent1) = alpha_beta(state.generateSuccessor(agent, a), depth, (agent + 1) % state.getNumAgents(), A, B)
					# else if it is next_depth = depth + 1
					else:
						(value1, agent1) = alpha_beta(state.generateSuccessor(agent, a), depth + 1, (agent + 1) % state.getNumAgents(), A, B)

					# Find the minimum value
					if(value1 < value):
						value = value1
						minOfa = a

					if value < A:
						return (value, minOfa)
					B = min(B, value)

			# Return the value and the action from which we found min
			if value is not infinity:
				return (value, minOfa)
		return alpha_beta(gameState, 0, 0, float("-inf"), float("inf"))[1]

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
		def expectimax(state, depth, agent):

			# If we find the bottom nodes or if we don't have any moves or we won/lost: Call evaluation function and return the result
			if depth == self.depth or state.getLegalActions(agent) == 0 or state.isWin() or state.isLose():
				return (self.evaluationFunction(state), None)

			minfinity = float("-inf")
			value = minfinity
			# If our agent is pacman
			if (agent is 0):
				for a in state.getLegalActions(agent):
					(value1, agent1) = expectimax(state.generateSuccessor(agent, a), depth, (agent + 1) % state.getNumAgents())
					# Find the maximum value
					if(value1 > value):
						value = value1
						maxOfa = a
			# Return the value and the action from which we found max
			if value is not minfinity:
				return (value, maxOfa)

			infinity = float("inf")
			value = 0.0
			count = 0.0
			# If our agent is a ghost
			if (agent is not 0):
				for a in state.getLegalActions(agent):
					# If it isn't the last ghost keep the same depth
					if(((agent + 1) % state.getNumAgents()) is not 0):
						(value1, agent1) = expectimax(state.generateSuccessor(agent, a), depth, (agent + 1) % state.getNumAgents())
					# else if it is next_depth = depth + 1
					else:
						(value1, agent1) = expectimax(state.generateSuccessor(agent, a), depth + 1, (agent + 1) % state.getNumAgents())

					# Find the average of the values
					value += value1
					count += 1
					minOfa = a
			if value is not infinity:
				return (value/count, minOfa)

		return expectimax(gameState, 0, 0)[1]

def betterEvaluationFunction(currentGameState):
	"""
	Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
	evaluation function (question 5).

	DESCRIPTION: <write something here so we know what you did>
	"""
	"*** YOUR CODE HERE ***"
	newPos = currentGameState.getPacmanPosition()
	newFood = currentGameState.getFood()
	newGhostStates = currentGameState.getGhostStates()
	newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

	# Get the current score of the successor state
	score = currentGameState.getScore()

	ghostValue = 10.0
	foodValue = 10.0
	scaredGhostValue = 50.0

	# For every ghost
	for x in newGhostStates:
		# Find the distance from pacman
		manDistance = manhattanDistance(newPos, x.getPosition())
		if manDistance > 0:
			"""
			If the ghost is edible, and the ghost is near, the distance
			is small. In order to get a bigger score we divide the distance to a big number
			to get a higher score
			"""
			if x.scaredTimer > 0:
				score += scaredGhostValue / manDistance
			else:
				score -= ghostValue / manDistance
			"""
			If the ghost is not edible, and the ghost is far, the distance
			is big. We want to avoid such situation so we subtract the distance to a big number
			to lower the score and avoid this state.
			"""

	# Find the distance of every food and insert it in a list using manhattan
	foodList = newFood.asList()
	foodDistances = []
	"""
	If the food is very close to the pacman then the distance is small and
	we want such a situation to proceed. So we divide the distance to a big number
	to get a higher score
	"""
	for x in foodList:
		foodDistances.append(manhattanDistance(newPos, x))

	# If there is at least one food
	if len(foodDistances) is not 0:
		score += foodValue / min(foodDistances)

	# Return the final Score
	return score

	util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
