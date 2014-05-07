# Adds vectors from two different lists
def add_vectors(vec_list1, vec_list2):
	return [vec_list1[vectors] + vec_list2[vectors] for vectors in range(len(vec_list1))]

# Multiply a set of vectors by a scalar
def scalar_mul_vectors(scalar, vectorlist):
	return [x * scalar for x in vectorlist]

# A class representation of a vector
# f is the function and must be represented by a dictionary
# D is the domain of the function and must be a set
class Vec:
	def __init__(self, labels, function):
		self.D = labels
		self.f = function

# Assigns zero vectors to each element in a set
def zero_vec(D):
	return Vec(D, {d:0 for d in D})

TestVector = Vec({'A', 'B', 'C'}, {'A':1.})