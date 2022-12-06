
import dotenv
import os
import requests


DAY = 4


def get_test_data():
    test_data = '''2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8'''
    return test_data.replace('        ', '')

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text

def get_range_set(range_string):
    start, stop = range_string.split('-')
    return set(range(int(start), int(stop) + 1))

def get_assignment_pairs(assignment_list):
    for assignment in assignment_list.splitlines():
        first, second = assignment.split(',')
        yield get_range_set(first), get_range_set(second)

def solve_part_1(assignment_list):
    assignment_pairs = get_assignment_pairs(assignment_list)
    return sum( 1 for a, b in assignment_pairs if a <= b or b <= a )

def solve_part_2(assignment_list):
    assignment_pairs = get_assignment_pairs(assignment_list)
    return sum( 1 for a, b in assignment_pairs if a & b )


if __name__ == '__main__':
    # input_data = get_test_data()
    input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
