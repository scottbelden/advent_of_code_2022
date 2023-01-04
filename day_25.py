from utils import answer1, get_input

ANSWER1 = None

fuel_reqs = get_input("day_25_input")

char_to_int = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}


def to_reversed_base_5(base_10):
    base_5 = ""
    while base_10:
        base_5 += str(int(base_10 % 5))
        base_10 = int(base_10 / 5)

    return base_5


total = 0
for fuel_req in fuel_reqs:
    power = 1
    for char in reversed(fuel_req):
        total += char_to_int[char] * power
        power *= 5

balanced_5 = ""
carry = 0
for char in to_reversed_base_5(total):
    current = int(char) + carry
    if current in {0, 1, 2}:
        balanced_5 += str(current)
        carry = 0
    elif current == 3:
        balanced_5 += "="
        carry = 1
    elif current == 4:
        balanced_5 += "-"
        carry = 1
    elif current == 5:
        balanced_5 += "0"
        carry = 1
    else:
        raise Exception()

ANSWER1 = answer1(balanced_5[::-1])
