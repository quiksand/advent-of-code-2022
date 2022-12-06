
import dotenv
import os
import re
import requests


DAY = 6


class StreamWindow:
    def __init__(self, size):
        self.size = size
        self.length = 0
        self.window = [None] * size

    def add(self, value):
        self.length += 1
        self.window = self.window[1:] + [value]
    
    def detect_start(self):
        return len(set(self.window)) == self.size and self.length >= self.size


def get_test_data():
    test_data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    return test_data

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text

def solve_part_1(input_data):
    stream_window = StreamWindow(4)
    for char in input_data:
        stream_window.add(char)
        if stream_window.detect_start():
            return stream_window.length

def solve_part_2(input_data):
    pass


if __name__ == '__main__':
    # input_data = get_test_data()
    input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
