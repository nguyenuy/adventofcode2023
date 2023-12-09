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

    def __get_rank(self):
        count = sorted(list(Counter(list(self.card_hand)).values()))

        rank = 0

        if count == [5]:
            # Five of a kind
            rank = 7
        elif count == [1,4]:
            # 4 of a kind
            rank = 6
        elif count == [2, 3]:
            # Full House
            rank = 5
        elif count == [1, 1, 3]:
            # 3 of a kind
            rank = 4
        elif count == [1, 2, 2]:
            # 2 pair
            rank = 3
        elif count == [1, 1, 1, 2]:
            # 1 pair
            rank = 2
        elif count == [1, 1, 1, 1, 1]:
            # High Card
            rank = 1
        
        return rank
    
    def __lt__(self, other):
        if self.__get_rank() < other.__get_rank():
            return True
        elif self.card_hand == other.card_hand:
            return False
        elif self.__get_rank() == other.__get_rank():
            for x, y in zip(self.card_hand, other.card_hand):
                if Card(x) < Card(y):
                    return True
                elif Card(x) == Card(y):
                    continue
                else:
                    return False
        else:
            return False
    
    def __eq__(self, other):
        return self.card_hand == other.card_hand

    def __hash__(self):
        return hash(self.card_hand)

def run_problem_one(prob_input: List[str]) -> int:
    card_bids = {}
    for hand in prob_input:
        split = hand.split(' ')
        card_bids[CardHand(split[0])] = int(split[1])
    
    x = list(card_bids.keys())
    x = sorted(x)
    
    total_winnings = 0
    for i, hand in enumerate(x):
        rank = i + 1
        total_winnings = total_winnings + rank * card_bids[hand]
    
    return total_winnings

@dataclass
class Card2():
    card: str

    # This makes a static variable shared amongst all dataclasses
    order: ClassVar[str] = 'J23456789TQKA'

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
class CardHand2():
    card_hand: str

    def __get_rank(self):
        counts = Counter(list(self.card_hand)) 
        count = sorted(list(Counter(list(self.card_hand)).values()))

        rank = 0

        if count == [5]:
            # Five of a kind
            rank = 7
        elif count == [1,4]:
            # 4 of a kind
            rank = 6
            if 'J' in self.card_hand:
                rank = 7
        elif count == [2, 3]:
            # Full House
            rank = 5
            if 'J' in self.card_hand:
                rank = 7
        elif count == [1, 1, 3]:
            # 3 of a kind
            rank = 4
            if 'J' in self.card_hand:
                rank = 6
        elif count == [1, 2, 2]:
            # 2 pair
            rank = 3
            if 'J' in self.card_hand:
                if counts['J'] == 2:
                    rank = 6
                else:
                    rank = 5
        elif count == [1, 1, 1, 2]:
            # 1 pair
            rank = 2
            if 'J' in self.card_hand:
                rank = 4
        elif count == [1, 1, 1, 1, 1]:
            # High Card
            rank = 1
            if 'J' in self.card_hand:
                rank = 2
        
        return rank
    
    def __lt__(self, other):
        if self.__get_rank() < other.__get_rank():
            return True
        elif self.card_hand == other.card_hand:
            return False
        elif self.__get_rank() == other.__get_rank():
            for x, y in zip(self.card_hand, other.card_hand):
                if Card2(x) < Card2(y):
                    return True
                elif Card2(x) == Card2(y):
                    continue
                else:
                    return False
        else:
            return False
    
    def __eq__(self, other):
        return self.card_hand == other.card_hand

    def __hash__(self):
        return hash(self.card_hand)
        

def run_problem_two(prob_input: List[str]) -> int:
    card_bids = {}
    for hand in prob_input:
        split = hand.split(' ')
        card_bids[CardHand2(split[0])] = int(split[1])
    
    x = list(card_bids.keys())
    x = sorted(x)
    
    total_winnings = 0
    for i, hand in enumerate(x):
        rank = i + 1
        total_winnings = total_winnings + rank * card_bids[hand]
    
    return total_winnings


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



