from typing import List

def read_problem_file(file_path: str) -> List[str]:
    'Reads in a files and returns the list'
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines
