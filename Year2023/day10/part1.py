def find_start(broken_up_puzzle_input: list[list[str]]) -> tuple[int]:
    for y in range(len(broken_up_puzzle_input)):
        for x in range(len(broken_up_puzzle_input[y])):
            if broken_up_puzzle_input[y][x] == "S":
                return x, y


def move(broken_up_puzzle_input: list[list[str]], x: int, y: int, previous_x: int, previous_y: int, places: list[tuple[int]] = []) -> list[tuple[int]] | None:
    new_places = places.copy()
    new_places.append((x, y))
    tile = broken_up_puzzle_input[y][x]
    if tile == "S":
        return new_places
    elif tile == "|":
        if previous_y == y + 1:
            return move(broken_up_puzzle_input, x, y-1, x, y, new_places)
        elif previous_y == y - 1:
            return move(broken_up_puzzle_input, x, y+1, x, y, new_places)
        else:
            return
    elif tile == "-":
        if previous_x == x + 1:
            return move(broken_up_puzzle_input, x-1, y, x, y, new_places)
        elif previous_x == x - 1:
            return move(broken_up_puzzle_input, x+1, y, x, y, new_places)
        else:
            return
    elif tile == "L":
        if previous_y == y + 1:
            return move(broken_up_puzzle_input, x+1, y, x, y, new_places)
        elif previous_y == y + 1:
            return move(broken_up_puzzle_input, x, y+1, x, y, new_places)
        else:
            return
    elif tile == "J":
        if previous_x == x - 1:
            return move(broken_up_puzzle_input, x, y+1, x, y, new_places)
        elif previous_y == y + 1:
            return move(broken_up_puzzle_input, x-1, y, x, y, new_places)
        else:
            return
    elif tile == "7":
        if previous_y == y - 1:
            return move(broken_up_puzzle_input, x-1, y, x, y, new_places)
        elif previous_x == x - 1:
            return move(broken_up_puzzle_input, x, y-1, x, y, new_places)
        else:
            return
    elif tile == "F":
        if previous_x == x + 1:
            return move(broken_up_puzzle_input, x, y-1, x, y, new_places)
        elif previous_y == y - 1:
            return move(broken_up_puzzle_input, x+1, y, x, y, new_places)
        else:
            return


def move_from_start(broken_up_puzzle_input: list[list[str]], x: int, y: int):
    for i in range(4):
        new_x = x
        new_y = y
        if i == 0:
            new_y += 1
        elif i == 1:
            new_x += 1
        elif i == 2:
            new_y -= 1
        elif i == 3:
            new_x -= 1
        rv = move(broken_up_puzzle_input, new_x, new_y, x, y)
        if rv:
            return rv


def main(puzzle_input: str) -> int:
    broken_up_puzzle_input = puzzle_input.split("\n")
    for i in range(len(broken_up_puzzle_input)):
        broken_up_puzzle_input[i] = list(broken_up_puzzle_input[i])
    starting_x, starting_y = find_start(broken_up_puzzle_input)
    loop = move_from_start(broken_up_puzzle_input, starting_x, starting_y)
    largest = 0
    for i in range(len(loop)):
        if i <= len(loop) - i:
            if i > largest:
                largest = i
        else:
            if len(loop) - i:
                largest = len(loop) - i
    return largest
