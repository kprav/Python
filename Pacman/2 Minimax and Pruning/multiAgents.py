from util import manhattanDistance
from game import Directions
import random, util
import pdb

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
    some Directions.X for some X in the set {North, South, West, East, Stop}
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
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.
    
    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)		# get the successor game state
    newPos = successorGameState.getPacmanPosition()					# get the next position of the pacman
    oldFood = currentGameState.getFood()						# get the current food grid
    newGhostStates = successorGameState.getGhostStates() 				# get the states of the ghosts
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]		# get the scared times of the ghosts
    newGhostPoss = successorGameState.getGhostPositions()      				# get the next position of all the ghosts
    i = newPos[0]
    j = newPos[1]    
    for newGhostPos in newGhostPoss:							# for each of the ghosts, check if they are
      if newPos[0] == newGhostPos[0] and newPos[1] == newGhostPos[1]+1:			# in any of the four possible next position 	
	return -99999									# of the pacman. if yes return a very high
      elif newPos[0] == newGhostPos[0] and newPos[1] == newGhostPos[1]-1:		# negative integer. Otherwise return the score	
	return -99999		 							# of the successor state
      elif newPos[0] == newGhostPos[0]+1 and newPos[1] == newGhostPos[1]:
	return -99999
      elif newPos[0] == newGhostPos[0]-1 and newPos[1] == newGhostPos[1]:
	return -99999
      else:       
        return successorGameState.getScore()
                
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
  depth = 0  												# initially the depth of the tree is zero
  keepTrac = {}												# dictionary to keeptrack of utility values & actions
  numGhosts = 0												# initially number of ghosts is set to zero 
  def getAction(self, gameState):									# The getaction function for the minimax algorithm
    """
      Returns the minimax action from the current gameState using self.depth 
      and self.evaluationFunction.
      
      Here are some method calls that might be useful when implementing minimax.
      
      gameState.getLegalActions(agentIndex):  
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1
      
      Directions.STOP:
        The stop direction, which is always legal
      
      gameState.generateSuccessor(agentIndex, action): 
        Returns the successor game state after an agent takes an action
      
      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    MinimaxAgent.depth = self.depth    									# obtain the depth passed at command line
    MinimaxAgent.keepTrac = {}										# the dictionary is initially empty
    MinimaxAgent.numGhosts = gameState.getNumAgents() - 1 						# get the number of ghosts
    v = self.MaxValue(gameState, MinimaxAgent.depth)   							# call the maxvalue function to maximize pacman's value
    legalAction = MinimaxAgent.keepTrac[v]       							# obtain the action for the utility value returned
    return legalAction											# return the legal action
    util.raiseNotDefined()
    
  def MinvValue(self, a, b):										# function to find the lower of two numbers
    if a > b:
      return b
    elif b > a:
      return a
    elif a == b:
      return a
      
  def MaxvValue(self, a, b):										# function to find the higher of two number
    if a > b:
      return a
    elif b > a:
      return b
    elif a == b:
      return a
  
  def MaxValue(self, gameState, depth):									# the max value function
    agentIndex = 0											# agent index for pacman is zero
    legalMoves = gameState.getLegalActions(agentIndex)    						# get the legal moves for the pacman
    if Directions.STOP in legalMoves: legalMoves.remove('Stop')						# remove the stop from the list of actions
    ghosts = gameState.getNumAgents() - 1    								# obtain the number of ghosts
    v = float('-inf')    										# initialize v to minus infinity
    if depth == 0:      										# if depth is zero return the value of the evaluation function
      v = self.evaluationFunction(gameState)      
      return v           
    successors = [(gameState.generateSuccessor(agentIndex, move), move) for move in legalMoves]		# get the successors for each action of the pacman
    for successor, move in successors:                    						# run a loop to check for every successor
      dummyV = self.MinValue(successor, 1, depth)      							# call the min value function for each successor
      v = self.MaxvValue(v, dummyV)									# get the highest out of all the utility values
      if depth == self.depth:										# if current depth is the depth of the game, update the dictionary of utility values and moves	
        tempDict = {dummyV:move}
        MinimaxAgent.keepTrac.update(tempDict)
    return v  												# return the max value of the pacman
  
  def MinValue(self, gameState, agentIndex, depth):							# the min value function
    if depth == 0:											# if depth is zero return the value of the evaluation function
      v = self.evaluationFunction(gameState)
      return v
    if agentIndex < MinimaxAgent.numGhosts:								# if the current ghost is not the last ghost
      legalMoves = gameState.getLegalActions(agentIndex)						# get the ghosts legal moves
      successors = [(gameState.generateSuccessor(agentIndex, move), move) for move in legalMoves]	# get the successors for all the legal moves
      if len(successors) == 0:										# if it has no successor, then return the value of the evaluation function
        v = self.evaluationFunction(gameState)
        return v
      v = float('inf')											# set v to plus infinity
      for successor, move in successors:								# run a loop to check for every successor
        dummyV = self.MinValue(successor, agentIndex + 1 , depth)					# call the min value function for each successor
        v = self.MinvValue(v, dummyV)									# get the least of all the utility values and return it
      return v
    else:												# the current ghost is the last ghost
      if depth > 0:											# the depth is greater than zero
        depth = depth - 1										# decrement the depth
        legalMoves = gameState.getLegalActions(agentIndex)						# get the legal moves for the ghost
        successors = [(gameState.generateSuccessor(agentIndex, move), move) for move in legalMoves]	# get the successors for all the legal moves
        if len(successors) == 0:									# if it has no successor, then return the value of the evaluation function
          v = self.evaluationFunction(gameState)
          return v
        v = float('inf')										# set v to plus infinity
        for successor, move in successors:								# run a loop to check for each successor
          dummyV = self.MaxValue(successor, depth)							# call the max value function for each successor
          v = self.MinvValue(v, dummyV)									# get the least out of all the utility values and return it	
        return v     
      
class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """
    
  def getAction(self, gameState):									# the getaction function for the alpha-beta pruning algorithm
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    MinimaxAgent.depth = self.depth    
    MinimaxAgent.keepTrac = {}
    MinimaxAgent.numGhosts = gameState.getNumAgents() - 1 
    alpha = float('-inf')										# set alpha to minus infinity
    beta = float('inf')											# set beta to plus infinity
    v = self.MaxValue(gameState, MinimaxAgent.depth, alpha, beta)   
    legalAction = MinimaxAgent.keepTrac[v]        
    return legalAction
    util.raiseNotDefined()
    
  def MinvValue(self, a, b):
    if a > b:
      return b
    elif b > a:
      return a
    elif a == b:
      return a
      
  def MaxvValue(self, a, b):
    if a > b:
      return a
    elif b > a:
      return b
    elif a == b:
      return a  

  def MaxValue(self, gameState, depth, alpha, beta):
    agentIndex = 0
    legalMoves = gameState.getLegalActions(agentIndex)    
    if Directions.STOP in legalMoves: legalMoves.remove('Stop')
    ghosts = gameState.getNumAgents() - 1    
    v = float('-inf')    
    if depth == 0:      
      v = self.evaluationFunction(gameState)      
      return v           
    successors = [(gameState.generateSuccessor(agentIndex, move), move) for move in legalMoves]
    for successor, move in successors:                    
      dummyV = self.MinValue(successor, 1, depth, alpha, beta)      
      v = self.MaxvValue(v, dummyV)
      if v >= beta:											# if the utility value is greater than beta, return it
        return v
      alpha = self.MaxvValue(alpha, v)
      if depth == self.depth:
        tempDict = {dummyV:move}
        MinimaxAgent.keepTrac.update(tempDict)    
    return v  
  
  def MinValue(self, gameState, agentIndex, depth, alpha, beta):
    if depth == 0:
      v = self.evaluationFunction(gameState)
      return v
    if agentIndex < MinimaxAgent.numGhosts:
      legalMoves = gameState.getLegalActions(agentIndex)
      successors = [(gameState.generateSuccessor(agentIndex, move), move) for move in legalMoves]
      if len(successors) == 0:
        v = self.evaluationFunction(gameState)
        return v
      v = float('inf')
      for successor, move in successors:
        dummyV = self.MinValue(successor, agentIndex + 1 , depth, alpha, beta)
        v = self.MinvValue(v, dummyV)
        if v <= alpha:											# if the utlity value is less than alpha, return it
          return v
        beta = self.MinvValue(beta, v)									# update beta	
      return v
    else:
      if depth > 0:
        depth = depth - 1
        legalMoves = gameState.getLegalActions(agentIndex)
        successors = [(gameState.generateSuccessor(agentIndex, move), move) for move in legalMoves]
        if len(successors) == 0:
          v = self.evaluationFunction(gameState)
          return v
        v = float('inf')
        for successor, move in successors:
          dummyV = self.MaxValue(successor, depth, alpha, beta)
          v = self.MinvValue(v, dummyV)
          if v <= alpha:										# if the utlity value is less than alpha, return it
            return v
          beta = self.MinvValue(beta, v)								# update beta
        return v				
        
        
#You can stop here, the following two questions are not released for this session. 

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

