from typing import List

def read_problem_file(file_path: str) -> List[str]:
    'Reads in a files and returns the list'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def read_day(day: str) -> List[str]:
    directory = 'day'
    full_path = f'{directory}/{day}.txt'
    return read_problem_file(full_path)
