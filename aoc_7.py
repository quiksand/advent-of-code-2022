
import dotenv
import os
import requests


DAY = 7


def get_test_data():
    test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    return test_data

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text


def create_directory_tree(input_data):
    directory = { '/': {} }
    current_directory = directory
    history = [directory]
    for line in input_data.splitlines():
        args = line.split(' ')
        if args[0] == '$':
            if args[1] == 'cd':
                if args[2] == '..':
                    current_directory = history.pop()
                else:
                    history.append(current_directory)
                    current_directory = current_directory[args[2]]
        else:
            if args[0] == 'dir':
                current_directory[args[1]] = {}
            else:
                current_directory[args[1]] = int(args[0])
    return directory

def get_directory_size(current_directory, tree):
    count = 0
    for k, v in current_directory.items():
        if isinstance(v, dict):
            size, sub_tree = get_directory_size(v, {})
            tree[k] = sub_tree
            count += size
        else:
            count += v
    tree['size'] = count
    return count, tree

def get_sizes_less_than(size, tree, vals):
    for k, v in tree.items():
        if isinstance(v, dict):
            get_sizes_less_than(size, v, vals)
        elif v < size:
            vals.append((k, v))
    return vals

def solve_part_1(input_data):
    file_system = create_directory_tree(input_data)
    _, size_tree = get_directory_size(file_system, {})
    sizes_less_than = get_sizes_less_than(100000, size_tree, [])
    return sum([item[1] for item in sizes_less_than])

def solve_part_2(input_data):
    total_space = 70000000
    required_space = 30000000
    file_system = create_directory_tree(input_data)
    _, size_tree = get_directory_size(file_system, {})
    directory_sizes = get_sizes_less_than(70000000, size_tree, [])
    directory_sizes.sort(key=lambda x: x[1])
    available_space = total_space - size_tree['size']
    needed_space = required_space - available_space
    return [x for x in directory_sizes if x[1] >= needed_space][0][1]


if __name__ == '__main__':
    # input_data = get_test_data()
    input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
