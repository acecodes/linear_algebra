# Adds vectors from two different lists
def add_vectors(vec_list1, vec_list2):
	return [vec_list1[vectors] + vec_list2[vectors] for vectors in range(len(vec_list1))]

# Multiply a set of vectors by a scalar
def scalar_mul_vectors(scalar, vectorlist):
	return [x * scalar for x in vectorlist]