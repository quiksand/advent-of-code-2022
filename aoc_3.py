
from re import A
import dotenv
import os
import requests


DAY = 3


def get_test_data():
    test_data = '''vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw'''
    return test_data.replace('        ', '')

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text

def get_priority_map():
    uppers = [chr(i) for i in range(65, 91)]
    lowers = [chr(i) for i in range(97, 123)]
    return { item: value + 1 for value, item in enumerate(lowers + uppers) }

def get_duplicated_item(rucksack):
    compartment_one = set([ *rucksack[:len(rucksack) // 2] ])
    compartment_two = set([ *rucksack[len(rucksack) // 2:] ])
    return compartment_one.intersection(compartment_two).pop()

def solve_part_1(packing_list, priority_map):
    rucksacks = ( rucksack for rucksack in packing_list.splitlines() )
    duplicates = ( get_duplicated_item(rucksack) for rucksack in rucksacks )
    priorities = ( priority_map[item] for item in duplicates )
    return sum(priorities)

def get_group_lists(packing_list):
    elf_per_group = 3
    group = []
    for count, rucksack in enumerate(packing_list.splitlines(), 1):
        group.append(rucksack)
        if count % elf_per_group == 0:
            yield group
            group = []

def get_duplicated_group_items(group):
    return set.intersection(*[set([*rucksack]) for rucksack in group]).pop()

def solve_part_2(packing_list, priority_map):
    groups = ( group for group in get_group_lists(packing_list) )
    duplicates = ( get_duplicated_group_items(group) for group in groups )
    priorities = ( priority_map[item] for item in duplicates )
    return sum(priorities)


if __name__ == '__main__':
    # packing_list = get_test_data()
    packing_list = get_input_data()
    priority_map = get_priority_map()
    priority_sums_1 = solve_part_1(packing_list, priority_map)
    priority_sums_2 = solve_part_2(packing_list, priority_map)
    print(f'The answer for part 1 is {priority_sums_1}')
    print(f'The answer for part 2 is {priority_sums_2}')
