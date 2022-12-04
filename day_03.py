from utils import answer1, answer2, get_input
from string import ascii_letters

ANSWER1 = None
ANSWER2 = None

sacks = get_input("day_03_input")

mapping = {letter: index + 1 for index, letter in enumerate(ascii_letters)}

total = 0
for sack in sacks:
    total_items = len(sack)
    half = int(total_items / 2)
    sack_1 = set(sack[:half])
    sack_2 = set(sack[half:])

    total += mapping[(sack_1 & sack_2).pop()]

ANSWER1 = answer1(total)

total = 0
i_sacks = iter(sacks)
while True:
    try:
        sack_1 = set(next(i_sacks))
    except StopIteration:
        break
    sack_2 = set(next(i_sacks))
    sack_3 = set(next(i_sacks))

    total += mapping[(sack_1 & sack_2 & sack_3).pop()]

ANSWER2 = answer2(total)
