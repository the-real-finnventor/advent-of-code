import os
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    record: int


def get_ways(race: Race) -> int:
    rv = 0
    for time in range(1, race.time):
        if time * (race.time - time) > race.record:
            rv += 1
    return rv


if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt", 'r') as f:
        race: Race = []
        lines = f.readlines()
        for i in range(len(lines)):
            values: list[str] = lines[i].strip().split(' ')
            del values[0]
            while '' in values:
                values.remove('')
            value: int = int(''.join(values))
            if i == 0:
                race = Race(value, 0)
            else:
                race.record = value
    print(get_ways(race))
