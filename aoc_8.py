
import dotenv
import functools
import os
import requests


DAY = 8


def get_test_data():
    test_data = """30373
25512
65332
33549
35390
"""
    return test_data

def get_input_data():
    dotenv.load_dotenv()
    session_token = os.getenv('SESSION_TOKEN')
    session = requests.Session()
    session.headers.update({'Cookie': f'session={session_token}'})
    return session.get(f'https://adventofcode.com/2022/day/{DAY}/input').text

def get_surveys(input_data):
    horizontal =  [ [int(col) for col in row] for row in input_data.splitlines() ]
    vertical = [ [*cols] for cols in zip(*horizontal) ]
    return horizontal, vertical

def mark_trees(treeline):
    tallest = -1
    survey = []
    for i, tree in enumerate(treeline):
        if tree > tallest:
            tallest = tree
            survey.append(1)
        else:
            survey.append(0)
    return survey

def get_viewable_trees(treeline):
    survey = []
    for i, tree in enumerate(treeline):
        if i == 0:
            survey.append(0)
        elif tree > treeline[i-1]:
            survey.append(survey[i-1] + 1)
        else:
            survey.append(1)
    return survey

def get_scenic_score(treeviews):
    return functools.reduce(lambda a, b: a* b, treeviews)

def solve_part_1(input_data):
    h_survey, v_survey = get_surveys(input_data)
    l_t_r = [mark_trees(treeline) for treeline in h_survey]
    r_t_l = [mark_trees(treeline[::-1])[::-1] for treeline in h_survey]
    t_t_b = [*zip(*[mark_trees(treeline) for treeline in v_survey])]
    b_t_t = [*zip(*[mark_trees(treeline[::-1])[::-1] for treeline in v_survey])]
    visibile_trees = 0
    for row_views in zip(l_t_r, r_t_l, t_t_b, b_t_t):
        visibilies = [sum(trees) for trees in zip(*row_views)]
        visibile_trees += len([v for v in visibilies if v > 0])
    return visibile_trees

# def solve_part_2(input_data):
#     h_survey, v_survey = get_surveys(input_data)
#     l_t_r = [get_viewable_trees(treeline) for treeline in h_survey]
#     r_t_l = [get_viewable_trees(treeline[::-1])[::-1] for treeline in h_survey]
#     t_t_b = [*zip(*[get_viewable_trees(treeline) for treeline in v_survey])]
#     b_t_t = [*zip(*[get_viewable_trees(treeline[::-1])[::-1] for treeline in v_survey])]
#     max_view_score = 0
#     for row_views in zip(l_t_r, r_t_l, t_t_b, b_t_t):
#         print(row_views)
#         break
#         # view_score = [get_scenic_score(trees) for trees in zip(*row_views)]
#         # view_score = max([get_scenic_score(trees) for trees in zip(*row_views)])
#         # print(view_score)
#         # max_view_score = view_score if view_score > max_view_score else max_view_score
#     return max_view_score

def too_annoyed_to_care(input_data):
    h_survey, _ = get_surveys(input_data)
    scores = [[0] * len(h_survey[0]) for _ in range(len(h_survey))]
    for i in range(len(h_survey)):
        for j in range(len(h_survey[0])):
            count = [0, 0, 0, 0]
            tree = h_survey[i][j]

            x = i - 1
            y = j
            while x >= 0:
                new_tree = h_survey[x][y]
                count[0] += 1
                if new_tree >= tree:
                    break
                x -= 1

            x = i + 1
            y = j
            while x < len(h_survey):
                new_tree = h_survey[x][y]
                count[1] += 1
                if new_tree >= tree:
                    break
                x += 1

            x = i
            y = j - 1
            while y >= 0:
                new_tree = h_survey[x][y]
                count[2] += 1
                if new_tree >= tree:
                    break
                y -= 1

            x = i
            y = j + 1
            while y < len(h_survey[0]):
                new_tree = h_survey[x][y]
                count[3] += 1
                if new_tree >= tree:
                    break
                y += 1

            scores[i][j] = get_scenic_score(count)
    
    return max([max(row) for row in scores])

if __name__ == '__main__':
    input_data = get_test_data()
    input_data = get_input_data()
    answer_part_1 = solve_part_1(input_data)
    answer_part_2 = too_annoyed_to_care(input_data)
    # answer_part_2 = solve_part_2(input_data)
    print(f'The answer for part 1 is {answer_part_1}')
    print(f'The answer for part 2 is {answer_part_2}')
