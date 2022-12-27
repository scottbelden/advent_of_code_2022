from utils import answer1, answer2, get_input

# from collections import defaultdict

ANSWER1 = None
ANSWER2 = None

cubes = get_input("day_18_input")

all_cubes = set()
for cube in cubes:
    x, y, z = cube.split(",")
    all_cubes.add((int(x), int(y), int(z)))

open_sides = 0
for cube in all_cubes:
    x, y, z = cube
    if (x - 1, y, z) not in all_cubes:
        open_sides += 1
    if (x + 1, y, z) not in all_cubes:
        open_sides += 1
    if (x, y - 1, z) not in all_cubes:
        open_sides += 1
    if (x, y + 1, z) not in all_cubes:
        open_sides += 1
    if (x, y, z - 1) not in all_cubes:
        open_sides += 1
    if (x, y, z + 1) not in all_cubes:
        open_sides += 1

ANSWER1 = answer1(open_sides)

# counter = defaultdict(int)
# for cube in all_cubes:
#     x, y, z = cube
#     if (x-1, y, z) not in all_cubes:
#         counter[(x-1, y, z)] += 1
#     if (x+1, y, z) not in all_cubes:
#         counter[(x+1, y, z)] += 1
#     if (x, y-1, z) not in all_cubes:
#         counter[(x, y-1, z)] += 1
#     if (x, y+1, z) not in all_cubes:
#         counter[(x, y+1, z)] += 1
#     if (x, y, z-1) not in all_cubes:
#         counter[(x, y, z-1)] += 1
#     if (x, y, z+1) not in all_cubes:
#         counter[(x, y, z+1)] += 1

# ANSWER2 = answer2(sum([value for value in counter.values() if value != 6]))
ANSWER2 = answer2("Unfinished")
