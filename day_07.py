from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

lines = get_input("day_07_input")

root = {}
i_lines = iter(lines)
line = next(i_lines)
try:
    while True:
        if line.startswith("$ cd"):
            if line == "$ cd /":
                cur_dir = root
            elif line == "$ cd ..":
                cur_dir = cur_dir[".."]
            else:
                directory = line.split()[-1]
                cur_dir = cur_dir[directory]
        elif line.startswith("$ ls"):
            while line := next(i_lines):
                if line.startswith("$"):
                    break
                elif line.startswith("dir"):
                    directory = line.split()[-1]
                    cur_dir[directory] = {"..": cur_dir}
                else:
                    size, file = line.split()
                    cur_dir[file] = int(size)
            continue

        line = next(i_lines)
except StopIteration:
    pass

max_size = 100000
overall_total = 0
sizes = {}


def traverse(directory, name, sizes):
    global overall_total
    size = 0
    for key, value in directory.items():
        if key == "..":
            continue
        elif isinstance(value, dict):
            size += traverse(directory[key], key, sizes)
        else:
            size += value

    if size < max_size:
        overall_total += size

    sizes[name] = size
    return size


traverse(root, "/", sizes)

ANSWER1 = answer1(overall_total)

total_disk = 70000000
needed_size = 30000000
root_size = sizes["/"]
current_free_space = total_disk - root_size

min_dir = ""
min_size = total_disk
for directory, size in sizes.items():
    if directory == "/":
        continue

    temp_size = current_free_space + size
    if (temp_size >= needed_size) and (temp_size < min_size):
        min_dir = directory
        min_size = temp_size

ANSWER2 = answer2(min_size - current_free_space)
