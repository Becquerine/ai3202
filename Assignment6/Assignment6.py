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
	data.getNode("P").setProbs(0.9)
	data.getNode("S").setProbs(0.3)
	data.getNode("C").addParent(data.getNode("P"))
	data.getNode("C").addParent(data.getNode("S"))
	data.getNode("C").setProbs({"PS":0.03, "P~S":0.001, "~PS":0.05, "~P~S":0.02,})
	data.getNode("X").addParent(data.getNode("C"))
	data.getNode("X").setProbs({"C":0.9, "~C":0.2})
	data.getNode("D").addParent(data.getNode("C"))
	data.getNode("D").setProbs({"C":0.65, "~C":0.3})
	return data

def parseArgs(args):
	for c in range(len(args)):
		if args[c:c+1] == "~":

		if args[c:c+1] == "m"

def computeMarginal(data, args):
	if len(args) == 0:
		return 0
	for c in args:


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


