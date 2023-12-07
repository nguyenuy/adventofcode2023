from dataclasses import dataclass
from functools import reduce
import re
from typing import Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day

@dataclass
class Race:
    race_time: int
    distance_record: int

def get_race_info(prob_input: List[str]) -> List[Race]:
    time = prob_input[0]
    distance = prob_input[1]

    times = [int(val) for val in time.split(':')[1].strip().split()]
    distances = [int(val) for val in distance.split(':')[1].strip().split()]

    return [Race(t, d) for t, d in zip(times, distances)]



def get_race_info_part_two(prob_input: List[str]) -> Race:
    time = prob_input[0]
    distance = prob_input[1]
    
    full_time = int(''.join(time.split(':')[1].strip().split()))
    full_distance = int(''.join(distance.split(':')[1].strip().split()))

    return Race(full_time, full_distance)

def get_num_ways_to_win(race: Race) -> int:
    count = 0
    acceleration = 1
    
    for hold_time in range(0, race.race_time + 1):
        initial_velocity = hold_time * acceleration
        remaining_time = race.race_time - hold_time
        total_distance = initial_velocity * remaining_time
        if total_distance > race.distance_record:
            count+=1

    return count


def run_problem_one(prob_input: List[str]) -> int:
    race_info = get_race_info(prob_input)
    race_winning_info = [get_num_ways_to_win(x) for x in race_info]
    ans = reduce(lambda x, y: x*y, race_winning_info)
    return ans

def run_problem_two(prob_input: List[str]) -> int:
    race_info = get_race_info_part_two(prob_input)
    
    return get_num_ways_to_win(race_info)


if __name__ == "__main__":
    day = '06'
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



