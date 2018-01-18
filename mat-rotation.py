

mat = [['a', 'b'], ['c', 'd']]

max_r = len(mat) - 1
max_c = len(mat[0]) - 1

for r in range(len(mat) // 2):

    ring = []
    c = r
    vector = [0, 1]  # (x, y)
    while True:

        if (r, c) == ring[0]:
            break

        ring.append((r, c))

        if vector == [0, 1]:
            if r < max_r:
                r += 1
            else:
                r = max_r
                c += 1
                vector = [1, 0]

        elif vector == [1, 0]:
            if c < max_c:
                c += 1
            else:
                c = max_c
                r -= 1
                vector = [0, -1]

        elif vector == [0, -1]:
            if r > 0:
                r -= 1
            else:
                r = 0
                c -= 1
                vector = [-1, 0]

        elif vector == [-1, 0]:
            if c > 0:
                c -= 1
            else:
                c = 0
                r += 1
                vector = [0, 1]


