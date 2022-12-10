from utils import answer1, answer2, get_input
from dataclasses import dataclass

ANSWER1 = None
ANSWER2 = None

moves = get_input("day_09_input")

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
all_tail_positions = set()

for move in moves:
    direction, distance = move.split()
    for i in range(int(distance)):
        if direction == "R":
            head_x += 1
        elif direction == "U":
            head_y += 1
        elif direction == "D":
            head_y -= 1
        else:
            head_x -= 1

        manhattan_distance = abs(head_y - tail_y) + abs(head_x - tail_x)

        if manhattan_distance <= 1:
            pass
        elif manhattan_distance == 2:
            if head_x == tail_x:
                tail_y = int((tail_y + head_y) / 2)
            elif head_y == tail_y:
                tail_x = int((tail_x + head_x) / 2)
            else:
                pass
        elif manhattan_distance == 3:
            if abs(head_y - tail_y) == 1:
                tail_y = head_y
                tail_x = int((tail_x + head_x) / 2)
            else:
                tail_x = head_x
                tail_y = int((tail_y + head_y) / 2)
        else:
            raise Exception("Bug")

        all_tail_positions.add((tail_x, tail_y))

ANSWER1 = answer1(len(all_tail_positions))


@dataclass
class Position:
    x: int
    y: int

    def update_position(self, other):
        manhattan_distance = abs(other.y - self.y) + abs(other.x - self.x)

        if manhattan_distance <= 1:
            pass
        elif manhattan_distance == 2:
            if other.x == self.x:
                self.y = int((self.y + other.y) / 2)
            elif other.y == self.y:
                self.x = int((self.x + other.x) / 2)
            else:
                pass
        elif manhattan_distance == 3:
            if abs(other.y - self.y) == 1:
                self.y = other.y
                self.x = int((self.x + other.x) / 2)
            else:
                self.x = other.x
                self.y = int((self.y + other.y) / 2)
        elif manhattan_distance == 4:
            self.x = int((self.x + other.x) / 2)
            self.y = int((self.y + other.y) / 2)
        else:
            raise Exception("Bug")


head = Position(0, 0)
positions = [head] + [Position(0, 0) for i in range(9)]
all_tail_positions = set()

for move in moves:
    direction, distance = move.split()
    for i in range(int(distance)):
        if direction == "R":
            head.x += 1
        elif direction == "U":
            head.y += 1
        elif direction == "D":
            head.y -= 1
        else:
            head.x -= 1

        for index, position in enumerate(positions):
            if index == 0:
                continue
            else:
                position.update_position(positions[index - 1])

        all_tail_positions.add((positions[-1].x, positions[-1].y))

ANSWER2 = answer2(len(all_tail_positions))
