from dataclasses import dataclass
from functools import reduce
import re
from typing import Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day

def run_problem_one(prob_input: List[str]) -> int:
    return 0

def run_problem_two(prob_input: List[str]) -> int:
    return 0


if __name__ == "__main__":
    day = 'XX'
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



