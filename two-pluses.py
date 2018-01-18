from collections import defaultdict

def twoPluses(grid):

    x, y = len(grid[0]) - 1, len(grid) - 1

    pluses = []

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):

            s = 0
            cells = set()
            while True:

                if "B" in (
                    grid[r - s if r - s > 0 else 0][c],
                    grid[r + s if r + s < y else y][c],
                    grid[r][c + s if c + s < x else x],
                    grid[r][c - s if c - s > 0 else 0],
                ):
                    break

                edge_reached = (
                    ((r + s) > y) or
                    ((r - s) < 0) or
                    ((c + s) > x) or
                    ((c - s) < 0)
                )

                if s >= 1 and edge_reached:
                    break

                cells.update([
                    (r - s, c), (r + s, c),
                    (r, c + s), (r, c - s),
                    (r, c)
                ])
                pluses.append(cells)
                cells = set(list(cells))

                if edge_reached:
                    break
                s += 1

    pluses.sort(key=lambda x: len(x), reverse=True)

    max_product = 1
    for c1 in pluses[:-1]:
        for c2 in pluses[1:]:
            if len(c1.intersection(c2)) > 0:
                continue
            if len(c1) == 1 and len(c2) == 1:
                continue
            if len(c1) * len(c2) > max_product:
                max_product = len(c1) * len(c2)
    return max_product




if __name__ == "__main__":

    g1 = (25, [ "BGBBGB", "GGGGGG", "BGBBGB", "GGGGGG", "BGBBGB", "BGBBGB", ])
    g2 = (5, [ "GGGGGG", "GBBBGB", "GGGGGG", "GGBBGB", "GGGGGG", ])
    g3 = (5, [ "BBGBB", "BGGGB", "BBGBG", ])
    g4 = (0, [ "BBGBB", "BGGGB", "BBGBB", ])

    g5 = (81, [
        "BBBGBGBBB",
        "BBBGBGBBB",
        "BBBGBGBBB",
        "GGGGGGGGG",
        "BBBGBGBBB",
        "BBBGBGBBB",
        "GGGGGGGGG",
        "BBBGBGBBB",
        "BBBGBGBBB",
        "BBBGBGBBB",
    ])

    for e, g in [g1, g2, g3, g4, g5]:
        print(e, twoPluses(g))

