
import dotenv
import os
import requests


value_of = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
    'LOSE': 0,
    'DRAW': 3,
    'WIN': 6,
}

outcome_of = {
    'ROCK': {
        'ROCK': 'DRAW',
        'PAPER': 'LOSE',
        'SCISSORS': 'WIN'
    },
    'PAPER': {
        'ROCK': 'WIN',
        'PAPER': 'DRAW',
        'SCISSORS': 'LOSE'
    },
    'SCISSORS': {
        'ROCK': 'LOSE',
        'PAPER': 'WIN',
        'SCISSORS': 'DRAW'
    }
}

code = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get('https://adventofcode.com/2022/day/2/input').text

def solve_part_1(guide):
    match_totals = 0
    for match in guide.splitlines():
        opponent, you = match.split(' ')
        round_score = get_round_score(opponent, you)
        print(round_score)
        match_totals += round_score
    return match_totals

def get_round_score(opponent, you):
    your_move = code[you]
    opponent_move = code[opponent]
    outcome = outcome_of[your_move][opponent_move]
    return value_of[your_move] + value_of[outcome]


# Answer to part 1
if __name__ == '__main__':
    encrypted_stategy_guide = get_input_data()
    print(encrypted_stategy_guide)
    match_totals = solve_part_1(encrypted_stategy_guide)
    print(f'Your total match score is {match_totals}')
