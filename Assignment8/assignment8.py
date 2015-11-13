# Ryan Tabler
# Assignment 8
# CSCI 3202

import sys
from string import ascii_lowercase

# Create a global list of characters we use
charList = list(ascii_lowercase) + ["_"]

# Create a global dictionary to convert characters to their numeric array indices
numDict = {}
i = 0
for c in ascii_lowercase:
	numDict[c] = i
	i += 1
numDict["_"] = 26

def toNum(c):
	global numDict
	return numDict[c]

def printPart1(evidence, transition, initial):
	# Prints all data as required for the Part I submission.

	global charList

	print("For Emission Probabilities:")
	print("P( E(t) | X(t) )")
	for x in charList:
		for e in charList:
			print("P( "+e+" | "+x+" ) = " + str(evidence[toNum(x)][toNum(e)]))
	print("")

	print("For Transition Probabilities:")
	print("P( X(t+1) | X(t) )")
	for xprev in charList:
		for x in charList:
			print("P( "+x+" | "+xprev+" ) = " + str(transition[toNum(xprev)][toNum(x)]))
	print("")

	print("For Marginal/Initial Probabilities:")
	print("P( X )")
	for x in charList:
		print("P( "+x+" ) = " + str(initial[toNum(x)]))

def verify(evidence, transition, initial):
	# Prints probability totals to the terminal. Values should be ~1.0.
	evidenceVerify = [sum(evidence[x]) for x in range(27)]
	transitionVerify = [sum(transition[xprev]) for xprev in range(27)]
	initialVerify = sum(initial)
	print(evidenceVerify)
	print(transitionVerify)
	print(initialVerify)

def main(argv):

	# Read in the data file
	filename = "typos20.data"
	datafile = open(filename, 'r')

	# Initialize counters with Laplace smoothing
	# [ X(t) ][ E(t) ]
	evidenceCount = [[1 for e in range(27)] for x in range(27)]
	# [ X(t-1) ][ X(t) ]
	transitionCount = [[1 for x in range(27)] for xprev in range(27)] # 
	# [ X(t) ]
	initialCount = [1 for x in range(27)]

	# Count data from the datafile
	line = datafile.readline()
	Xprev = line[0:1]
	Eprev = line[2:3]
	while(line != ""):
		
		X = line[0:1]
		E = line[2:3]
	
		# Increase count for letter frequency
		initialCount[ toNum(X) ] += 1
		# Increase count for X(t)->E(t) evidence
		evidenceCount[ toNum(X) ][ toNum(E) ] += 1
		# Increase count for X(t-1)->X(t) transition
		transitionCount[ toNum(Xprev) ][ toNum(X) ] += 1

		# Prepare for next iteration
		Xprev = X
		Eprev = E
		line = datafile.readline()

	# Count totals for every frequency distribution
	evidenceTotals = [sum(evidenceCount[x]) for x in range(27)]
	transitionTotals = [sum(transitionCount[xprev]) for xprev in range(27)]
	initialTotal = sum(initialCount)

	# Compute probability distributions
	evidence = [ [ float(evidenceCount[x][e])/float(evidenceTotals[x]) for e in range(27) ] for x in range(27) ]
	transition = [ [ float(transitionCount[xprev][x])/float(transitionTotals[xprev]) for x in range(27) ] for xprev in range(27) ]
	initial = [ float(initialCount[x])/float(initialTotal) for x in range(27) ]

	# Print data for Part 1 of homework
	printPart1( evidence, transition, initial )

if __name__ == "__main__":
	main(sys.argv)


