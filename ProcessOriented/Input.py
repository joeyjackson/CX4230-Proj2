from processes import Vehicle
from engine import Event, Process, wait_until, advance_time, schedule_future_event, current_time, StartProcessEvent
from processes import TrafficLight, NoLight
from servers import RoadSegment, Lane
from conditions import LightIsColorCondition
from constants import *


class EnterRoadEvent(Event):
    def __init__(self, destination, road, lane, tracked):
        self.destination = destination
        self.road = road
        self.lane = lane
        self.tracked = tracked
        self.v = None

    def handle(self):
        self.v = Vehicle(self.destination, self.road, self.lane, current_time(), self.tracked)
        self.v.start()

    def message(self, ts):
        pass  # print(round(ts, 2), "\t", self.v, "entered road", self.road, "in lane", self.lane)


class InputProcess(Process):
    def __init__(self, road, iat_dist, dest_dist, lane_dist, traffic_light, pass_colors, tracked):
        super().__init__()
        self.road = road
        self.iat_dist = iat_dist
        self.dest_dist = dest_dist
        self.lane_dist = lane_dist
        self.traffic_light = traffic_light
        self.pass_colors = pass_colors
        self.tracked = tracked

    def run(self):
        while True:
            self.cv.acquire()
            iat = max(0, self.iat_dist())
            destination = self.dest_dist()

            lane = self.lane_dist()
            tracked = self.tracked and destination >= 20

            if self.road.lanes[lane].is_open():
                schedule_future_event(EnterRoadEvent(destination, self.road, lane, tracked), iat)
            advance_time(self, iat)
            wait_until(LightIsColorCondition(self, self.traffic_light, self.pass_colors))


def initialize_simulation():
    # *************************************************
    #   CREATE SERVERS
    # *************************************************
    t1 = TrafficLight(seq10)
    t1E = TrafficLight(seq10E)
    t2 = TrafficLight(seq11)
    t3 = TrafficLight(seq12)
    t4 = NoLight()
    t5 = TrafficLight(seq14)

    road4 = RoadSegment(
        [
            Lane(100, None, [LightState.L_GREEN]),
            Lane(100, None, [LightState.GREEN]),
            Lane(100, None, [LightState.GREEN])
        ],
        t5
    )

    road3 = RoadSegment(
        [
            Lane(75, (road4, 0), [LightState.GREEN]),
            Lane(110, (road4, 1), [LightState.GREEN]),
            Lane(110, (road4, 2), [LightState.GREEN])
        ],
        t4
    )

    road2 = RoadSegment(
        [
            Lane(45, None, [LightState.GREEN]),
            Lane(120, (road3, 1), [LightState.GREEN]),
            Lane(120, (road3, 2), [LightState.GREEN])
        ],
        t3
    )

    road1 = RoadSegment(
        [
            Lane(30, None, [LightState.L_GREEN]),
            Lane(125, (road2, 1), [LightState.GREEN]),
            Lane(125, (road2, 2), [LightState.GREEN])
        ],
        t2
    )

    # *************************************************
    #   INITIALIZE PROCESSES
    # *************************************************
    schedule_future_event(StartProcessEvent(t1), 0)
    schedule_future_event(StartProcessEvent(t1E), 0)
    schedule_future_event(StartProcessEvent(t2), 0)
    schedule_future_event(StartProcessEvent(t3), 0)
    schedule_future_event(StartProcessEvent(t4), 0)
    schedule_future_event(StartProcessEvent(t5), 0)

    # *************************************************
    #   SCHEDULE INPUT EVENTS
    # *************************************************
    ip101 = InputProcess(road1, ip101_dist, ip101_dest_dist, ip101_lane_dist, t1, [LightState.GREEN], True)
    schedule_future_event(StartProcessEvent(ip101), 0)
    ip102 = InputProcess(road1, ip102_dist, ip102_dest_dist, ip102_lane_dist, t1, [LightState.RED], True)
    schedule_future_event(StartProcessEvent(ip102), 0)
    ip123 = InputProcess(road1, ip123_dist, ip123_dest_dist, ip123_lane_dist, t1E, [LightState.L_GREEN], True)
    schedule_future_event(StartProcessEvent(ip123), 0)

    ip103 = InputProcess(road2, ip103_dist, ip103_dest_dist, ip103_lane_dist, t2, [LightState.RED], False)
    schedule_future_event(StartProcessEvent(ip103), 0)

    ip106 = InputProcess(road3, ip106_dist, ip106_dest_dist, ip106_lane_dist, t3, [LightState.RED], False)
    schedule_future_event(StartProcessEvent(ip106), 0)

    ip112 = InputProcess(road4, ip112_dist, ip112_dest_dist, ip112_lane_dist, t4, [LightState.GREEN], False)
    schedule_future_event(StartProcessEvent(ip112), 0)
