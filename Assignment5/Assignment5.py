import sys, getopt

'''
Ryan Tabler
Assignment 5
CSCI 3202
'''
# Questions answered in the README

# Calculates the best action and its utility
def bestUtility(world, worldDims, Ui, A, sx, sy):
	# Wrapper to simplify calculations for the 4 cardinal directions
	def U(x, y):
		if x < 0 or y < 0 or x >= worldDims[0] or y >= worldDims[1]:
			return 0
		else:
			return Ui[x][y]
	# Calculate utilities for 4 cardinal directions
	UNorth = 0.8*U(sx-1,sy) + 0.1*U(sx,sy+1) + 0.1*U(sx,sy-1)
	UEast = 0.8*U(sx,sy+1) + 0.1*U(sx-1,sy) + 0.1*U(sx+1,sy)
	USouth = 0.8*U(sx+1,sy) + 0.1*U(sx,sy+1) + 0.1*U(sx,sy-1)
	UWest = 0.8*U(sx,sy-1) + 0.1*U(sx+1,sy) + 0.1*U(sx-1,sy)
	UAll = [UNorth, UEast, USouth, UWest]
	# Calculate best action and return its utility
	'''Actions:
	0-North, 1-East, 2-South, 3-West
	'''
	maxU = 0
	bestPlan = 0
	for i in range(4):
		if UAll[i] > maxU:
			maxU = UAll[i]
			bestPlan = i
	A[sx][sy] = bestPlan
	return maxU

# Returns the reward for a tile
def R(world, worldDims, sx, sy):
	if sx < 0 or sy < 0 or sx >= worldDims[0] or sy >= worldDims[1]:
		return 0.0
	value = world[sx][sy]
	if value == 0: # Nothing
		return 0.0
	elif value == 1: # Mountain
		return -1.0
	elif value == 2: # Wall
		return 0.0
	elif value == 3: # Snake
		return -2.0
	elif value == 4: # Barn
		return 1.0
	elif value == 50: # Apples
		return 50.0
	else:
		return 0.0

def main(argv):
	# Read in command-line arguments
	if len(argv) != 2:
		print("Requires 2 arguments: world file and epsilon value")
		return
	filename = argv[0]
	epsilon = float(argv[1])

	# Create World matrix from text file
	worldFile1 = open(filename, 'r')
	world1Dims = (8,10) # X lines, Y units
	world1 = [[0 for x in range(world1Dims[1])] for x in range(world1Dims[0])]
	for i in range(world1Dims[0]):
		line = worldFile1.readline()
		lines = line.split()
		for j in range(world1Dims[1]):
			world1[i][j] = int(lines[j])

	# Uncomment this to see if the world matrix was created correctly
	#print(world1)

	# Initialize Utility and Action matrices
	UCurrent = [[0.0 for x in range(world1Dims[1])] for x in range(world1Dims[0])]
	UNext = [[0.0 for x in range(world1Dims[1])] for x in range(world1Dims[0])]
	Action = [[0 for x in range(world1Dims[1])] for x in range(world1Dims[0])]

	# First "iteration"
	for i in range(world1Dims[0]):
		for j in range(world1Dims[1]):
			UCurrent[i][j] = R(world1, world1Dims, i, j)

	# Do Value Iteration until delta is acceptable
	gamma = 0.9
	delta = float('Inf')
	threshhold = epsilon * (1-gamma) / gamma
	while (delta >= threshhold):
		
		# Iterate through all tiles
		for i in range(world1Dims[0]):
			for j in range(world1Dims[1]):

				# Horse cannot move through walls, so utility will always be 0
				if world1[i][j] == 2: # Wall
					UNext[i][j] = 0
					Action[i][j] = -1
				# Calculate utility
				else:
					UBest = bestUtility(world1, world1Dims, UCurrent, Action, i, j)
					UNext[i][j] = R(world1, world1Dims, i, j) + gamma * UBest

		# Calculate delta
		maxDelta = 0
		for i in range(world1Dims[0]):
			for j in range(world1Dims[1]):
				thisDelta = abs(UNext[i][j] - UCurrent[i][j])
				if thisDelta > maxDelta:
					maxDelta = thisDelta

				# Copy UNext into UCurrent in preparation for next iteration
				UCurrent[i][j] = UNext[i][j]

		delta = maxDelta


	# Follow the Actions to find the best path
	print("OPTIMAL PATH:")
	print("(Locations are X rows from the north and Y columns from the west)")
	start = (7,0)
	goal = (0,9)
	s = start
	print("Begin at " + str(s))
	while s != goal:
		a = Action[s[0]][s[1]]
		if a == 0:
			s = (s[0]-1,s[1])
		elif a == 1:
			s = (s[0],s[1]+1)
		elif a == 2:
			s = (s[0]+1,s[1])
		elif a == 3:
			s = (s[0],s[1]-1)
		else:
			print("ERROR")
			break
		
		if s[0]<0 or s[1]<0 or s[0]>=world1Dims[0] or s[1]>=world1Dims[1]:
			print("ERROR")
			break

		print("Move to " + str(s) + " with utility " + str(UCurrent[s[0]][s[1]]))


if __name__ == "__main__":
	main(sys.argv[1:])

