from typing import Iterable


def is_valid(line: str):
    group_amounts: list[str] = line.split(" ")[1].split(',')
    for i in range(len(group_amounts)):
        group_amounts[i] = int(group_amounts[i])
    group_amounts: list[int]
    i: int = 0
    curr_len: int = 0
    for char in line.split(" ")[0]:
        if char == "#":
            curr_len += 1
        elif curr_len != group_amounts[i]:
            return False
        else:
            i += 1
            curr_len: int = 0
    return True


def is_more_unknown(line: Iterable) -> bool:
    for char in line:
        if char == "?":
            return True
    return False


def get_all_possible_arrangements(line: Iterable) -> int:
    line: list = list(line)
    rv: int = 0
    for i in range(len(line)):
        if line[i] == "?":
            new_line: list = line.copy()
            new_line[i] == "#"
            if not is_more_unknown(new_line):
                if is_valid(new_line):
                    rv += 1
            else:
                rv += get_all_possible_arrangements(new_line)
    return rv


def main(puzzle_input: str) -> int:
    rv: int = 0
    for line in puzzle_input.split("\n"):
        rv += get_all_possible_arrangements(line)
    return rv
