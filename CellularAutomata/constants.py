from tiles import Intersection

car_lifespans = []

v_max = 1
arrival_rate = 0.02


peachTreeMap = [["ILO", "IS", "IR"]]
peachTreeMap += [["L", "S", "S"] for _ in range(20)]
peachTreeMap += ["IS", "IS", "IR"],
peachTreeMap += [["S", "S", "S"] for _ in range(15)]
peachTreeMap += [["X", "S", "S"] for _ in range(5)]
peachTreeMap += ["ILO", "IS", "IR"],
peachTreeMap += [["L", "S", "S"] for _ in range(9)]
peachTreeMap += [["X", "S", "S"] for _ in range(15)]
peachTreeMap += ["ILO", "IS", "IR"],
peachTreeMap += [["L", "S", "S"] for _ in range(6)]
peachTreeMap += [["X", "S", "S"] for _ in range(19)]
peachTreeMap = peachTreeMap[::-1]
# print(peachTreeMap)

# laneChangeLeft = {
#     "map": [
#         ["X", "", ""],
#         ["X", "", ""],
#         ["X", "", ""],
#         ["X", "", ""],
#         ["X", "*", ""],
#     ],
#     pos: ()
# }

road_width = 3
road_length = len(peachTreeMap)

ixns = [
    # { #10th
    #     "i":1,
    #     "lights": ["g", "y", "r", "G", "Y", "R"],
    #     "times": [7, 4, 2, 35, 4, 50]
    # },
    { #11th
        "i":25,
        "lights": ["g", "y", "r"],
        "times": [42, 3, 55]
    },
    { # 12th
        "i":50,
        "lights": ["g", "y", "r"],
        "times": [61, 3, 36]
    },
    { # 13th
        "i":76,
        "lights": ["g"],
        "times": [100]
    },
    { # 14th
        "i":92,
        "lights": ["g", "y", "r", "G", "Y", "R"],
        "times": [9, 4, 4, 35, 4, 46]
    }
]
n_ixns = len(ixns)

spawns = [
    { #10th eastbound 123
        "lights": ["R", "x", "G", "Y"],
        "times": [55, 10, 30, 5],
        "coords": (0, 2),
        "beta": 19.99
    },
    { #10th northbound 101
        "lights": ["G", "Y", "R", "x"],
        "times": [35, 4, 50, 10],
        "coords": (0, 2),
        "beta": 6.47
    },
    { #10th westbound 102
        "lights": ["R", "x", "G", "Y"],
        "times": [87, 5, 4, 4],
        "coords": (0, 1),
        "beta": 19.99
    },
    { #11th eastbound 122
        "lights": ["R", "G", "Y"],
        "times": [76, 4, 20],
        "coords": (26, 1),
        "beta": 85.76
    },
    { #11th westbound 103
        "lights": ["R", "G", "Y"],
        "times": [76, 4, 20],
        "coords": (26, 1),
        "beta": 85.76
    },
    { #12th eastbound 121
        "lights": ["R", "G", "Y"],
        "times": [69, 4, 27],
        "coords": (51, 1),
        "beta": 85.76
    },
    { #12th westbound 106
        "lights": ["R", "G", "Y"],
        "times": [69, 4, 27],
        "coords": (51, 1),
        "beta": 85.76
    },
    { #12th westbound 112
        "lights": ["G"],
        "times": [100],
        "coords": (76, 1),
        "beta": 85.76
    }
]

light_times = {
    "G": 4,
    "Y": 2,
    "R": 6
}

dests_side = ["L", "S", "R"]
dests_side_to_dir = {
    "L": -1,
    "S": 0,
    "R": 1
}
dests_side_to_lane = {
    "L": 0,
    "S": 1,
    "R": 2
}
