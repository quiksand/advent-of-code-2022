
import dotenv
import functools
import os
import requests


DAY = 9


def get_test_data():
    test_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    return test_data

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text

def parse_input_data(input_data):
    moves = (line.split(' ') for line in input_data.splitlines())
    return ((move[0], int(move[1])) for move in moves)

def must_move(head_x, head_y, tail_x, tail_y):
    return abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1

def move_head(head_x, head_y, direction):
    match direction:
        case 'R':
            return head_x + 1, head_y
        case 'L':
            return head_x - 1, head_y
        case 'U':
            return head_x, head_y + 1
        case 'D':
            return head_x, head_y - 1

def solve_part_1(input_data):
    tail_positions = set()
    moves = parse_input_data(input_data)
    head_x = head_y = tail_x = tail_y = 0
    for direction, steps in moves:
        for _ in range(steps):
            prev_head_x, prev_head_y = head_x, head_y
            head_x, head_y = move_head(head_x, head_y, direction)
            if must_move(head_x, head_y, tail_x, tail_y):
                tail_x, tail_y = prev_head_x, prev_head_y
            tail_positions.add((tail_x, tail_y))
    return len(tail_positions)

def solve_part_2(input_data):
    return

if __name__ == '__main__':
    # input_data = get_test_data()
    input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
