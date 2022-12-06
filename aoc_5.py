
from ast import parse
import dotenv
import os
import re
import requests


DAY = 5


def get_test_data():
    test_data = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
    return test_data

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text

def parse_starting_row(line):
    return [line[i] for i in range(1, len(line), 4)]

def parse_instructions(line):
    regex = r'move (\d+) from (\d+) to (\d+)'
    match = re.match(regex, line)
    return ( int(match.group(1)), int(match.group(2)) - 1, int(match.group(3)) -1 )

def get_stacks(starting_rows):
    stacks = [ [] for _ in range(len(starting_rows[0])) ]
    for row in starting_rows[::-1]:
        for index, value in enumerate(row):
            if value != ' ':
                stacks[index].append(value)
    return stacks

def parse_input(input_data):
    starting_rows = []
    instructions = []
    for line in input_data.splitlines():
        if '[' in line:
            starting_rows.append(parse_starting_row(line))
        if 'move' in line:
            instructions.append(parse_instructions(line))
    starting_stacks = get_stacks(starting_rows)
    return starting_stacks, instructions

def solve_part_1(input_data):
    stacks, instructions = parse_input(input_data)
    for move, from_stack, to_stack in instructions:
        for _ in range(move):
            stacks[to_stack].append(stacks[from_stack].pop())
    return ''.join(stack[-1] for stack in stacks if stack)

def solve_part_2(input_data):
    stacks, instructions = parse_input(input_data)
    for move, from_stack, to_stack in instructions:
        for i in range(move):
            stacks[to_stack].append(stacks[from_stack].pop(-(move - i)))
    return ''.join(stack[-1] for stack in stacks if stack)


if __name__ == '__main__':
    # input_data = get_test_data()
    input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
