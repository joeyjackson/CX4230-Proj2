from enum import Enum


class LightState(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2
    L_GREEN = 3
    L_YELLOW = 4
    L_RED = 5

# 10th and Peachtree
seq10 = [
    (LightState.L_GREEN, 7),
    (LightState.L_YELLOW, 3.6),
    (LightState.L_RED, 2.2),
    (LightState.GREEN, 34.7),
    (LightState.YELLOW, 3.6),
    (LightState.RED, 49.3)
]

# 11th and Peachtree
seq11 = [
    (LightState.GREEN, 41.5),
    (LightState.YELLOW, 3.2),
    (LightState.RED, 55.4)
]

# 12th and Peachtree
seq12 = [
    (LightState.GREEN, 60.9),
    (LightState.YELLOW, 3.2),
    (LightState.RED, 35.7)
]

# 14th and Peachtree
seq14 = [
    (LightState.L_GREEN, 8.8),
    (LightState.L_YELLOW, 3.6),
    (LightState.L_RED, 3.6),
    (LightState.GREEN, 34.6),
    (LightState.YELLOW, 3.2),
    (LightState.RED, 46.1)
]

reaction_time = 1.5
car_length = 20
