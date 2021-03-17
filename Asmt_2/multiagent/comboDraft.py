# listA = ['1', '2', '3']
# listB = ['A', 'B']
# listC = ['!', '@', '#', '$']
# listList = [listA, listB, listC]

# import itertools
# final = list(itertools.product(*listList))
# for c in final:
#     print(c)
# print(3 * 2 * 4)
# print(str(len(final)))

# l = [ (2,'a'), (1,'b'), (3,'c')]
# l.sort()
# print(l)

# l = [1]
# if l:
#     print('not empty')
# else:
#     print('empty')

print(type(1))
print(type(1.))

# def getAction(self, gameState):
#     """
#     Returns the expectimax action using self.depth and self.evaluationFunction

#     All ghosts should be modeled as choosing uniformly at random from their
#     legal moves.
#     """
#     "*** YOUR CODE HERE ***"
#     # util.raiseNotDefined()
#     self.minimaxRunCount = 0
#     numAgents = gameState.getNumAgents()
#     print('------------------------------------------')
#     print('numAgents ' + str(numAgents))
#     self.actions = []
#     self.expectimax(gameState, self.depth, 0, numAgents)
#     print('list: ' + str(self.actions))
#     self.actions.sort(reverse=True)
#     print('getAction: returning ' + str(self.actions[0]))
#     return self.actions[0][1]

# def expectimax(self, currentState : GameState, depth, agentIndex, numAgents) -> float:
#     print('Minimax: count: ' + str(self.minimaxRunCount) +
#           ' agentIndex: ' + str(agentIndex) +
#           ' depth:' + str(depth))
#     self.minimaxRunCount += 1

#     newDepth = depth
#     #if last agent, next is a new depth
#     if agentIndex == numAgents - 1:
#         newDepth -= 1

#     #base cases
#     if depth == 0 or currentState.isWin() or currentState.isLose():
#         val = self.evaluationFunction(currentState)
#         print('terminal: returning ' + str(val) + ' : ' + str(type(val)))
#         return val

#     if agentIndex == 0:
#         # if pacman, maximize score
#         val = float('-inf')
#         actions = currentState.getLegalActions(agentIndex)
#         for a in actions:
#             newState = currentState.generateSuccessor(agentIndex, a)
#             newAgentIndex = (agentIndex + 1 ) % numAgents
#             retVal = self.expectimax(newState, newDepth, newAgentIndex, numAgents)
#             print('recieved: ' + str(retVal) + ' : ' + str(type(retVal)))
#             print('val:' + str(val))
#             val = max(val, retVal)
#             #if root node, save actions and returned scores
#             if depth == self.depth:
#                 self.actions.append( (retVal, a) )
#                 print('action: ' + a)
#     else:
#         # if ghost, minimize score
#         val = float(0)
#         retVal = val
#         actions = currentState.getLegalActions(agentIndex)
#         for a in actions:
#             p = 1.0 /( numAgents - 1)
#             # print('p: ' + str(p))
#             newState = currentState.generateSuccessor(agentIndex, a)
#             newAgentIndex = (agentIndex + 1 ) % numAgents
#             retVal += p * self.expectimax(newState, newDepth, newAgentIndex, numAgents)
#         # print('expVal: ' + str(val))
#     return val