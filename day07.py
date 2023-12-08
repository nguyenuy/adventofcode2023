from collections import Counter
from dataclasses import dataclass
from functools import reduce
import re
from typing import ClassVar, Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day


@dataclass
class Card():
    card: str

    # This makes a static variable shared amongst all dataclasses
    order: ClassVar[str] = '23456789TJQKA'

    def __lt__(self, other):
        return self.order.index(self.card) < self.order.index(other.card)
    
    def __eq__(self, other):
        return self.order.index(self.card) == self.order.index(other.card)

    def __le__(self, other):
        return self.order.index(self.card) <= self.order.index(other.card)

    def __ge__(self, other):
        return self.order.index(self.card) >= self.order.index(other.card)

    def __gt__(self, other):
        return self.order.index(self.card) > self.order.index(other.card)



@dataclass
class CardHand():
    card_hand: str

    def __get_type(self):
        count = Counter(list(self.card_hands))
        if len(count.values()) == 1:
            # Five of a kind
            return 7
        elif len(count.values()) == 5:
            # High Card
            return 1
        


def run_problem_one(prob_input: List[str]) -> int:
    return 0

def run_problem_two(prob_input: List[str]) -> int:
    return 0


if __name__ == "__main__":
    day = '07'
    test_input = read_day(f'{day}_test')
    ans = run_problem_one(test_input)
    print(f'Test Answer ===> {ans}')
    prob_input = read_day(f'{day}')
    ans = run_problem_one(prob_input)
    print(f'Day Answer ===> {ans}')

    ans = run_problem_two(test_input)
    print(f'Test Answer ===> {ans}')
    ans = run_problem_two(prob_input)
    print(f'Day Answer ===> {ans}')



