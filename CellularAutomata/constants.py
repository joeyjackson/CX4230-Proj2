from tiles import Intersection

car_lifespans = []

v_max = 1
arrival_rate = 0.1


peachTreeMap = [["ILO", "IS", "IR"]]
peachTreeMap += [["L", "S", "S"] for _ in range(10)]
peachTreeMap += [["S", "S", "S"] for _ in range(60)]
peachTreeMap += ["IS", "IS", "IR"],
peachTreeMap += [["S", "S", "S"] for _ in range(49)]
peachTreeMap += [["X", "S", "S"] for _ in range(10)]
peachTreeMap += ["ILO", "IS", "IR"],
peachTreeMap += [["L", "S", "S"] for _ in range(10)]
peachTreeMap += [["X", "S", "S"] for _ in range(47)]
peachTreeMap += ["ILO", "IS", "IR"],
peachTreeMap += [["L", "S", "S"] for _ in range(10)]
peachTreeMap += [["X", "S", "S"] for _ in range(46)]
peachTreeMap = peachTreeMap[::-1]
print(peachTreeMap)

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
    {
        "i":56,
        "lights": ["g", "y", "r", "G", "Y", "R"],
        "times": [7, 4, 2, 35, 4, 50]
    },
    {
        "i":114,
        "lights": ["G", "Y", "R"],
        "times": [42, 3, 55]
    },
    {
        "i":174,
        "lights": ["G", "Y", "R"],
        "times": [61, 3, 36]
    },
    {
        "i":245,
        "lights": ["g", "y", "r", "G", "Y", "R"],
        "times": [9, 4, 4, 35, 4, 46]
    }
]
n_ixns = len(ixns)

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
