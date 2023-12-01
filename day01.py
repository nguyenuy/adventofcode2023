import re
from typing import Dict, List

from util.advent_reader import read_day


def run_first_part(prob_input: List[str]) -> int:
    filtered_numbers = [re.sub("[^0-9]", "", line) for line in prob_input]
    calibration_values = [int(f'{number[0]}{number[-1]}') for number in filtered_numbers]
    return sum(calibration_values)

def find_number_indices(numbers: Dict[str, str], full_string: str) -> Dict[str, int]:
    discovered = {}
    for key, value in numbers.items():
        key_indexes = [m.start() for m in re.finditer(key, full_string)]
        value_indexes = [m.start() for m in re.finditer(value, full_string)]
        discovered[key] = sorted(key_indexes + value_indexes)
    
    return discovered
    

def replace_number_strings(number_input: str) -> str:
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    discovered_numbers = find_number_indices(numbers, number_input)

    num_string = '*' * len(number_input)
    for key, value in discovered_numbers.items():
        for index in value:
            temp = list(num_string)
            temp[index] = numbers[key]
            num_string = "".join(temp)

    return num_string

def run_second_part(prob_input: List[str]) -> int:
    replaced_numbers = [replace_number_strings(line) for line in prob_input]

    filtered_numbers = [re.sub("[^0-9]", "", line) for line in replaced_numbers]
    calibration_values = [int(f'{number[0]}{number[-1]}') for number in filtered_numbers]
    return sum(calibration_values)


if __name__ == "__main__":
    day = '01'
    first_input = read_day(f'{day}a')
    ans = run_first_part(first_input)
    print(ans)


    second_test_input = read_day(f'{day}b_test')
    ans = run_second_part(first_input)
    print(ans)
    pass