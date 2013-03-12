import math, random

LEVELS = [2,3,3,1]
class Node:
	def __init__(self, num_weights):
		self.weights = []
		self.threshhold = random.random()
		self.value = 0
		for i in range(num_weights):
			self.weights.append(random.random());
	def set_inputs(self, inputs):
		total = 0
		for i in range(len(inputs)):
			total += inputs[i] * self.weights[i];
		self.value = sigmoid(total);
	def set_output(self, output):
		self.value = output
	def set_threshhold(self, new_threshhold):
		self.threshhold = new_threshhold
	def fired(self):
		return self.value > self.threshhold
	def __repr__(self):
		return str(self.fired())
class Network:
	def __init__(self):
		self.levels = []
		for i in range(len(LEVELS)):
			level = []
			for j in range(LEVELS[i]):
				level.append(Node(LEVELS[max(i - 1, 0)]))
			self.levels.append(level)
	def __repr__(self):
		return str(self.levels)
	def set_inputs(self, inputs):
		for i in range(len(self.levels[0])):
			self.levels[0][i].set_output(inputs[i])
			self.levels[0][i].set_threshhold(0)
	def get_outputs(self, level):
		outputs = []
		for node in level:
			if node.fired():
				outputs.append(1)
			else:
				outputs.append(0)
		return outputs
	def compute(self):
		for i in range(len(self.levels)):
			if i != 0:
				for j in range(len(self.levels[i])):
					self.levels[i][j].set_inputs(self.get_outputs(self.levels[i - 1]))
def sigmoid(input):
	return 1 / (1 + math.exp(-input))

network = Network()
network.set_inputs([1, 0])
network.compute()
print network
