from enum import Enum
import random
import numpy as np


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

endt = 1000

car_length = 5
car_speed = 7.5  # m/s
reaction_time = 1 + (car_length / car_length)

ip101_dist = lambda: np.random.exponential(scale=6.471338129496403)
ip102_dist = lambda: np.random.exponential(scale=19.988775280898874)
ip123_dist = lambda: np.random.exponential(scale=19.988775280898874)
ip103_dist = lambda: np.random.exponential(scale=85.76111111111112)
ip106_dist = lambda: np.random.exponential(scale=85.76111111111112)
ip112_dist = lambda: np.random.exponential(scale=85.76111111111112)

ip101_dest_dist = lambda: np.random.choice([39, 40, 38, 28, 18, 19, 8, 8], p=[0.09375, 0.7083333333333334, 0.03125, 0.020833333333333332, 0.03125, 0.0625, 0.041666666666666664, 0.010416666666666666])
ip102_dest_dist = lambda: np.random.choice([39, 40, 38, 28, 18, 19, 8, 8], p=[0.125, 0.59375, 0.03125, 0.03125, 0.03125, 0.0625, 0.0625, 0.0625])
ip123_dest_dist = lambda: np.random.choice([39, 40, 38, 28, 18, 19, 8, 8], p=[0.09375, 0.5625, 0.0625, 0.03125, 0.03125, 0.03125, 0.09375, 0.09375])
ip103_dest_dist = lambda: np.random.choice([29, 30, 28, 18, 8, 9], p=[0.166, 0.17, 0.166, 0.166, 0.166, 0.166])
ip106_dest_dist = lambda: np.random.choice([19, 20, 18, 8], p=[0.25, 0.25, 0.25, 0.25])
ip112_dest_dist = lambda: np.random.choice([9, 10, 8], p=[0.33, 0.33, 0.34])

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

