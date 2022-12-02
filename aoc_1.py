
import dotenv
import os
import requests


class TopNCalorieTracker:
    def __init__(self, n):
        self.n = n
        self.tracker = [0] * n

    def insert(self, calories):
        tracker = []
        idx = 0
        while idx < n:
            if calories > self.tracker[idx]:
                tracker.append(calories)
                tracker.extend(self.tracker[idx:-1])
                break
            else:
                tracker.append(self.tracker[idx])
            idx += 1
        self.tracker = tracker

    def total(self):
        return sum(self.tracker)


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

def get_calories_of_top_n_elves(n, food_list):
    # Sure, we could just create a long list of sums, sort, and sum the top 3, but where's the fun in that?
    calorie_tracker = TopNCalorieTracker(n)
    total_calories_per_elf = 0
    for food in food_list.splitlines():
        if food == '':
            calorie_tracker.insert(total_calories_per_elf)
            total_calories_per_elf = 0
        else:
            total_calories_per_elf += int(food)
    return calorie_tracker

# Answer to part 1
# if __name__ == '__main__':
#     food_list = get_input_data()
#     max_calories_carried_by_single_elf = get_max_calories_carried_by_single_elf(food_list)
#     print(f'The top elf carries {max_calories_carried_by_single_elf} calories')

# Answer to part 2
if __name__ == '__main__':
    n = 3
    food_list = get_input_data()
    calories_of_top_n_elves = get_calories_of_top_n_elves(n, food_list)
    print(calories_of_top_n_elves.tracker)
    print(f'The top elf carries {calories_of_top_n_elves.tracker[0]} calories')
    print(f'The top {n} elves carry {calories_of_top_n_elves.total()} calories')
