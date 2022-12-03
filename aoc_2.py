
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

# Would have made more sense to reverse opponent and your move in the dict, but I'm too lazy to change it now
outcome_of = {
    # YOUR_MOVE: {OPPONENT_MOVE: OUTCOME}
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

code_part_1 = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

code_part_2 = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
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
        round_score = get_round_score_part_1(opponent, you)
        match_totals += round_score
    return match_totals

def get_round_score_part_1(opponent, you):
    your_move = code_part_1[you]
    opponent_move = code_part_1[opponent]
    outcome = outcome_of[your_move][opponent_move]
    return value_of[your_move] + value_of[outcome]

def solve_part_2(guide):
    match_totals = 0
    for match in guide.splitlines():
        opponent, outcome = match.split(' ')
        round_score = get_round_score_part_2(opponent, outcome)
        match_totals += round_score
    return match_totals

def get_round_score_part_2(opponent, outcome):
    outcome = code_part_2[outcome]
    opponent_move = code_part_2[opponent]
    move_for_outcome = get_move_for_outcome()
    your_move = move_for_outcome[opponent_move][outcome]
    return value_of[your_move] + value_of[outcome]

def get_move_for_outcome():
    # It would be easier to just create a new dict, but I would rather practice rearranging the existing one
    move_for_outcome = { key: {} for key in outcome_of.keys() }
    for your_move, outcome_map in outcome_of.items():
        for opponent_move, outcome in outcome_map.items():
            move_for_outcome[opponent_move][outcome] = your_move
    return move_for_outcome

if __name__ == '__main__':
    encrypted_stategy_guide = get_input_data()
    match_totals_part_1 = solve_part_1(encrypted_stategy_guide)
    match_totals_part_2 = solve_part_2(encrypted_stategy_guide)
    print(f'Your total match score for part 1 is {match_totals_part_1}')
    print(f'Your total match score for part 2 is {match_totals_part_2}')
