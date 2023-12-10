from collections import Counter
from dataclasses import dataclass
from functools import reduce
from math import lcm
import re
from typing import ClassVar, Dict, List, Literal, Match, Optional, Tuple

from util.advent_reader import read_day


def get_instructions(prob_input: List[str]) -> List[str]:
    instructions = list(prob_input[0])
    return instructions

def get_map_network(prob_input: List[str]) -> Dict[str, List[str]]:
    mapped_nodes = {}
    for i in range(2, len(prob_input)):
        node_split = prob_input[i].split('=')
        node = node_split[0].strip()

        pattern = r"\b\w+\b"
        matches = re.findall(pattern, node_split[1].strip())
        mapped_nodes[node] = matches





    return mapped_nodes

def run_problem_one(prob_input: List[str]) -> int:
    instructions = get_instructions(prob_input)
    mapped_network = get_map_network(prob_input)

    current_node = 'AAA'
    end_node = 'ZZZ'

    steps = 0
    while current_node != 'ZZZ':
        instruction_index = steps % len(instructions)
        current_instruction = instructions[instruction_index]
        if current_instruction == 'L':
            current_node = mapped_network[current_node][0]
        else:
            current_node = mapped_network[current_node][1]
        
        
        steps += 1
    return steps
        

def run_problem_two(prob_input: List[str]) -> int:
    instructions = get_instructions(prob_input)
    mapped_network = get_map_network(prob_input)

    current_nodes = [node for node in mapped_network.keys() if node[-1] == 'A']
    steps = 0
    step_list = [0] * len(current_nodes)
    
    while True:
        instruction_index = steps % len(instructions)
        current_instruction = instructions[instruction_index]
        next_node = ""
        next_nodes = []
        steps += 1 

        for i, node in enumerate(current_nodes):
            if current_instruction == 'L':
                next_node = mapped_network[node][0]
                next_nodes.append(next_node)
            else:
                next_node = mapped_network[node][1]
                next_nodes.append(next_node)
        
            if next_node[-1] == 'Z' and step_list[i] == 0:
                step_list[i] = steps

        current_nodes = next_nodes
        is_nonzero = all(element != 0 for element in step_list)
        if is_nonzero:
            return lcm(*step_list)

        


if __name__ == "__main__":
    day = '08'
    test_input_1 = read_day(f'{day}_test_1')
    test_input_2 = read_day(f'{day}_test_2')
    test_input_3 = read_day(f'{day}_test_3')
    ans = run_problem_one(test_input_1)
    print(f'Test 1 Answer ===> {ans}')

    
    ans = run_problem_one(test_input_2)
    print(f'Test 2 Answer ===> {ans}')

    prob_input = read_day(f'{day}')
    ans = run_problem_one(prob_input)
    print(f'Day Answer Part 1 ===> {ans}')

 
    ans = run_problem_two(test_input_3)
    print(f'Test Answer ===> {ans}')
    ans = run_problem_two(prob_input)
    print(f'Day Answer ===> {ans}')



