# A class representation of a vector
# f is the function and must be represented by a dictionary
# D is the domain of the function and must be a set
class Vec:
	def __init__(self, labels, function):
		self.D = labels
		self.f = function

	def __str__(self):
		return "Domain: " + str(self.D) + "\nFunction: " + str(self.f)

# Adds vectors from two different lists
def add_vectors(vec_list1, vec_list2):
	return [vec_list1[vectors] + vec_list2[vectors] for vectors in range(len(vec_list1))]

# Multiply a set of vectors by a scalar
def scalar_mul_vectors(scalar, vectorlist):
	return [x * scalar for x in vectorlist]

# Assigns zero vectors to each element in a set
def zero_vec(D):
	return Vec(D, {d:0 for d in D})

# Pulls an element from the function dictionary of a vector (or returns 0)
def getitem(vec_instance, element_of_D):
	if element_of_D in vec_instance.f:
		return vec_instance.f[element_of_D]
	else:
		return 0

# Creates a vector instance with list element indices acting as keys and the elements themselves acting as values.  
def list2vec(input_list):
	number = 0
	return Vec(set(range(len(input_list))), {key:value for key,value in enumerate(input_list)})

TestVector = Vec({'A', 'B', 'C'}, {'A':1.})