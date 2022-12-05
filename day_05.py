from utils import answer1, answer2, get_input
from collections import deque, defaultdict

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_05_input", "rstrip")


def parse_input(lines):
    stacks = defaultdict(deque)
    moves = []

    for line in lines:
        if line == "":
            continue
        elif line.startswith(" 1"):
            continue
        elif line.startswith("move"):
            _, crates_to_move, _, start_stack, _, end_stack = line.split()
            moves.append((int(crates_to_move), int(start_stack), int(end_stack)))
        else:
            line = line.replace("] ", "")
            line = line.replace("]", "")
            line = line.replace("[", "")
            line = line.replace("    ", "\t")
            for index, char in enumerate(line):
                if char == "\t":
                    continue
                else:
                    stacks[index + 1].appendleft(char)
    return stacks, moves


stacks, moves = parse_input(lines)

for crates_to_move, start_stack, end_stack in moves:
    for _ in range(crates_to_move):
        stacks[end_stack].append(stacks[start_stack].pop())

answer = ""
for index in range(len(stacks)):
    answer += stacks[index + 1].pop()

ANSWER1 = answer1(answer)

stacks, moves = parse_input(lines)

for crates_to_move, start_stack, end_stack in moves:
    temp = []
    for _ in range(crates_to_move):
        temp.append(stacks[start_stack].pop())

    for char in reversed(temp):
        stacks[end_stack].append(char)

answer = ""
for index in range(len(stacks)):
    answer += stacks[index + 1].pop()

ANSWER2 = answer2(answer)
