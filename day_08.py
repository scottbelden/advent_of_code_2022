from utils import answer1, answer2, get_input
from collections import defaultdict

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_08_input")

rows = lines
temp = defaultdict(str)
for row in rows:
    for index, char in enumerate(row):
        temp[index] += char

cols = list(temp.values())

width = len(rows[0])
height = len(cols[0])


def is_visible(value, others):
    return int(value) > max(int(other) for other in others)


visible_count = width * 2 + height * 2 - 4
for x in range(1, width - 1):
    for y in range(1, height - 1):
        current_tree = rows[y][x]
        if (
            is_visible(current_tree, rows[y][:x])
            or is_visible(current_tree, rows[y][x + 1 :])
            or is_visible(current_tree, cols[x][:y])
            or is_visible(current_tree, cols[x][y + 1 :])
        ):
            visible_count += 1

ANSWER1 = answer1(visible_count)


def get_view(value, others):
    for index, tree in enumerate(others):
        if tree >= value:
            break

    return index + 1


scores = set()
for x in range(1, width - 1):
    for y in range(1, height - 1):
        current_tree = rows[y][x]
        scenic_score = (
            get_view(current_tree, reversed(rows[y][:x]))
            * get_view(current_tree, rows[y][x + 1 :])
            * get_view(current_tree, reversed(cols[x][:y]))
            * get_view(current_tree, cols[x][y + 1 :])
        )
        scores.add(scenic_score)

ANSWER2 = answer2(max(scores))
