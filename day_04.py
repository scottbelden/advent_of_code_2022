from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

pairs = get_input("day_04_input")

part_1_total = 0
part_2_total = 0

for pair in pairs:
    elf_1, elf_2 = pair.split(",")
    e1_start, e1_end = elf_1.split("-")
    e2_start, e2_end = elf_2.split("-")

    e1_set = set(range(int(e1_start), int(e1_end) + 1))
    e2_set = set(range(int(e2_start), int(e2_end) + 1))

    if (e1_set - e2_set == set()) or (e2_set - e1_set == set()):
        part_1_total += 1

    if e1_set & e2_set:
        part_2_total += 1


ANSWER1 = answer1(part_1_total)
ANSWER2 = answer2(part_2_total)
