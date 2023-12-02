import re
from typing import Dict, List, Literal, Match, Optional

from util.advent_reader import read_day



def is_exceeds_max(match: Optional[Match], max: int) -> bool:
    if match is None:
        return False
    else:
        number = int(match.group(1))
        if number > max:
            return True
        else:
            return False

def is_game_exceed_max(game: List[str], max_red: int, max_green: int, max_blue: int) -> bool:
    blue_pattern = r'(\b\d+\b)\s+blue\b'
    red_pattern = r'(\b\d+\b)\s+red\b'
    green_pattern = r'(\b\d+\b)\s+green\b'

    blue_match = re.search(blue_pattern, game)
    red_match = re.search(red_pattern, game)
    green_match = re.search(green_pattern, game)

    return is_exceeds_max(blue_match, max_blue) or is_exceeds_max(red_match, max_red) or is_exceeds_max(green_match, max_green)


def run_first_part(prob_input: List[str], max_red: int, max_green: int, max_blue: int) -> int:
    total = 0
    for entry in prob_input:
        game_info = entry.split(':')
        game_number = int(game_info[0].lstrip('Game '))
        game_info = game_info[1].split(';')

        is_exceeds = [is_game_exceed_max(game, max_red, max_green, max_blue)for game in game_info]
        if True not in is_exceeds:
            total = total + game_number

    return total

def get_max(game_info: List[str], match_pattern: Literal) -> int:
    current_max = 0
    
    for game in game_info:
        match = re.search(match_pattern, game)
        if match:
            number = int(match.group(1))
            if number > current_max:
                current_max = number
    
    return current_max
        

def run_second_part(prob_input: List[str]) -> int:
    total = 0
    for entry in prob_input:
        game_info = entry.split(':')
        game_number = int(game_info[0].lstrip('Game '))
        game_info = game_info[1].split(';')
        
        max_blue = get_max(game_info, r'(\b\d+\b)\s+blue\b')
        max_red = get_max(game_info, r'(\b\d+\b)\s+red\b')
        max_green = get_max(game_info, r'(\b\d+\b)\s+green\b')

        total = total + max_blue * max_red * max_green
    
    return total

if __name__ == "__main__":
    day = '02'
    prob_input = read_day(f'{day}a_test')
    ans = run_first_part(prob_input=prob_input, max_red=12, max_green=13, max_blue=14)

    prob_input = read_day(f'{day}a')
    ans = run_first_part(prob_input=prob_input, max_red=12, max_green=13, max_blue=14)
    print(ans)

    prob_input = read_day(f'{day}a_test')
    ans = run_second_part(prob_input=prob_input)
    print(ans)

    prob_input = read_day(f'{day}a')
    ans = run_second_part(prob_input=prob_input)
    print(ans)



