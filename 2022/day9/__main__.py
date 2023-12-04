import os
from icecream import ic
from dataclasses import dataclass


@dataclass
class Move:
    direction: str
    amount: int


@dataclass
class Position:
    x: int
    y: int


with open(os.path.dirname(__file__) + "/input.txt", "r") as f:
    moves: list[Move] = []
    for move in f.readlines():
        moves.append(Move(move[0], int(move[2])))


def is_touching(h: Position, t: Position) -> bool:
    if h.x == t.x:
        if h.y == t.y:
            return True
        elif h.y - 1 == t.y:
            return True
        elif h.y + 1 == t.y:
            return True
    elif h.y == t.y:
        if h.x == t.x:
            return True
        elif h.x - 1 == t.x:
            return True
        elif h.x + 1 == t.x:
            return True
    elif h.x + 1 == t.x:
        if h.y + 1 == t.y:
            return True
        elif h.y - 1 == t.y:
            return True
    elif h.x - 1 == t.x:
        if h.y + 1 == t.y:
            return True
        elif h.y - 1 == t.y:
            return True
    return False


def fix_not_touching(h: Position, t: Position) -> Position:
    if h.x == t.x:
        if h.y > t.y:
            t.y += 1
        elif h.y < t.y:
            t.y -= 1
    elif h.y == t.y:
        if h.x > t.x:
            t.x += 1
        elif h.x < t.x:
            t.x -= 1
    elif h.x > t.x:
        t.x += 1
        if h.y > t.y:
            t.y += 1
        elif h.y < t.y:
            t.y -= 1
    elif h.x < t.x:
        t.x -= 2
        if h.y > t.y:
            t.y += 1
        elif h.y < t.y:
            t.y -= 1
    return t


def move_things(h: Position, t: Position, move: Move) -> int:
    t_visited = 0
    while move.amount:
        if move.direction == "U":
            h.y += 1
            move.amount -= 1
        elif move.direction == "D":
            h.y -= 1
            move.amount -= 1
        elif move.direction == "L":
            h.x -= 1
            move.amount -= 1
        elif move.direction == "R":
            h.x += 1
            move.amount -= 1
        if not is_touching(h, t):
            t = fix_not_touching(h, t)
            t_visited += 1
    return t_visited


def main() -> int:
    t_visited = 1
    h = Position(0, 0)
    t = Position(0, 0)
    for move in moves:
        t_visited += move_things(h, t, move)
        ic(t)
        ic(t_visited)
        ic(move)
        print()
    return t_visited


if __name__ == "__main__":
    print(main())
