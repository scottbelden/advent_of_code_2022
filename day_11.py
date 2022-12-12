from utils import answer1, answer2, get_line_separated_inputs
from dataclasses import dataclass
from typing import Callable

ANSWER1 = None
ANSWER2 = None

monkey_stats = get_line_separated_inputs("day_11_input")


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: int
    on_true: int
    on_false: int
    total_inspections: int = 0

    def do_test(self, value):
        self.total_inspections += 1
        return value % self.test == 0


monkeys = {}
for index, monkey_stat in enumerate(monkey_stats):
    for line in monkey_stat:
        if line.startswith("Starting items"):
            _, items = line.split(": ")
            starting_items = [int(item) for item in items.split(", ")]
        elif line.startswith("Operation"):
            tokens = line.split()
            final = tokens[-1]
            if tokens[-2] == "+":
                if final == "old":
                    operation = lambda x: x + x  # noqa
                else:
                    operation = lambda x, final=final: x + int(final)  # noqa
            else:
                if final == "old":
                    operation = lambda x: x * x  # noqa
                else:
                    operation = lambda x, final=final: x * int(final)  # noqa
        elif line.startswith("Test"):
            tokens = line.split()
            test = int(tokens[-1])
        elif line.startswith("If true"):
            tokens = line.split()
            on_true = int(tokens[-1])
        elif line.startswith("If false"):
            tokens = line.split()
            on_false = int(tokens[-1])

    monkey = Monkey(starting_items, operation, test, on_true, on_false)
    monkeys[index] = monkey

for game_round in range(20):
    for monkey in monkeys.values():
        while monkey.items:
            item = monkey.items.pop(0)
            worry_level = monkey.operation(item)
            worry_level = int(worry_level / 3)
            result = monkey.do_test(worry_level)
            if result:
                monkeys[monkey.on_true].items.append(worry_level)
            else:
                monkeys[monkey.on_false].items.append(worry_level)

total_inspections = sorted(
    [monkey.total_inspections for monkey in monkeys.values()], reverse=True
)

ANSWER1 = answer1(total_inspections[0] * total_inspections[1])


monkeys = {}
test_mult = 1
for index, monkey_stat in enumerate(monkey_stats):
    for line in monkey_stat:
        if line.startswith("Starting items"):
            _, items = line.split(": ")
            starting_items = [int(item) for item in items.split(", ")]
        elif line.startswith("Operation"):
            tokens = line.split()
            final = tokens[-1]
            if tokens[-2] == "+":
                if final == "old":
                    operation = lambda x: x + x  # noqa
                else:
                    operation = lambda x, final=final: x + int(final)  # noqa
            else:
                if final == "old":
                    operation = lambda x: x * x  # noqa
                else:
                    operation = lambda x, final=final: x * int(final)  # noqa
        elif line.startswith("Test"):
            tokens = line.split()
            test = int(tokens[-1])
            test_mult *= test
        elif line.startswith("If true"):
            tokens = line.split()
            on_true = int(tokens[-1])
        elif line.startswith("If false"):
            tokens = line.split()
            on_false = int(tokens[-1])

    monkey = Monkey(starting_items, operation, test, on_true, on_false)
    monkeys[index] = monkey

for game_round in range(10_000):
    for monkey in monkeys.values():
        while monkey.items:
            item = monkey.items.pop(0)
            worry_level = monkey.operation(item)
            result = monkey.do_test(worry_level)
            worry_level %= test_mult
            if result:
                monkeys[monkey.on_true].items.append(worry_level)
            else:
                monkeys[monkey.on_false].items.append(worry_level)

total_inspections = sorted(
    [monkey.total_inspections for monkey in monkeys.values()], reverse=True
)

ANSWER2 = answer2(total_inspections[0] * total_inspections[1])
