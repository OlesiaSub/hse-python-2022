from hw3.matrix_mixin import RepresentationMixin


class MulMixin:

    # sum of squares % prime number
    def __hash__(self):
        res = 0
        mod = 10000019
        for m in self._matrix:
            res += sum(v * v for v in m)
        return res % mod


class Matrix(MulMixin, RepresentationMixin):

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
        self._mul_cache = {}

    @staticmethod
    def _validate_matrix(matrix):
        for m in matrix:
            if len(m) != len(matrix[0]):
                raise ValueError("Dimensions of the given matrix differ")

    def _cmp_validate(self, other):
        if (len(self._matrix[0]) != len(other.matrix[0])) or (len(self._matrix) != len(other.matrix)):
            raise Exception("Dimensions of matrices do not match")

    def __add__(self, other):
        res = []
        self._validate_matrix(other.matrix)
        self._cmp_validate(other)
        for m, i in zip(other.matrix, range(len(other.matrix))):
            res.append([m[j] + self._matrix[i][j] for j in range(len(m))])
        return Matrix(res)

    def __mul__(self, other):
        res = []
        self._validate_matrix(other.matrix)
        self._cmp_validate(other)
        for m, i in zip(other.matrix, range(len(other.matrix))):
            res.append([m[j] * self._matrix[i][j] for j in range(len(m))])
        return Matrix(res)

    def __matmul__(self, other):
        self._validate_matrix(other.matrix)
        self._cmp_validate(other)
        key = self.__hash__(), other.__hash__()
        if key in self._mul_cache:
            return self._mul_cache[key]
        matrix_rows = list(zip(*other.matrix))
        res = [[sum(i * j for i, j in zip(row, col)) for col in matrix_rows] for row in self._matrix]
        self._mul_cache[key] = Matrix(res)
        return Matrix(res)

    def __str__(self):
        res = ""
        for s in self._matrix:
            res += str(s) + '\n'
        return '[' + res[:-1] + ']'
