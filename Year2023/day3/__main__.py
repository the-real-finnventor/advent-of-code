import os

with open(os.path.dirname(__file__) + "/input.txt") as f:
    lines: list[list[str]] = []
    for line in f.readlines():
        line = line.strip()
        curr: list[str] = []
        for char in line:
            curr.append(char)
        lines.append(curr)


def adjacent(x: int, y: int) -> bool:
    if x == 0:
        if y == 0:
            return lines[y+1][x] != '.' or lines[y][x+1] != '.'
        elif y + 1 == len(lines):
            return lines[y-1][x] != '.' or lines[y][x+1] != '.'
        else:
            return lines[y+1][x] != '.' or lines[y-1][x] != '.' or lines[y][x+1]
    elif x + 1 == len(lines[y]):
        if y == 0:
            return lines[y+1][x] != '.' or lines[y][x-1] != '.'
        elif y + 1 == len(lines):
            return lines[y-1][x] != '.' or lines[y][x-1] != '.'
        else:
            return lines[y+1][x] != '.' or lines[y-1][x] != '.' or lines[y][x-1] != '.'
    elif y == 0:
        return lines[y+1][x] != '.' or lines[y][x+1] != '.' or lines[y][x-1] != '.'
    elif y + 1 == len(lines):
        return lines[y-1][x] != '.' or lines[y][x+1] != '.' or lines[y][x-1] != '.'
    return lines[y+1][x] != '.' or lines[y-1][x] != '.' or lines[y][x+1] != '.' or lines[y][x-1] != '.'


def diagonal(x: int, y: int) -> bool:
    if x == 0:
        if y == 0:
            return lines[y+1][x+1] != '.'
        elif y + 1 == len(lines):
            return lines[y-1][x+1] != '.'
        else:
            return lines[y+1][x+1] != '.' or lines[y-1][x+1] != '.'
    elif x + 1 == len(lines[y]):
        if y == 0:
            return lines[y+1][x-1] != '.'
        elif y + 1 == len(lines):
            return lines[y-1][x-1] != '.'
        else:
            return lines[y+1][x-1] != '.' or lines[y-1][x-1] != '.'
    elif y == 0:
        return lines[y+1][x+1] != '.' or lines[y+1][x-1] != '.'
    elif y + 1 == len(lines):
        return lines[y-1][x+1] != '.' or lines[y-1][x-1] != '.'
    return lines[y+1][x+1] != '.' or lines[y+1][x-1] != '.' or lines[y-1][x+1] != '.' or lines[y-1][x-1] != '.'


def long_check(y: int, start_char: int, end_char: int) -> bool:
    for char_num in range(start_char, end_char+1):
        if adjacent(char_num, y) or diagonal(char_num, y):
            return True
    return False


def main() -> int:
    rv: int = 0
    for line_num in range(len(lines)):
        curr: str = ""
        curr_span: tuple = None
        for char_num in range(len(lines[line_num])):
            if lines[line_num][char_num].isnumeric():
                curr += lines[line_num][char_num]
                if not curr_span:
                    curr_span = (char_num, char_num)
                else:
                    curr_span = list(curr_span)
                    curr_span[1] = char_num
                    curr_span = tuple(curr_span)
            else:
                if curr_span and long_check(line_num, curr_span[0], curr_span[1]):
                    rv += int(curr)
                curr = ""
                curr_span = None
            if char_num + 1 == len(lines[line_num]) and curr:
                if curr_span and long_check(line_num, curr_span[0], curr_span[1]):
                    rv += int(curr)
                curr = ""
                curr_span = None
    return rv


if __name__ == "__main__":
    print(main())
