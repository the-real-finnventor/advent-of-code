import os
from dataclasses import dataclass


@dataclass
class Cube:
    amount: int
    cube_type: str


def parse(line: str) -> list[list[Cube]]:
    rv = []
    cube_sets = line.split(':')[1].strip().split(';')
    for cube_set in cube_sets:
        cube_set_list = []
        cubes = cube_set.strip().split(',')
        for cube in cubes:
            cube = cube.strip().split(' ')
            cube_set_list.append(Cube(int(cube[0]), cube[1]))
        rv.append(cube_set_list)
    return rv


def get_min(parsed: list[list[Cube]]):
    min_values = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for cube_set in parsed:
        for cube in cube_set:
            if cube.amount > min_values[cube.cube_type]:
                min_values[cube.cube_type] = cube.amount
    return min_values['red'] * min_values['green'] * min_values['blue']


def main():
    rv = 0
    with open(os.path.dirname(__file__) + "/input.txt", 'r') as f:
        for line in f.readlines():
            rv += get_min(parse(line))
    return rv


if __name__ == "__main__":
    print(main())
