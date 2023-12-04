import os

with open(os.path.dirname(__file__) + "/input.txt") as f:
    rows: list[list[int]] = []
    for line in f.readlines():
        new_row = []
        for tree in line:
            if tree != "\n":
                new_row.append(int(tree))
        rows.append(new_row)


def up(x: int, y: int) -> int:
    trees = 0
    for i in range(y+1):
        i = y - i
        trees += 1
        if rows[i][x] >= rows[y][x]:
            return trees
    return trees


def down(x: int, y: int) -> int:
    trees = 0
    for i in range(y, len(rows)):
        if i != y:
            trees += 1
            if rows[i][x] >= rows[y][x]:
                return trees
    return trees


def left(x: int, y: int) -> int:
    trees = 0
    for i in range(x+1):
        i = x - i
        trees += 1
        if rows[y][i] >= rows[y][x]:
            return trees
    return trees


def right(x: int, y: int) -> int:
    trees = 0
    for i in range(x, len(rows)):
        if i != x:
            trees += 1
            if rows[y][i] >= rows[y][x]:
                return trees
    return trees


def main() -> int:
    best_view = 0
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            view = up(x, y) * down(x, y) * left(x, y) * right(x, y)
            if best_view < view:
                best_view = view
    return best_view


if __name__ == "__main__":
    print(main())
