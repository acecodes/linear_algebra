import math


class Vector:

    """
    Class for vectors and vector operations
    All operations are staticmethods
    f is the function and must be represented by a dictionary
    D is the domain of the function and must be a set
    """

    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def __str__(self):
        return "Domain: " + str(self.D) + "\nFunction: " + str(self.f)

    @staticmethod
    def add_vectors(v, w):
        """Add two vectors"""
        return [v_i + w_i for v_i, w_i in zip(v, w)]

    @staticmethod
    def add_vector_lists(vec_list1, vec_list2):
        """Adds vectors from two different lists"""
        return [vec_list1[vectors] + vec_list2[vectors] for vectors in range(len(vec_list1))]

    @staticmethod
    def subtract_vectors(v, w):
        """Subtract vectors"""
        return [v_i - w_i for v_i, w_i in zip(v, w)]

    @staticmethod
    def multiply_by_scalar(s, v):
        """s is a scalar, v is a vector"""
        return [s * v_i for v_i in v]

    @staticmethod
    def dot_product(v, w):
        """Sum of componentwise products"""
        return (sum(v_i * w_i for v_i, w_i in zip(v, w)))

    @staticmethod
    def magnitude(v):
        """Size of a vector"""
        return math.sqrt(Vector.sum_of_squares(v))

    @staticmethod
    def sum_of_squares(v):
        """v_1 * v_1 + ... v_n * v_n"""
        return Vector.dot_product(v, v)

    @staticmethod
    def sum_vectors(vectors):
        return reduce(Vector.add_vectors, vectors)

    @staticmethod
    def scalar_mul_vectors(scalar, vectorlist):
        """Multiply a set of vectors by a scalar"""
        return [x * scalar for x in vectorlist]

    @staticmethod
    def zero_vec(D):
        """Assigns zero vectors to each element in a set"""
        return Vector(D, {d: 0 for d in D})

    @staticmethod
    def squared_distance(v, w):
        """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
        return Vector.sum_of_squares(Vector.subtract_vectors(v, w))

    @staticmethod
    def distance(v, w):
        return Vector.magnitude(Vector.subtract_vectors(v, w))

    @staticmethod
    def getitem(vec_instance, element_of_D):
        """Pulls an element from the function dictionary of a vector (or returns 0)"""
        if element_of_D in vec_instance.f:
            return vec_instance.f[element_of_D]
        else:
            return 0

    @staticmethod
    def list_dot(list1, list2):
        """Create a dot/scalar product from two lists of vectors"""
        if len(list1) != len(list2):
            return "These lists are not equal, please try again."
        else:
            return sum([list1[vectors] * list2[vectors] for vectors in range(len(list1))])

    @staticmethod
    def list2vec(input_list):
        """
        Creates a vector instance with list element indices acting as keys and
        the elements themselves acting as values.
        """
        return Vector(set(range(len(input_list))),
                      {key: value for key, value in enumerate(input_list)})

    @staticmethod
    def triangluar_solve(rowlist, label_list, b):
        """For solving a triangular system of linear equations"""
        x = Vector.zero_vec(set(label_list))
        for r in reversed(range(len(rowlist))):
            c = label_list[r]
            x[c] = (b[r] - x * rowlist[r]) / rowlist[r][c]
        return x


class Matrix:

    """
    Class for matrices
    All methods are staticmethods
    """

    def __init__(self, rows, columns, entry_function):
        self.rows = rows
        self.columns = columns
        self.matrix = [[entry_function(i, j) for j in range(self.columns)]
                       for i in range(self.rows)]

    @staticmethod
    def is_diagonal(i, j):
        """
        Create an identity (diagonal) matrix,
        which has ones diagonal and zeroes everywhere else
        """
        return 1 if i == j else 0

    @staticmethod
    def shape(A):
        """Get dimensions (shape) of matrix"""
        num_rows = len(A)
        num_cols = len(A[0]) if A else 0
        return num_rows, num_cols

    @staticmethod
    def get_row(A, i):
        """Get A_i from matrix"""
        return A[i]

    def get_column(A, j):
        """Get column j from matrix"""
        return [A_i[j] for A_i in A]


if __name__ == '__main__':
    # For testing out list2vec
    TestList1 = [1, 2, 3, 4, 5]
    TestList2 = [6, 7, 8, 9, 10]
    TestList3 = [2, 4, 6]

    # Test vector instance
    TestVector = Vector({'A', 'B', 'C'}, {'A': 1})

    # Test matrix instance
    TestMatrix = Matrix(5, 5, Matrix.is_diagonal)
    print(TestMatrix.matrix)
