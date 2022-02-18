class Matrix:

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    def __init__(self, n_matrix):
        self._validate_matrix(n_matrix)
        self._matrix = []
        for m in n_matrix:
            self._matrix.append(m)

    @staticmethod
    def _validate_matrix(matrix):
        for m in matrix:
            if len(m) != len(matrix[0]):
                raise ValueError("Dimensions of the given matrix differ")

    def _cmp_validate(self, other):
        if not isinstance(other, Matrix):
            raise Exception("Other is not an instance of Matrix class, unable to perform required operations")
        if (len(self._matrix[0]) != len(other.matrix[0])) or (len(self._matrix) != len(other.matrix)):
            raise Exception("Dimensions of matrices do not match")

    def __add__(self, other):
        res = []
        self._validate_matrix(other.matrix)
        self._cmp_validate(other)
        for o, i in zip(other.matrix, range(len(other.matrix))):
            res.append([o[j] + self._matrix[i][j] for j in range(len(o))])
        return Matrix(res)

    def __mul__(self, other):
        res = []
        self._validate_matrix(other.matrix)
        self._cmp_validate(other)
        for o, i in zip(other.matrix, range(len(other.matrix))):
            res.append([o[j] * self._matrix[i][j] for j in range(len(o))])
        return Matrix(res)

    def __matmul__(self, other):
        self._validate_matrix(other.matrix)
        self._cmp_validate(other)
        matrix_rows = list(zip(*other.matrix))
        res = [[sum(i * j for i, j in zip(row_a, col_b)) for col_b in matrix_rows] for row_a in self._matrix]
        return Matrix(res)

    def __str__(self):
        res = ""
        for s in self._matrix:
            res += str(s) + '\n'
        return '[' + res[:-1] + ']'
