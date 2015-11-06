import sys
import getopt
import copy

class Data:
	def __init__(self):
		self.data = [Node("c"), Node("s"), Node("r"), Node("w")]
	def getNode(self, c):
		for n in self.data:
			if n.name == c:
				return n
		return

class Node:
	def __init__(self, name):
		self.name = name
		self.parents = []
		self.probs = {}
	def addParent(self, n):
		self.parents.append(n)
	def deleteAllParents(self):
		self.parents = []
	def setProbs(self, probs):
		self.probs = probs
	def getProbs(self):
		return self.probs

def setupData():
	data = Data()
	data.getNode("c").setProbs(0.5)
	data.getNode("s").addParent(data.getNode("c"))
	data.getNode("s").setProbs({"c":0.1, "~c":0.5})
	data.getNode("r").addParent(data.getNode("c"))
	data.getNode("r").setProbs({"c":0.8, "~c":0.2})
	data.getNode("w").addParent(data.getNode("s"))
	data.getNode("w").addParent(data.getNode("r"))
	data.getNode("w").setProbs({"sr":0.99, "s~r":0.9, "~sr":0.9, "~s~r":0.0})
	return data

def parseArgs(args):
	i = 0
	params = [[],[]] # [results, conditions]
	c = 0
	while c < len(args): 
		if args[c:c+1] == "|":
			i += 1
		elif args[c:c+1] == "~":
			if c+1 >= len(args):
				print("A character must follow ~")
				return []
			param = args[c:c+2]
			c += 1
		else:
			param = args[c:c+1]
		c += 1
		params[i].append(param)	
	return params

def prior(data, samples, params):

	sampleSet = []
	fullSample = []
	fullSamples = []
	i = 0
	# Generate full samples from the data point samples
	while i < len(samples):
		sampleSet.append(samples[i])

		if len(sampleSet) == 4:
			for j in range(len(sampleSet)):
				node = data.data[j]
				parents = node.parents
				if len(parents) == 0: # Base node
					prob = node.getProbs() # Number
				else:
					key = ""
					for p in parents:
						key = key+p.name
					probs = node.getProbs()
					prob = probs[key]
					#prob = node.getProbs()[key] # Dictionary lookup

				if sampleSet[j] < prob:
					fullSample.append(node.name)
				else:
					fullSample.append("~"+node.name)

			fullSamples.append(fullSample)
			sampleSet = []
			fullSample = []

		i += 1

	# Count the data points that fit our conditions
	validFullSamples = fullSamples
	conditions = params[1]
	for f in validFullSamples:
		for c in conditions:
			if c in f:
				validFullSamples.remove(f)
				break
	
	# Count the data points that fit our data
	successfulValidFullSamples = copy.copy(validFullSamples)
	results = params[0]
	for f in successfulValidFullSamples:
		for r in results:
			if r in f:
				successfulValidFullSamples.remove(f)
				break

	# Return a (successes, total) tuple
	return (len(successfulValidFullSamples), len(validFullSamples))

def rejection(data, samples, params):
	return (-1.0, 1.0)
	'''
	results = params[0]
	conditions = params[1]

	sampleSet = []
	fullSample = [-1.0 for i in range(len(data.data))]
	fullSamples = []
	i = 0
	# Generate full samples from the data point samples
	while i < len(samples):

		for i in fullSample:

		
		node = data.data[j]
		parents = node.parents
		
		if len(parents) == 0: # Base node
			prob = node.getProbs() # Number
		else:
			key = ""
			for p in parents:
				key = key+p.name
			probs = node.getProbs()
			prob = probs[key]
			#prob = node.getProbs()[key] # Dictionary lookup

		if sampleSet[j] < prob:
			fullSample.append(node.name)
		else:
			fullSample.append("~"+node.name)



		i += 1
 
	# Reject when fails conditions
	# Add to full samples when meets conditions and result is calculated

	# Count the data points that fit our data
	successfulFullSamples = copy.copy(fullSamples)
	results = params[0]
	for f in successfulFullSamples:
		for r in results:
			if r in f:
				successfulFullSamples.remove(f)
				break

	# Return a (successes, total) tuple
	return (len(successfulFullSamples), len(fullSamples))
	'''

def main(argv):

	# A Data object containing Nodes
	# Everything as specified in the syllabus
	data = setupData()

	# Read in command-line arguments
	if len(argv) < 2:
		print("This program requires at least 2 arguments")
		return 0
	params = parseArgs(argv[2])

	filename = argv[0]
	sampleFile = open(filename, 'r')
	samples = [0.0 for x in range(100)]
	for x in range(len(samples)):
		samples[x] = float(sampleFile.readline())

	# Calculate and print
	results = (-1.0,1.0)
	if argv[1] == "-p":
		results = prior(data, samples, params)
		print("Calculated result using Prior sampling:")
	elif argv[1] == "-r":
		results = rejection(data, samples, params)
	print("Success rate: "+str(results[0])+" / "+str(results[1]))
	print(float(results[0]) / float(results[1]))

if __name__ == "__main__":
	main(sys.argv[1:])



