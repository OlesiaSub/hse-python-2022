import numpy as np

from hw3.matrix import Matrix


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


if __name__ == '__main__':
    np.random.seed(0)
    easy_artifacts()
