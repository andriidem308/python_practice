from math import log2 as lg, pow, exp
import numpy as np


def entropy(arr):
    ent = 0

    for p in arr:
        if p <= 0: continue
        ent -= p * lg(p)

    return ent


def get_py_array(px, yx_matrix):
    py_array = [round(sum([px[i] * yx_matrix[i][j] for i in range(len(yx_matrix))]), 4) for j in range(len(yx_matrix))]
    return py_array


def get_entropy_x(px):
    hx = entropy(px)
    return hx


def get_entropy_y(px, yx_matrix):
    py_array = get_py_array(px, yx_matrix)
    hy = entropy(py_array)
    return hy


def get_entropy_yx(px, yx_matrix):
    hyx = sum([sum(px[i] * entropy(yx_matrix[i]) for i in range(len(yx_matrix)))])

    return hyx


def get_entropy_xy(px, yx_matrix):
    # py_array = get_py_array(px, yx_matrix)
    return get_entropy_x(px) - get_entropy_y(px, yx_matrix) + get_entropy_yx(px, yx_matrix)
    # new_matrix = [[yx_matrix[i][j] for i in range(len(yx_matrix))] for j in range(len(yx_matrix))]
    # hxy = sum([sum(py_array[i] * entropy(new_matrix[i]) for i in range(len(new_matrix)))])
    #
    # return hxy


def print_all(p, m):
    print("p(y) array:", get_py_array(p, m))
    print("H(X) =", get_entropy_x(p))
    print("H(Y) =", get_entropy_y(p, m))
    print("H(Y|X) =", get_entropy_yx(p, m))
    print("H(X|Y) = ", get_entropy_xy(p, m))
    print(lg(3))


if __name__ == "__main__":
    px = [0.4, 0.2, 0.4]
    # yx_matrix = [[0.15, 0.25, 0.6],
    #              [0.35, 0.25, 0.4],
    #              [0.49, 0.5, 0.01]]

    yx_matrix = [[0.7, 0.2, 0.1],
                 [0.1, 0.7, 0.2],
                 [0.2, 0.1, 0.7]]

    pxx = [10/43, 9/43, 5/43, 6/43, 7/43, 4/43, 1/43, 1/43]
    print(entropy(pxx))

    print_all(px, yx_matrix)
