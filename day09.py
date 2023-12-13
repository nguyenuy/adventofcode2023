from collections import Counter
from dataclasses import dataclass
from functools import reduce
from math import lcm
import re
from typing import ClassVar, Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day

def convert_input(prob_input: List[str]) -> List[List[int]]:

    converted = []
    for prob in prob_input:
        converted.append([int(i) for i in prob.split()])

    return converted

def get_next_history_value(sequence: List[int]) -> int:
    current_sequence = sequence

    sequences = [current_sequence]

    while all(v == 0 for v in current_sequence) is False:
        current_sequence = [x - current_sequence[i - 1] for i, x in enumerate(current_sequence) if i > 0]
        sequences.append(current_sequence)
    
    next_value = None
    for s in sequences[::-1]:
        if next_value is None:
            next_value = s[-1]
        else:
            s.append(next_value + s[-1])
            next_value = s[-1]
    return sequences[0][-1]

def run_problem_one(prob_input: List[str]) -> int:
    prob_input = convert_input(prob_input)
    ans = sum([get_next_history_value(prob) for prob in prob_input])

    return ans

def get_next_history_value_part_two(sequence: List[int]) -> int:
    current_sequence = sequence

    sequences = [current_sequence]

    while all(v == 0 for v in current_sequence) is False:
        current_sequence = [x - current_sequence[i - 1] for i, x in enumerate(current_sequence) if i > 0]
        sequences.append(current_sequence)
    
    next_value = None
    for s in sequences[::-1]:
        if next_value is None:
            next_value = s[0]
        else:
            next_value = s[0] - next_value
            s.insert(0, next_value)
            next_value = s[0]
    return sequences[0][0]

def run_problem_one(prob_input: List[str]) -> int:
    prob_input = convert_input(prob_input)
    ans = sum([get_next_history_value(prob) for prob in prob_input])

    return ans

def run_problem_two(prob_input: List[str]) -> int:
    prob_input = convert_input(prob_input)
    ans = sum([get_next_history_value_part_two(prob) for prob in prob_input])

    return ans

if __name__ == "__main__":
    day = '09'
    test_input_1 = read_day(f'{day}_test_1')
    ans = run_problem_one(test_input_1)
    print(f'Test 1 Answer ===> {ans}')

    prob_input = read_day(f'{day}')
    ans = run_problem_one(prob_input)
    print(f'Day Answer Part 1 ===> {ans}')


    ans = run_problem_two(test_input_1)
    print(f'Test 1 Answer ===> {ans}')


    ans = run_problem_two(prob_input)
    print(f'Day Answer Part 2 ===> {ans}')



