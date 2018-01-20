#!/bin/python

import sys
from copy import deepcopy
from collections import deque


def matrixRotation(mat, amount=1):

    limit = min(len(mat), len(mat[0])) // 2
    max_r = len(mat) - 1
    max_c = len(mat[0]) - 1

    for i, r in enumerate(range(limit)):

        ring, values = deque([]), []
        c, s = r, 0
        while True:
            if ring and (r, c) == ring[0]:
                break
            ring.append((r, c))
            values.append(mat[r][c])
            if s == 0:
                if r < max_r - i:
                    r += 1
                else:
                    r = max_r - i
                    c += 1
                    s = 1
            elif s == 1:
                if c < max_c - i:
                    c += 1
                else:
                    c = max_c - i
                    r -= 1
                    s = 2
            elif s == 2:
                if r > i:
                    r -= 1
                else:
                    r = i
                    c -= 1
                    s = 3
            elif s == 3:
                if c > i:
                    c -= 1
                else:
                    c = i
                    r += 1
                    s = 0

        step = amount % len(values)
        if step == 0:
            continue

        ring.rotate(-step)
        for i, (r, c) in enumerate(ring):
            mat[r][c] = values[i]

    for row in mat:
        print(" ".join(map(str, row)))

    return mat


if __name__ == "__main__":


    def display(mat):
        for _ in mat:
            print(" ".join(map(str, _)))
        print("=================")

    mat = [
        [1, 8, 7],
        [2, 9, 6],
        [3, 4, 5],
    ]

    mat = [
        [1, 6, 5],
        [2, 3, 4],
    ]

    mat = [
        [1, 6],
        [2, 5],
        [3, 4],
    ]


    for x in range(10):
        print(x)
        mat = [
            [1, 2, 3, 4],
            [1, 5, 8, 4],
            [1, 6, 7, 4],
            [1, 2, 3, 4],
        ]
        display(matrixRotation(mat, x))

