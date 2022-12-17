
import dotenv
import os
import requests


DAY = 10


def get_test_data():
    test_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
    return test_data

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text


class Cpu:
    def __init__(self):
        self.sig_strengths = []
        self.register = 1
        self.cycle_count = 0

    def parse_cmds(self, raw_cmds):
        return (raw_cmd.split(' ') for raw_cmd in raw_cmds.splitlines())

    def addx(self, x):
        self.cycle()
        self.cycle()
        self.register += x

    def noop(self):
        self.cycle()

    def run(self, cmds):
        for cmd in self.parse_cmds(cmds):
            if cmd[0] == 'noop':
                self.noop()
            else:
                self.addx(int(cmd[1]))

    def sig_time(self):
        return (self.cycle_count - 20) % 40 == 0

    def calculate_signal_strength(self):
        self.sig_strengths.append(self.register * self.cycle_count)

    def cycle(self):
        self.cycle_count += 1
        if self.sig_time():
            self.calculate_signal_strength()

def solve_part_1(input_data):
    cpu = Cpu()
    cpu.run(input_data)
    return sum(cpu.sig_strengths)


def solve_part_2(input_data):
    return

if __name__ == '__main__':
    input_data = get_test_data()
    # input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
