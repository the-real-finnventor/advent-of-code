from os.path import dirname
from typing import Mapping


def step(nodes: Mapping[str, tuple[str]], curr: list[str], instruction: int) -> list[str]:
    new_curr: list[str] = []
    for node in curr:
        new_curr.append(nodes[node][instruction])
    return new_curr


def get_starting_curr(nodes: Mapping[str, tuple[str]]) -> list[str]:
    rv: list[str] = []
    for node in nodes:
        if list(node)[-1] == "A":
            rv.append(node)
    return rv


def main(instructions: list[int], nodes: Mapping[str, tuple[str]]) -> int:
    steps = 1
    curr = get_starting_curr(nodes)
    instruction = instructions[0]
    instruction_i = 0
    while True:
        curr = step(nodes, curr, instruction)
        ends_z = 0
        for node in curr:
            if list(node)[-1] == "Z":
                ends_z += 1
        if ends_z == len(curr):
            return steps
        if instruction_i + 1 == len(instructions):
            instruction_i = -1
        instruction_i += 1
        instruction = instructions[instruction_i]
        steps += 1


if __name__ == "__main__":
    with open(dirname(__file__) + "/input.txt", 'r') as f:
        lines = f.readlines()
    instructions: list[int] = []
    for direction in lines[0]:
        if direction == "L":
            instructions.append(0)
        elif direction == "R":
            instructions.append(1)
    nodes: Mapping[str, tuple[str]] = {}
    for node_line in lines[2:]:
        node_line = list(node_line)
        nodes[''.join(node_line[:3])] = (
            ''.join(node_line[7:10]), ''.join(node_line[12:15]))
    print(main(instructions, nodes))
