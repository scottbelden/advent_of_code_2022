from utils import answer1, answer2, get_input
from dataclasses import dataclass

ANSWER1 = None
ANSWER2 = None

report = get_input("day_15_input")


@dataclass
class Sensor:
    x: int
    y: int
    beacon_x: int
    beacon_y: int

    def get_distance(self, other_x, other_y):
        return abs(self.x - other_x) + abs(self.y - other_y)

    def __post_init__(self):
        self.distance = self.get_distance(self.beacon_x, self.beacon_y)


sensors = []
for line in report:
    (
        _,
        _,
        sensor_x_part,
        sensor_y_part,
        _,
        _,
        _,
        _,
        beacon_x_part,
        beacon_y_part,
    ) = line.split()
    sensor_x = int(sensor_x_part[2:-1])
    sensor_y = int(sensor_y_part[2:-1])
    beacon_x = int(beacon_x_part[2:-1])
    beacon_y = int(beacon_y_part[2:])
    sensors.append(Sensor(sensor_x, sensor_y, beacon_x, beacon_y))


TEST_LINE = 2000000
x_points = set()

for sensor in sensors:
    difference = sensor.distance - sensor.get_distance(sensor.x, TEST_LINE)
    if difference < 0:
        # Too far away
        continue
    else:
        x_points = x_points | set(
            range(sensor.x - difference, sensor.x + difference + 1)
        )

for sensor in sensors:
    if sensor.beacon_y == TEST_LINE and sensor.beacon_x in x_points:
        x_points.remove(sensor.beacon_x)

ANSWER1 = answer1(len(x_points))
ANSWER2 = answer2("Unfinished")
