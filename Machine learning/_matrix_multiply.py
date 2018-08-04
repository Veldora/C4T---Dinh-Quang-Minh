import numpy as np

A = np.array([[1, 2, 3],
              [1, 4, 5]])

B = np.array([[1],
              [2],
              [3]])


def mat_multiply(a, b):
    if a.shape[1] != b.shape[0]:
        return False
    c = np.zeros((a.shape[0], b.shape[1]))
    for y in range(a.shape[0]):
        for x in range(a.shape[1]):
            for z in range(b.shape[1]):
                c[y][z] += a[y][x] * b[x][z]
    return c


C = mat_multiply(A, B)

print(C)
# print(A.shape)
# print(B.shape)
