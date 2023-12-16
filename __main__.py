#!python3
import importlib
import fire
from typing import Literal


def get_advent_of_code_class(year, day):
    try:
        module_name = f"Year{year}.day{day}"
        class_name = f"AdventOfCode{year}Day{day}"

        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    except ImportError:
        raise fire.core.FireError(
            f"Module for Year {year} Day {day} not found.")
    except AttributeError:
        raise fire.core.FireError(
            f"Class AdventOfCode{year}Day{day} not found in module.")


def handler(year, day, part: Literal["part1", "part2"], example=False):
    if part == "part1":
        return get_advent_of_code_class(year, day)().part1(example)
    if part == "part2":
        return get_advent_of_code_class(year, day)().part2(example)


if __name__ == "__main__":
    fire.Fire(handler)
