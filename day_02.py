from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

matches = get_input("day_02_input")

transform = {"X": "A", "Y": "B", "Z": "C"}
score_map = {"A": 1, "B": 2, "C": 3}
winner = {"A": "B", "B": "C", "C": "A"}
loser = {"A": "C", "B": "A", "C": "B"}

total_score = 0
for match in matches:
    them, me = match.split()
    me = transform[me]

    if them == me:
        total_score += 3 + score_map[me]
    elif me == winner[them]:
        total_score += 6 + score_map[me]
    else:
        total_score += score_map[me]

ANSWER1 = answer1(total_score)

total_score = 0
for match in matches:
    them, outcome = match.split()

    if outcome == "Y":
        total_score += 3 + score_map[them]
    elif outcome == "Z":
        total_score += 6 + score_map[winner[them]]
    else:
        total_score += score_map[loser[them]]

ANSWER2 = answer2(total_score)
