from utils import answer1, answer2, get_input_as_str
from collections import deque

ANSWER1 = None
ANSWER2 = None

buffer = get_input_as_str("day_06_input")

four = deque(buffer[:3], maxlen=4)
for index, char in enumerate(buffer[3:]):
    four.append(char)
    if len(set(four)) == 4:
        break

ANSWER1 = answer1(index + 4)

four = deque(buffer[:3], maxlen=14)
for index, char in enumerate(buffer[3:]):
    four.append(char)
    if len(set(four)) == 14:
        break

ANSWER2 = answer2(index + 4)
