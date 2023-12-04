import re
from typing import Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day


def run_problem_two(prob_input: List[str]) -> int:
    total = 0
    split_input = [prob.split(':') for prob in prob_input]

    matched_numbers_list = []
    for scratchcard in split_input: 
        numbers = scratchcard[1].strip().split('|')
        winning_numbers = set(numbers[0].strip().split())
        my_numbers = set(numbers[1].strip().split())
        matched_numbers = winning_numbers.intersection(my_numbers)
        matched_numbers_list.append(len(matched_numbers))

    count = [1] * len(matched_numbers_list)
    for index, item in enumerate(matched_numbers_list):
        num_matched = matched_numbers_list[index]
        
        # Update current card matches
        for i in range(index + 1, index + num_matched + 1):
            count[i] = count[i] + 1*count[index]
        

    return sum(count)



def run_problem_one(prob_input: List[str]) -> int:
    total = 0
    split_input = [prob.split(':') for prob in prob_input]
    for scratchcard in split_input:
        numbers = scratchcard[1].strip().split('|')
        winning_numbers = set(numbers[0].strip().split())
        my_numbers = set(numbers[1].strip().split())
        matched_numbers = winning_numbers.intersection(my_numbers)
        if len(matched_numbers) > 0:
            total = total + 2**(len(matched_numbers) - 1)
    return total


if __name__ == "__main__":
    day = '04'
    prob_input = read_day(f'{day}a')
    test_input = read_day(f'{day}a_test')
    ans = run_problem_one(prob_input)
    print(ans)

    ans = run_problem_two(test_input)
    print(ans)
    
    ans = run_problem_two(prob_input)
    print(ans)

