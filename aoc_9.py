
import dotenv
import os
import requests


DAY = 9


# def get_test_data():
#     test_data = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# """
#     return test_data

def get_test_data():
    test_data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
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

def move_head(x, y, direction):
    match direction:
        case 'R':
            return x + 1, y
        case 'L':
            return x - 1, y
        case 'U':
            return x, y + 1
        case 'D':
            return x, y - 1

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def pretty_print(knots, w, h):
    board = [['.'] * w for _ in range(h)]
    for i, knot in enumerate(knots):
        x, y = knot
        symbol = str(i) if i != 0 else 'H'
        board_var = board[y][x]
        board[y][x] = symbol if board_var == '.' else board_var
    for row in board[::-1]:
        print(''.join(row))
    print()

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
    moves = parse_input_data(input_data)
    rope_length = 10
    knot_positions = [set() for _ in range(rope_length) ]
    # x_s = [11] * rope_length
    # y_s = [5] * rope_length
    x_s = [0] * rope_length
    y_s = [0] * rope_length
    for direction, steps in moves:
        # print()
        # print(direction, steps)
        for _ in range(steps):
            x_s[0], y_s[0] = move_head(x_s[0], y_s[0], direction)
            knot_positions[0].add((x_s[0], y_s[0]))
            for i in range(rope_length - 1):
                d_x = x_s[i] - x_s[i+1]
                d_y = y_s[i] - y_s[i+1]
                if must_move(x_s[i], y_s[i], x_s[i+1], y_s[i+1]):
                    x_s[i+1] += sign(d_x)
                    y_s[i+1] += sign(d_y)
                knot_positions[i + 1].add((x_s[i+1], y_s[i+1]))
        # pretty_print([*zip(x_s, y_s)], 6, 5)
        # pretty_print([*zip(x_s, y_s)], 26, 21)
    return len(knot_positions[rope_length-1])

if __name__ == '__main__':
    # input_data = get_test_data()
    input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
