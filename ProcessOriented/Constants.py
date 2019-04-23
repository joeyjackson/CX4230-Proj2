from enum import Enum
import random


class LightState(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2
    L_GREEN = 3
    L_YELLOW = 4
    L_RED = 5

# 10th and Peach tree
seq10 = [
    (LightState.L_GREEN, 7),
    (LightState.L_YELLOW, 3.6),
    (LightState.L_RED, 2.2),
    (LightState.GREEN, 34.7),
    (LightState.YELLOW, 3.6),
    (LightState.RED, 49.3)
]

# 11th and Peach tree
seq11 = [
    (LightState.GREEN, 41.5),
    (LightState.YELLOW, 3.2),
    (LightState.RED, 55.4)
]

# 12th and Peach tree
seq12 = [
    (LightState.GREEN, 60.9),
    (LightState.YELLOW, 3.2),
    (LightState.RED, 35.7)
]

# 14th and Peach tree
seq14 = [
    (LightState.L_GREEN, 8.8),
    (LightState.L_YELLOW, 3.6),
    (LightState.L_RED, 3.6),
    (LightState.GREEN, 34.6),
    (LightState.YELLOW, 3.2),
    (LightState.RED, 46.1)
]

seq10E = [
    (LightState.L_GREEN, 8),
    (LightState.L_YELLOW, 1.8),
    (LightState.L_RED, 1.8),
    (LightState.GREEN, 30),
    (LightState.YELLOW, 3.8),
    (LightState.RED, 55)
]

endt = 60

car_length = 10
car_speed = 4.4196  # 14.5 ft/s
reaction_time = 2 + (car_length / car_length)

ip101_dist = lambda: random.gauss(7, 3)
ip102_dist = lambda: random.gauss(7, 3)
ip123_dist = lambda: random.gauss(7, 3)
ip103_dist = lambda: random.gauss(7, 3)
ip106_dist = lambda: random.gauss(7, 3)
ip112_dist = lambda: random.gauss(7, 3)

ip101_dest_dist = lambda: random.randint(0, 30)
ip102_dest_dist = lambda: random.randint(0, 30)
ip123_dest_dist = lambda: random.randint(0, 30)
ip103_dest_dist = lambda: random.randint(0, 30)
ip106_dest_dist = lambda: random.randint(0, 30)
ip112_dest_dist = lambda: random.randint(0, 30)

ip101_lane_dist = lambda: random.randint(1, 2)
ip102_lane_dist = lambda: random.randint(1, 2)
ip123_lane_dist = lambda: random.randint(1, 2)
ip103_lane_dist = lambda: random.randint(1, 2)
ip106_lane_dist = lambda: random.randint(1, 2)
ip112_lane_dist = lambda: random.randint(1, 2)


def end_time():
    global endt
    return endt


def set_end_time(time):
    global endt
    endt = time

