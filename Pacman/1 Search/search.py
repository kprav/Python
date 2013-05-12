"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):						# Implements the DFS algorthims to navigate the pacman from start to goal
  """
  Search the deepest nodes in the search tree first [p 74].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
   
  from game import Directions						# import the four directions 
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  
  openQueue = util.Stack()						# open queue implemented as stack
  closedQueue = util.Queue()						# closed queue implemented as queue
  
  moves = []								# list that will contain the sequence of nodes to reach the goal node
  cost = 0
  check = 0
  i = 0
  dctnry = {}								# dictionary that maintains the parent of each node	
  
  parentStart = ()
  startState = problem.getStartState()
  startNode = (startState,'NoDir',0)					# Create a start Node in the standart 3 tuple format
  if not(problem.isGoalState(startState)):				# check if the start node is the goal node - it is not the goal
  	successors = problem.getSuccessors(startState)  		# get the successors of the start node
  	for successor in successors:					
  		openQueue.push(successor)  				# push the successors of the start node into the open queue
  		tempDict = {successor:startNode}
  		dctnry.update(tempDict)					# keep a dictionary of parents to keeptrack of a node's parent
  else:
  	print "Hurray!! Reached Goal : ",startState
  	return

  while not(openQueue.isEmpty()):  					# We have nodes in the open queue
  	oQPoppedSucc = openQueue.pop()    	  			# pop a node from the open queue
  	closedQueue.push(oQPoppedSucc)  				# push that node into the closed node
	succ = oQPoppedSucc[0]						# successor state
	action = oQPoppedSucc[1]					# action to reach the successor
	stepCost = oQPoppedSucc[2]  					# cost to reach the successor
	
	if problem.isGoalState(succ):					# check if the current state is goal state
		finalRoute = util.Stack()				# keep a stack that keeps track of the route to the goal node
		goalNode = oQPoppedSucc					
		tempNode = goalNode
		finalRoute.push(tempNode)				# push the goal node into the stack of routes
		while not(tempNode == startNode):			# backtrack in the dictionary of parents to find the route upto the start node
			tempNode = dctnry[tempNode]			
			finalRoute.push(tempNode)		
		while not(finalRoute.isEmpty()):			# pop nodes from the route stack until it is empty and update the moves to reach the goal
			node = finalRoute.pop()			
			action = node[1]
			cost = cost + node[2]
			if action == 'West':			
				moves.append(w)
			elif action == 'South':
				moves.append(s)
			elif action == 'North':
				moves.append(n)
			elif action == 'East':
				moves.append(e)	
  		return moves						# return the sequence of moves from the start node to the goal node
				
	else:								# the current node is not the goal node
		tempSucc = problem.getSuccessors(succ)			# get all the successors of the current node
		
		for tS in tempSucc:
			if (closedQueue.list.count(tS)==0 and openQueue.list.count(tS)==0):				
				check = 1				
			if check == 1:					# the successor is not in both the open queue and the closed queue	
				openQueue.push(tS)			# push the successor into the open queue
				tempDict = {tS:oQPoppedSucc}		
		  		dctnry.update(tempDict)			# update the dictionary of parents
				check = 0		
  util.raiseNotDefined()

def breadthFirstSearch(problem):					# implements the BFS algorithm to navigate the pacman from goal to destination
  "Search the shallowest nodes in the search tree first. [p 74]"
  "*** YOUR CODE HERE ***"
  """
  The implementation is very similar to DFS search. The only difference 
  is that the open queue is implemented as a queue as opposed to that of
  a stack in the case of DFS search
  """
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
   
  from game import Directions						
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  
  openQueue = util.Queue()						# open queue implemented as queue
  closedQueue = util.Queue()						# closed queue implemented as queue
  
  moves = []
  cost = 0
  check = 0
  i = 0
  dctnry = {}
  
  parentStart = ()
  startState = problem.getStartState()
  startNode = (startState,'NoDir',0)
  if not(problem.isGoalState(startState)):
  	successors = problem.getSuccessors(startState)  	
  	for successor in successors:
  		openQueue.push(successor)  		
  		tempDict = {successor:startNode}
  		dctnry.update(tempDict)
  else:
  	print "Hurray!! Reached Goal : ",startState
  	return

  while not(openQueue.isEmpty()):  	
  	oQPoppedSucc = openQueue.pop()    	  	
  	closedQueue.push(oQPoppedSucc)  		
	succ = oQPoppedSucc[0]
	action = oQPoppedSucc[1]
	stepCost = oQPoppedSucc[2]  		
	
	if problem.isGoalState(succ):		
		finalRoute = util.Stack()
		goalNode = oQPoppedSucc
		tempNode = goalNode
		finalRoute.push(tempNode)
		while not(tempNode == startNode):
			tempNode = dctnry[tempNode]
			finalRoute.push(tempNode)
		while not(finalRoute.isEmpty()):
			node = finalRoute.pop()			
			action = node[1]
			cost = cost + node[2]
			if action == 'West':
				moves.append(w)
			elif action == 'South':
				moves.append(s)
			elif action == 'North':
				moves.append(n)
			elif action == 'East':
				moves.append(e)	
  		return moves				
				
	else:	
		tempSucc = problem.getSuccessors(succ)
		
		for tS in tempSucc:
			if (closedQueue.list.count(tS)==0 and openQueue.list.count(tS)==0):				
				check = 1
			if check == 1:				
				openQueue.push(tS)
				tempDict = {tS:oQPoppedSucc}
		  		dctnry.update(tempDict)
				check = 0	

  util.raiseNotDefined()
      
def uniformCostSearch(problem):						# implements the UCS algorithm to navigate the pacman from source to goal
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  """
  The implementation is a litte different from BFS because the open
  queue is implemented as a priority queue as opposed to that of a
  queue in case of BFS. Here we use the cost to reach a particular 
  node as priority to push it into the open queue
  """
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
   
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  
  openQueue = util.PriorityQueue()					# priority queue implementation of open queue
  closedQueue = util.Queue()						# queue implementation of closed queue
  dummyQueue = util.Queue()						# maintain a queue of open queue nodes for simplicity and checking purposes
  
  moves = []
  cost = 0
  check = 0
  i = 0
  pCost = 0
  dctnry = {}
  costDict = {}								# dictionary that keeps track of the cost to reach a particular node from start
  
  parentStart = ()
  startState = problem.getStartState()
  startNode = (startState,'NoDir',0)
  if not(problem.isGoalState(startState)):
  	successors = problem.getSuccessors(startState)  	
  	for successor in successors:
  		pCost = successor[2]
  		openQueue.push(successor,pCost)  		
  		dummyQueue.push(successor)
  		tempDict = {successor:startNode}
  		tempDict2 = {successor:pCost}
  		costDict.update(tempDict2)
  		dctnry.update(tempDict)
  else:
  	print "Hurray!! Reached Goal : ",startState
  	return

  while not(openQueue.isEmpty()):  	
  	oQPoppedSucc = openQueue.pop()    	  	
  	closedQueue.push(oQPoppedSucc)  		
	succ = oQPoppedSucc[0]
	action = oQPoppedSucc[1]
	stepCost = oQPoppedSucc[2]  		
	
	if problem.isGoalState(succ):	
		print "Hurray!! Reached Goal : ",startState		
		finalRoute = util.Stack()
		goalNode = oQPoppedSucc
		tempNode = goalNode
		finalRoute.push(tempNode)
		while not(tempNode == startNode):
			tempNode = dctnry[tempNode]
			finalRoute.push(tempNode)
		while not(finalRoute.isEmpty()):
			node = finalRoute.pop()			
			action = node[1]
			cost = cost + node[2]
			if action == 'West':
				moves.append(w)
			elif action == 'South':
				moves.append(s)
			elif action == 'North':
				moves.append(n)
			elif action == 'East':
				moves.append(e)	
		return moves
				
	else:	
		tempSucc = problem.getSuccessors(succ)
		
		for tS in tempSucc:
			if tS[2]<0:					# check for negative cost of path	
				if not(closedQueue.list.count(tS)==0):	# check if the current node is already in the open queue
					pCost = costDict[oQPoppedSucc]
					pCost = pCost+tS[2]
					prevPCost = costDict[tS]
					if pCost<prevPCost:		# the current cost is lesser that what it was before
						tempDict = {tS:oQPoppedSucc}	
						tempDict2 = {tS:pCost}
						del costDict[tempDict2]	# delete the old cost entry from the dictionary of costs	
						del dctnry[tempDict]	# delete the old parent entry from the dictionary of parents
						dctnry.update(tempDict)	# update the cost and parent dictionary with new values
						costDict.update(tempDict2)					
			if (closedQueue.list.count(tS)==0 and dummyQueue.list.count(tS)==0):				
				check = 1				# the current node is not in both the open queue and closed queue
			if check == 1:
				pCost = costDict[oQPoppedSucc]		# find the cost upto the current node's parent
				pCost = pCost + tS[2]			# update the cost with the cost to reach the current node from its parent
				openQueue.push(tS,pCost)		# push the current node into the open queue using the cost as the priority
				dummyQueue.push(tS)			# push the current node into the dummyQueue also for checking purposes
				tempDict = {tS:oQPoppedSucc}		
				tempDict2 = {tS:pCost}
		  		costDict.update(tempDict2)		# update the cost dictionary
		  		dctnry.update(tempDict)			# update the parent dictionary
				check = 0
			elif not(dummyQueue.list.count(tS)==0):		# the current node is present in the open queue
				pCost = costDict[oQPoppedSucc]		# find the cost to reach its current parent
				pCost = pCost + tS[2]			# add the cost to reach the current node from the current node
				prevPCost = costDict[tS]		# find the cost to reach the current node via its older parent
				if pCost<prevPCost:			# the current cost is cheaper than the older cost
					dummyQueue.list.remove(tS)	# remove the old entry current node from the dummy queue
					openQueue.list.remove(tS)	# remove the old entry current node from the open queue
					dummyQueue.push(tS)		# push the current node into the dummy queue again
					openQueue.push(tS,pCost)	# push the current node into the openqueue
					tempDict = {tS:oQPoppedSucc}	
					tempDict2 = {tS:pCost}
					del costDict[tempDict2]		# delete the old cost entry from the dictionary of costs
					del dctnry[tempDict]		# delete the old parent entry from the dictionary of parents
					dctnry.update(tempDict)		# update the parent dictionary with the new parent
					costDict.update(tempDict2)  	# update the cost dictionary with the new cost
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  """
  This is similar to UCS algorithm but we also take into consideration 
  the manhatten heuristic distance which is the estimated straight line
  cost from the source to goal and add it with the cost to reach the
  current node from start. We then use this parameter as priority to push
  the node into the open queue
  """
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
   
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  
  openQueue = util.PriorityQueue()
  closedQueue = util.Queue()
  dummyQueue = util.Queue()
  
  moves = []
  cost = 0
  check = 0
  i = 0
  pCost = 0
  dctnry = {}
  costDict = {}
  
  parentStart = ()
  startState = problem.getStartState()
  startNode = (startState,'NoDir',0)
  if not(problem.isGoalState(startState)):
  	successors = problem.getSuccessors(startState)  	
  	for successor in successors:
  		pCost = successor[2]
  		mntDist = heuristic(successor[0],problem)
  		pCost = pCost + mntDist
  		openQueue.push(successor,pCost)  		
  		dummyQueue.push(successor)
  		tempDict = {successor:startNode}
  		tempDict2 = {successor:pCost}
  		costDict.update(tempDict2)
  		dctnry.update(tempDict)  		
  else:
  	print "Hurray!! Reached Goal : ",startState
  	return

  while not(openQueue.isEmpty()):  	
  	oQPoppedSucc = openQueue.pop()    	  	
  	closedQueue.push(oQPoppedSucc)  		
	succ = oQPoppedSucc[0]
	action = oQPoppedSucc[1]
	stepCost = oQPoppedSucc[2]  		
	
	if problem.isGoalState(succ):	
		print "Hurray!! Reached Goal : ",startState	
		finalRoute = util.Stack()
		goalNode = oQPoppedSucc
		tempNode = goalNode
		finalRoute.push(tempNode)
		while not(tempNode == startNode):
			tempNode = dctnry[tempNode]
			finalRoute.push(tempNode)
		while not(finalRoute.isEmpty()):
			node = finalRoute.pop()			
			action = node[1]
			cost = cost + node[2]
			if action == 'West':
				moves.append(w)
			elif action == 'South':
				moves.append(s)
			elif action == 'North':
				moves.append(n)
			elif action == 'East':
				moves.append(e)	
		return moves
				
	else:	
		tempSucc = problem.getSuccessors(succ)
		
		for tS in tempSucc:
			check = 0
			if tS[2]<0:
				if not(closedQueue.list.count(tS)==0):
					pCost = costDict[oQPoppedSucc]
					pCost = pCost+tS[2]
					mntDist = heuristic(tS[0],problem)	# calculate the manhatten heuristic distance
					pCost = pCost + mntDist			# update the cost
					prevPCost = costDict[tS]
					if pCost<prevPCost:
						tempDict = {tS:oQPoppedSucc}
						nodeCost = pCost - mntDst
						tempDict2 = {tS:nodeCost}
						del costDict[tempDict2]
						del dctnry[tempDict]
						dctnry.update(tempDict)
						costDict.update(tempDict2)	
			if (closedQueue.list.count(tS)==0 and dummyQueue.list.count(tS)==0):				
				check = 1
			if check == 1:		
				pCost = costDict[oQPoppedSucc]
				pCost = pCost + tS[2]
				mntDist = heuristic(tS[0],problem)		# calculate the manhatten heuristic distance
		  		pCost = pCost + mntDist				# update the cost
				openQueue.push(tS,pCost)
				dummyQueue.push(tS)
				tempDict = {tS:oQPoppedSucc}
				nodeCost = pCost - mntDist
				tempDict2 = {tS:nodeCost}
		  		costDict.update(tempDict2)
		  		dctnry.update(tempDict)
				check = 0
			elif dummyQueue.list.count(tS)>0:
				pCost = costDict[oQPoppedSucc]
				pCost = pCost + tS[2]
				mntDist = heuristic(tS[0],problem)		# calculate the manhatten heuristic distance	
				pCost = pCost + mntDist				# add it to the cost
				prevPCost = costDict[tS]
				if pCost<prevPCost:
					dummyQueue.list.remove(tS)
					openQueue.list.remove(tS)
					dummyQueue.push(tS)
					openQueue.push(tS,pCost)
					tempDict = {tS:oQPoppedSucc}
					nodeCost = pCost - mntDist
					tempDict2 = {tS:nodeCost}	
					del costDict[tempDict2]
					del dctnry[tempDict]
					dctnry.update(tempDict)
					costDict.update(tempDict2)
  
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
