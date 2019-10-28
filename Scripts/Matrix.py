# Returns true if x is a number
def is_number(x):
    try:
        0 + x
    except TypeError:
        return False
    return True


# Vectorial product of two lists
def vector_mul(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])


# Creates a null matrix
def null_matrix(r, c):
    result = []
    for i in range(r):
        result.append([])
        for _ in range(c):
            result[i].append([0])
    return result

class Matrix:
    # Default matrix is [[0]]
    def __init__(self, m=None):
        if m is None:
            m = [[0]]
        self.m = m

    # Returns the number of rows in a matrix
    def __len__(self):
        return len(self.m)

    # Returns a row of the matrix
    def __getitem__(self, key):
        return self.m[key]

    # Returns a row in a matrix
    def row(self, key):
        return self[key]

    # Returns a column in a matrix
    def col(self, key):
        return [x[key] for x in self]

    # Returns the matrix in a nice way
    def __str__(self):
        size = 0
        string = ""
        for row in self:
            for elem in row:
                if len(str(elem)) > size:
                    size = len(str(elem))
        for row in self:
            string += "[" + " "
            for elem in row:
                elem = str(round(elem, 5))
                if elem == "-0.0":
                    elem = "0.0"
                string += " " * (size - len(elem)) + elem + " "
            string += "]\n"
        return string

    # Sum of matrices
    def __add__(self, other):
        result = self
        for i in range(len(self)):
            for j in range(len(self[0])):
                result[i][j] += other[i][j]
        return result

    # Subtraction of matrices
    def __sub__(self, other):
        result = self
        for i in range(len(self)):
            for j in range(len(self[0])):
                result[i][j] -= other[i][j]
        return result

    # Multiplication of matrices
    def __mul__(self, other):
        if is_number(other):
            result = self
            for i in range(len(self)):
                for j in range(len(self[0])):
                    result[i][j] *= other
        else:
            result = []
            for i in range(len(self)):
                result.append([])
                for j in range(len(other[0])):
                    result[i].append(vector_mul(self[i], other.col(j)))
        return Matrix(result)

    # Multiplication of a matrix by -1
    def __neg__(self):
        result = self
        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] *= -1
        return result

    # Multiplication of a matrix by itself n times
    def __pow__(self, power, modulo=None):
        result = self
        if power < 0:
            power = abs(power)
            result = ~result
        for _ in range(power - 1):
            result *= result
        return result

    #
    def __invert__(self):
        pass

    #
    def __int__(self):
        pass

    def gauss(self):
        result = self

        def row_null(list1, list2, pivot):
            def mult(x):
                return x * list2[pivot]

            list1 = list(map(mult, list1))
            for i in range(len(list1)):
                list2[i] = list2[i] - list1[i]
            return list2

        for column in range(len(result[0]) - 1):
            if result[column][column] == 0:
                if not [x for x in result[column:].col(column) if x != 0]:
                    return None
                for row in range(column, len(result)):
                    if result[row][column] != 0:
                        result[row], result[column] = result[column], result[row]
            pivot = result[column][column]
            result.m[column] = list(map(lambda x: x / pivot, result[column]))
            for row in range(len(result)):
                if row == column:
                    continue
                result.m[row] = row_null(result[column], result[row], column)
        return result
