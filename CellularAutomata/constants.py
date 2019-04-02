from tiles import Intersection

v_max = 1
arrival_rate = 0.1


peachTreeMap = [
    ["ILO", "IS", "IR"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["IS", "IS", "IR"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["S", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["ILO", "IS", "IR"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["ILO", "IS", "IR"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["L", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"],
    ["X", "S", "S"]
][::-1]

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

road_width = len(peachTreeMap[0])
road_length = len(peachTreeMap)

ixns = [
    {
        "i":10,
        "lights": ["g", "y", "r", "G", "Y", "R"],
        "times": [7, 4, 2, 35, 4, 50]
    },
    {
        "i":21,
        "lights": ["G", "Y", "R"],
        "times": [42, 3, 55]
    },
    {
        "i":34,
        "lights": ["G", "Y", "R"],
        "times": [61, 3, 36]
    },
    {
        "i":47,
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
