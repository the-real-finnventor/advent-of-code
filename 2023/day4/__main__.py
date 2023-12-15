import os
from typing import Mapping, Literal

with open(os.path.dirname(__file__) + "/input.txt", 'r') as f:
    cards: list[Mapping[Literal["my_nums", "winning_nums"], list[int]]] = []
    for line in f.readlines():
        card: Mapping[Literal["my_nums", "winning_nums"], list[int]] = {
            "my_nums": [],
            "winning_nums": []
        }
        num_type: Literal["My number", "Winning number"] = "Winning number"
        for num in line.split(":")[1].strip().split(' '):
            if num.isnumeric():
                if num_type == "Winning number":
                    card["winning_nums"].append(int(num))
                elif num_type == "My number":
                    card["my_nums"].append(int(num))
            elif num == "|":
                num_type = "My number"
        cards.append(card)


def main() -> int:
    i = 0
    for card in cards:
        next_copy = i + 1
        for winning_num in card["winning_nums"]:
            if winning_num in card["my_nums"]:
                cards.append(cards[next_copy])
                next_copy += 1
        i += 1
    return len(cards)


if __name__ == "__main__":
    print(main())
