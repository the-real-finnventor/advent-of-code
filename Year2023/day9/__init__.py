from os.path import dirname
from .part1 import main as p1
from .part2 import main as p2


class AdventOfCode2023Day9(object):
    def part1(self, example=False):
        open_path = "/input.txt"
        if example:
            open_path = "/example.txt"
        with open(dirname(__file__) + open_path) as f:
            puzzle_input = f.read()
        return p1(puzzle_input)

    def part2(self, example=False):
        open_path = "/input.txt"
        if example:
            open_path = "/example.txt"
        with open(dirname(__file__) + open_path) as f:
            puzzle_input = f.read()
        return p2(puzzle_input)
