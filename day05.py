import re
from typing import Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day


def get_seeds(prob_input: List[str]) -> List[int]:
    seeds = prob_input[0].split(':')
    seeds = seeds[1]
    seeds = [int(seed) for seed in seeds.split()]
    return seeds


def construct_maps(prob_input: List[str]) -> Dict[str, List[Tuple[int, int, int]]]:
    prob_input: str = '\n'.join(prob_input) + '\n'
    
    mapped = {}
    keys = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    for key in keys:
        pattern = key + " map:(\s*\d+[\s\d]*)+(?=\n)"
        match = re.search(pattern, prob_input)
        if match:
            rows = [tuple(list(map(int, row.split()))) for row in match.group(1).strip().split('\n')]
            mapped[key] = rows
        
    return mapped


def get_mapping(value: int, map: List[Tuple[int, int, int]]) -> int:
    dest = value
    for mapping in map:
        dest_range_start = mapping[0]
        source_range_start = mapping[1]
        range_length = mapping[2]
        if (value >= source_range_start) and (value <= source_range_start + range_length):
            diff = value - source_range_start
            dest = dest_range_start + diff
            break
    
    return dest


def get_locations(seeds: List[int], seed_map: Dict[str, List[Tuple[int, int, int]]]) -> List[int]:
    locations = []
    for seed in seeds:
        seed_to_soil = get_mapping(seed, seed_map['seed-to-soil'])
        soil_to_fertilizer = get_mapping(seed_to_soil, seed_map['soil-to-fertilizer'])
        fertilizer_to_water = get_mapping(soil_to_fertilizer, seed_map['fertilizer-to-water'])
        water_to_light = get_mapping(fertilizer_to_water, seed_map['water-to-light'])
        light_to_temperature = get_mapping(water_to_light, seed_map['light-to-temperature'])
        temperature_to_humidity = get_mapping(light_to_temperature, seed_map['temperature-to-humidity'])
        humidty_to_location = get_mapping(temperature_to_humidity, seed_map['humidity-to-location'])
        locations.append(humidty_to_location)

    return locations

def run_problem_one(prob_input: List[str]) -> int:
    seeds = get_seeds(prob_input)
    seed_maps = construct_maps(prob_input)
    ans = min(get_locations(seeds, seed_maps))
    return ans

def run_problem_two(prob_input: List[str]) -> int:
    seeds = get_seeds(prob_input)
    min_value = None
    seed_maps = construct_maps(prob_input)
    it = iter(seeds)
    for x in it:
        seed_start = x
        seed_range = next(it)
        local_seeds = list(range(seed_start, seed_start + seed_range + 1))
        local_min = min(get_locations(local_seeds, seed_maps))
        if min_value is None:
            min_value = local_min
        elif local_min < min_value:
            min_value = local_min

    return min_value


if __name__ == "__main__":
    day = '05'
    test_input = read_day(f'{day}_test')
    ans = run_problem_one(test_input)
    print(f'Test Answer ===> {ans}')
    prob_input = read_day(f'{day}')
    ans = run_problem_one(prob_input)
    print(f'Day Answer ===> {ans}')

    ans = run_problem_two(test_input)
    print(f'Day Answer ===> {ans}')
    ans = run_problem_two(prob_input)
    print(f'Day Answer ===> {ans}')



