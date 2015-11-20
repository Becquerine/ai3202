import sys
import getopt

class Data:
	def __init__(self):
		self.data = [Node("P"), Node("S"), Node("C"), Node("D"), Node("X")]
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
	def setProbs(self, probs):
		self.probs = probs

def setupData():
	data = Data()
	data.getNode("p").setProbs(0.9)
	data.getNode("s").setProbs(0.3)
	data.getNode("c").addParent(data.getNode("p"))
	data.getNode("c").addParent(data.getNode("s"))
	data.getNode("c").setProbs({"ps":0.03, "p~s":0.001, "~ps":0.05, "~p~s":0.02,})
	data.getNode("x").addParent(data.getNode("c"))
	data.getNode("x").setProbs({"c":0.9, "~c":0.2})
	data.getNode("d").addParent(data.getNode("c"))
	data.getNode("d").setProbs({"c":0.65, "~c":0.3})
	return data

def parseArgs(args):
	def lowercase(params):
		allparams = [params]
		for i in range(len(params)):
			if (params[i] >= "A" and params[i] <= "Z"):
				params[i] = "~"+params[i].lower()
				allparams.append(params)
				allparams.append()

	params = []
	c = 0
	while c < len(args): 
		if args[c:c+1] == "~":
			if c+1 >= len(args) or (args[c+1:c+2] >= "A" and args[c+1:c+2] <= "Z"):
				print("A lowercase character must follow ~")
				return []
			param = args[c:c+2]
			c += 1
		else:
			param = args[c:c+1]
		params.append(param)

def computeMarginal(data, args):
	niceArgs = parseArgs(args)
	


def main(argv):

	# A Data object containing Nodes
	# Everything as specified in the syllabus
	data = setupData()

	# Read in command-line arguments
	if len(argv) == 0:
		print("This program requires at least 1 argument")
		return 0
	
	arg1 = argv[0]
	if len(arg1) < 2:
		return 0

	if arg1[0:2] == "-p": # Prior for Pollution or Smoking
		print("Unsupported")
		return
		setPrior(data, arg1[2:], argv[1])
		arg1 = argv[1]

	if arg1[0:2] == "-g": # Conditional
		print("Unsupported")
		return
		return computeConditional(data, arg1[2:])
	if arg1[0:2] == "-j": # Joint
		print("Unsupported")
		return
		return computeJoint(data, arg1[2:])
	if arg1[0:2] == "-m": # Marginal
		print("Unsupported")
		return
		return computeMarginal(data, arg1[2:])

if __name__ == "__main__":
	main(sys.argv[1:])


