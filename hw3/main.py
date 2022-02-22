import numpy as np

from hw3.matrix import Matrix
from hw3.matrix_mixin import MatrixExt


def easy_artifacts():
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    res_add = m1 + m2
    res_mul = m1 * m2
    res_matmul = m1 @ m2
    with open('artifacts/easy/matrix+.txt', 'w') as fp:
        fp.write(res_add.__str__())
    with open('artifacts/easy/matrix*.txt', 'w') as fp:
        fp.write(res_mul.__str__())
    with open('artifacts/easy/matrix@.txt', 'w') as fp:
        fp.write(res_matmul.__str__())


def medium_artifacts():
    m1 = MatrixExt(np.random.randint(0, 10, (10, 10)))
    m2 = MatrixExt(np.random.randint(0, 10, (10, 10)))
    res_add = m1 + m2
    res_mul = m1 * m2
    res_matmul = m1 @ m2
    res_add.write_to_file('artifacts/medium/matrix+.txt')
    res_mul.write_to_file('artifacts/medium/matrix*.txt')
    res_matmul.write_to_file('artifacts/medium/matrix@.txt')


def hard_artifacts():
    A = Matrix([[2, 3], [9, 4]])
    C = Matrix([[8, 6], [3, 1]])
    B = Matrix([[1, 2], [3, 4]])
    D = Matrix([[1, 2], [3, 4]])
    AB = A @ B
    C._mul_cache = {}
    CD = C @ D
    A.write_to_file('artifacts/hard/A.txt')
    B.write_to_file('artifacts/hard/B.txt')
    C.write_to_file('artifacts/hard/C.txt')
    D.write_to_file('artifacts/hard/D.txt')
    AB.write_to_file('artifacts/hard/AB.txt')
    CD.write_to_file('artifacts/hard/CD.txt')
    with open('artifacts/hard/hash.txt', 'w') as fp:
        fp.write("Hash AB: " + str(AB.__hash__()) + '\n' + "Hash CD: " + str(CD.__hash__()))


if __name__ == '__main__':
    np.random.seed(0)
    easy_artifacts()
    medium_artifacts()
    hard_artifacts()
