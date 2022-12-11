from utils import answer1, answer2, get_input
from collections import deque

ANSWER1 = None
ANSWER2 = None

instructions = get_input("day_10_input")

cycle = 0
reg_x = 1
buffer = deque()
signal_strengths = []
i_instructions = iter(instructions)
doing_addx = False

while True:
    cycle += 1
    # During
    if not doing_addx:
        try:
            instruction = next(i_instructions)
        except StopIteration:
            break
        if instruction == "noop":
            doing_addx = False
            pass
        else:
            _, value = instruction.split()
            buffer.append((cycle + 1, int(value)))
            doing_addx = True
    else:
        doing_addx = False

    if cycle % 40 == 20:
        signal_strengths.append(cycle * reg_x)

    # After
    if buffer and buffer[0][0] == cycle:
        _, value = buffer.popleft()
        reg_x += value

ANSWER1 = answer1(sum(signal_strengths))

cycle = 0
reg_x = 1
buffer = deque()
i_instructions = iter(instructions)
doing_addx = False
screen = []
current_line = ""

while True:
    cycle += 1
    # During
    if not doing_addx:
        try:
            instruction = next(i_instructions)
        except StopIteration:
            break
        if instruction == "noop":
            doing_addx = False
            pass
        else:
            _, value = instruction.split()
            buffer.append((cycle + 1, int(value)))
            doing_addx = True
    else:
        doing_addx = False

    if (reg_x - 1) <= ((cycle - 1) % 40) <= (reg_x + 1):
        current_line += "#"
    else:
        current_line += "."

    if cycle % 40 == 0:
        screen.append(current_line)
        current_line = ""

    # After
    if buffer and buffer[0][0] == cycle:
        _, value = buffer.popleft()
        reg_x += value

for line in screen:
    print(line)

ANSWER2 = answer2("RBPARAGF")
