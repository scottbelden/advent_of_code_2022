from utils import answer1, answer2, get_line_separated_inputs

ANSWER1 = None
ANSWER2 = None

sacks = get_line_separated_inputs("day_01_input")

totals = []
for sack in sacks:
    totals.append(sum(int(item) for item in sack))

ANSWER1 = answer1(max(totals))

totals.sort(reverse=True)

ANSWER2 = answer2(sum(totals[:3]))
