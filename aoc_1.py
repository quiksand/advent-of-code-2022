
import dotenv
import os
import requests


def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get('https://adventofcode.com/2022/day/1/input').text

def get_max_calories_carried_by_single_elf(food_list):
    max_calories_carried_by_single_elf = 0
    total_calories_per_elf = 0

    for food in food_list.splitlines():
        if food == '':
            if total_calories_per_elf > max_calories_carried_by_single_elf:
                max_calories_carried_by_single_elf = total_calories_per_elf
            total_calories_per_elf = 0
        else:
            total_calories_per_elf += int(food)

    return max_calories_carried_by_single_elf

if __name__ == '__main__':
    food_list = get_input_data()
    max_calories_carried_by_single_elf = get_max_calories_carried_by_single_elf(food_list)
    print(max_calories_carried_by_single_elf)
