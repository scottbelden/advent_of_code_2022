from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

paths = get_input("day_14_input")

min_x = 500
max_x = 500
min_y = 0
max_y = 0
new_paths = []
for path in paths:
    new_path = []
    points = path.split(" -> ")
    for point in points:
        x, y = point.split(",")
        x = int(x)
        y = int(y)
        if x > max_x:
            max_x = x
        elif x < min_x:
            min_x = x

        if y > max_y:
            max_y = y

        new_path.append((x, y))

    new_paths.append(new_path)

min_x -= 1
max_x += 1
max_y += 1


def print_grid(grid):
    for row in grid:
        print("".join(row[min_x : max_x + 1]))


grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for new_path in new_paths:
    for index, point in enumerate(new_path):
        if index + 1 == len(new_path):
            break

        x1, y1 = point
        x2, y2 = new_path[index + 1]

        if x1 == x2:
            if y1 < y2:
                for _ in range(y1, y2 + 1):
                    grid[_][x1] = "#"
            else:
                for _ in range(y2, y1 + 1):
                    grid[_][x1] = "#"
        else:
            if x1 < x2:
                for _ in range(x1, x2 + 1):
                    grid[y1][_] = "#"
            else:
                for _ in range(x2, x1 + 1):
                    grid[y1][_] = "#"

sand_x = 500
sand_y = 0
solid = {"#", "o"}
rest = 0

while True:
    if sand_x == min_x or sand_x == max_x:
        break

    if grid[sand_y + 1][sand_x] == ".":
        sand_y += 1
        continue

    if (
        grid[sand_y + 1][sand_x] in solid
        and grid[sand_y + 1][sand_x - 1] in solid
        and grid[sand_y + 1][sand_x + 1] in solid
    ):
        grid[sand_y][sand_x] = "o"
        sand_x = 500
        sand_y = 0
        rest += 1
    elif grid[sand_y + 1][sand_x] in solid and grid[sand_y + 1][sand_x - 1] in solid:
        sand_x += 1
        sand_y += 1
    else:
        sand_x -= 1
        sand_y += 1

ANSWER1 = answer1(rest)

grid = [["." for _ in range(max_x + max_y)] for _ in range(max_y + 2)]

for new_path in new_paths:
    for index, point in enumerate(new_path):
        if index + 1 == len(new_path):
            break

        x1, y1 = point
        x2, y2 = new_path[index + 1]

        if x1 == x2:
            if y1 < y2:
                for _ in range(y1, y2 + 1):
                    grid[_][x1] = "#"
            else:
                for _ in range(y2, y1 + 1):
                    grid[_][x1] = "#"
        else:
            if x1 < x2:
                for _ in range(x1, x2 + 1):
                    grid[y1][_] = "#"
            else:
                for _ in range(x2, x1 + 1):
                    grid[y1][_] = "#"

for index in range(len(grid[-1])):
    grid[-1][index] = "#"

sand_x = 500
sand_y = 0
solid = {"#", "o"}
rest = 0

while True:
    if grid[sand_y + 1][sand_x] == ".":
        sand_y += 1
        continue

    if (
        grid[sand_y + 1][sand_x] in solid
        and grid[sand_y + 1][sand_x - 1] in solid
        and grid[sand_y + 1][sand_x + 1] in solid
    ):
        grid[sand_y][sand_x] = "o"
        rest += 1

        if sand_x == 501 and sand_y == 1:
            rest += 1
            break
        else:
            sand_x = 500
            sand_y = 0
    elif grid[sand_y + 1][sand_x] in solid and grid[sand_y + 1][sand_x - 1] in solid:
        sand_x += 1
        sand_y += 1
    else:
        sand_x -= 1
        sand_y += 1

ANSWER2 = answer2(rest)
