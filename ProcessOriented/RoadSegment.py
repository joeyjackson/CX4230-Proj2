from threading import Lock


class Lane:
    def __init__(self, length):
        self.length = length
        self.light_q = []
        self.traffic_q_pos = 0
        self.traffic_q = []


class RoadSegment:
    def __init__(self, lanes, lt_lane):
        self.lock = Lock()
        self.left_turn_lane = lt_lane
        self.lanes = lanes
        self.traffic_light = None

    def enter(self, vehicle, lane=0):
        self.lock.acquire()
        self.lanes[lane].light_q.append(vehicle)
        self.lock.release()

    def exit(self, lane=0):
        self.lock.acquire()
        v = self.lanes[lane].light_q.pop(0)
        self.lock.release()
        return v
