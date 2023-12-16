def step(values: list[int]) -> list[int]:
    rv: list[int] = []
    for i in range(len(values)):
        if i != len(values) - 1:
            rv.append(values[i+1] - values[i])
    return rv


def get_values(line: str) -> list[int]:
    rv: list[int] = []
    for value in line.strip().split(" "):
        rv.append(int(value))
    return rv


def check_done(values: list[int]) -> bool:
    for value in values:
        if value != 0:
            return False
    return True


def find_next_history_value(previous_values: list[list[int]]) -> int:
    previous_values.append([0])
    for i in range(len(previous_values)-1):
        i = -1 - i
        previous_values[i-1].append(previous_values[i-1]
                                    [-1]+previous_values[i][-1])
    return previous_values[0][-1]


def main(puzzle_input: str) -> int:
    rv: int = 0
    for line in puzzle_input.split("\n"):
        previous_values: list[list[int]] = []
        values: list[int] = get_values(line)
        while not check_done(values):
            previous_values.append(values)
            values = step(values)
        rv += find_next_history_value(previous_values)
    return rv
