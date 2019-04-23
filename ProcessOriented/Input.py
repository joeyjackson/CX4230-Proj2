from engine import *
from servers import *
from constants import *
from processes import *
import random


class EnterRoadEvent(Event):
    def __init__(self, destination, road, lane, tracked):
        self.destination = destination
        self.road = road
        self.lane = lane
        self.tracked = tracked
        self.v = None

    def handle(self):
        self.v = Vehicle(self.destination, self.road, self.lane, fel.current_time, self.tracked)
        self.v.start()

    def message(self, ts):
        pass  # print(round(ts, 2), "\t", self.v, "entered road", self.road, "in lane", self.lane)


class InputProcess(Process):
    def __init__(self, road, iat, stddev, traffic_light, pass_colors, tracked):
        super().__init__()
        self.road = road
        self.iat = iat
        self.stddev = stddev
        self.traffic_light = traffic_light
        self.pass_colors = pass_colors
        self.tracked = tracked

    def run(self):
        while True:
            self.cv.acquire()
            iat = max(0, random.gauss(self.iat, self.stddev))

            destination = random.randint(0, 30)
            lane = random.randint(1, 2)
            tracked = self.tracked and destination >= 20

            if self.road.lanes[lane].is_open():
                schedule_future_event(EnterRoadEvent(destination, self.road, lane, tracked), iat)
            advance_time(self, iat)
            wait_until(LightIsColorCondition(self, self.traffic_light, self.pass_colors))


def initialize_simulation():
    # *************************************************
    #   CREATE SERVERS
    # *************************************************
    t0 = TrafficLight(seq10)
    t1 = TrafficLight(seq11)
    t2 = TrafficLight(seq12)
    t3 = TrafficLight(seq14)

    road3 = RoadSegment(
        [
            Lane(175, None, [LightState.L_GREEN]),
            Lane(210, None, [LightState.GREEN]),
            Lane(210, None, [LightState.GREEN])
        ],
        t3
    )

    road2 = RoadSegment(
        [
            Lane(45, None, [LightState.GREEN]),
            Lane(120, (road3, 1), [LightState.GREEN]),
            Lane(120, (road3, 2), [LightState.GREEN])
        ],
        t2
    )

    road1 = RoadSegment(
        [
            Lane(30, None, [LightState.L_GREEN]),
            Lane(125, (road2, 1), [LightState.GREEN]),
            Lane(125, (road2, 2), [LightState.GREEN])
        ],
        t1
    )

    # *************************************************
    #   INITIALIZE PROCESSES
    # *************************************************
    schedule_future_event(StartProcessEvent(t0), 0)
    schedule_future_event(StartProcessEvent(t1), 0)
    schedule_future_event(StartProcessEvent(t2), 0)
    schedule_future_event(StartProcessEvent(t3), 0)

    # *************************************************
    #   SCHEDULE INPUT EVENTS
    # *************************************************
    ip1 = InputProcess(road1, 4, 2, t0, [LightState.GREEN], True)
    schedule_future_event(StartProcessEvent(ip1), 0)

    ip2 = InputProcess(road2, 16, 8, t1, [LightState.RED], False)
    schedule_future_event(StartProcessEvent(ip2), 0)

    ip3 = InputProcess(road3, 16, 8, t2, [LightState.RED], False)
    schedule_future_event(StartProcessEvent(ip3), 0)

    # schedule_future_event(EnterRoadEvent(23, road1, 1, True), 0)
    # schedule_future_event(EnterRoadEvent(25, road1, 1, True), 2)
    # schedule_future_event(EnterRoadEvent(50, road3, 1, True), 74)
    # schedule_future_event(EnterRoadEvent(50, road3, 1, True), 76)
    # schedule_future_event(EnterRoadEvent(50, road3, 1, True), 78)