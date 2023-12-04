import re
from typing import Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day


def pad_input(prob_input: List[str]) -> List[str]:
    padded_input = ['.' + input_str + '.' for input_str in prob_input]

    some_padding = len(padded_input[0]) * '.'
    padded_input.insert(0, some_padding)
    padded_input.append(some_padding)

    return padded_input


def get_adjacent_coordinates(coordinate: Tuple[int, int, int]) -> List[Tuple[int, int]]:
    row = coordinate[0]
    col = coordinate[1]
    value_len = len(str(coordinate[2]))

    coordinate_list = [(row, col - 1), (row, col + value_len)]
    for column in range(col -1, col + value_len + 1):
        coordinate_list.append((row - 1, column))
        coordinate_list.append((row + 1, column))

    
    return coordinate_list


def run_problem_one(prob_input: List[str]) -> int:
    prob_input = pad_input(prob_input)
    total = 0
    non_numeric_coordinates = set([(row, char_col) for row, string in enumerate(prob_input) for char_col, char in enumerate(string) if char != '.' and not char.isdigit()])

    for row, string in enumerate(prob_input):
        numeric_data = [(row, match.start(), int(match.group())) for match in re.finditer(r'\b\d+\b', string)]
        for coordinate in numeric_data:
            adjacent_coordinates = set(get_adjacent_coordinates(coordinate))
            #print(coordinate)
            #print(adjacent_coordinates)
            #print(non_numeric_coordinates)
            if len(adjacent_coordinates.intersection(non_numeric_coordinates)) > 0:
                total = total + coordinate[2]
                #print(f'Added ==> {coordinate[2]}')


    return total

if __name__ == "__main__":
    day = '03'
    prob_input = read_day(f'{day}a')
    ans = run_problem_one(prob_input)
    print(ans)


