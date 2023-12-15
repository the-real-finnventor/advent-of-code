import os
from typing import Literal, Mapping
from dataclasses import dataclass


@dataclass
class Hand:
    hand: str
    bid: int


rankings = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0
}


def evaluate_hand(hand: str) -> Literal["High card", "Pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]:
    card_nums = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }
    for card in hand:
        card_nums[card] += 1
    pairs = 0
    for card_type in card_nums:
        card_num = card_nums[card_type]
        if card_num == 5:
            return "Five of a kind"
        elif card_num == 4:
            return "Four of a kind"
        elif card_num == 3:
            for card_type in card_nums:
                card_num2 = card_nums[card_type]
                if card_num2 == 2:
                    return "Full house"
            return "Three of a kind"
        elif card_num == 2:
            pairs += 1
    if pairs == 2:
        return "Two pair"
    elif pairs == 1:
        return "Pair"
    elif pairs == 0:
        return "High card"


def main(hands: Mapping[Literal["High card", "Pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"], list[Hand]]) -> int:
    rv = 0
    ranks: list[Hand] = []
    for card_type in hands:
        new_hands = hands[card_type].copy()
        index = 0
        while new_hands:
            best = None
            i = 0
            for hand in new_hands:
                og_hand = hand
                hand = list(hand.hand)
                if not best or rankings[best[index]] < rankings[hand[index]]:
                    best = hand
                else:
                    ranks.append(og_hand)
                    del new_hands[i]
                i += 1
            index += 1
    for i in range(len(ranks)):
        rv += ranks[i].bid * i
    return rv


if __name__ == "__main__":
    hands = {
        "High card": [],
        "Pair": [],
        "Two pair": [],
        "Three of a kind": [],
        "Full house": [],
        "Four of a kind": [],
        "Five of a kind": []
    }
    with open(os.path.dirname(__file__) + "/input.txt", 'r') as f:
        for line in f.readlines():
            split = line.split(' ')
            hand = Hand(split[0], int(split[1]))
            hands[evaluate_hand(hand.hand)].append(hand)
    print(main(hands))
