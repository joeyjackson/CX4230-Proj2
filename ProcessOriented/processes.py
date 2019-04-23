from engine import *
from conditions import *
from constants import *
from output import *


# *************************************************
#   TRAFFIC LIGHT
# *************************************************
class TrafficLight(Process):
    def __init__(self, sequence):
        super().__init__()
        self.sequence = sequence
        self.state = 0

    def light(self):
        self.cv.acquire()
        l = self.sequence[self.state][0]
        self.cv.release()
        return l

    def run(self):
        self.cv.acquire()

        while True:
            color, duration = self.sequence[self.state]
            # print(fel.current_time, '\t', color)
            advance_time(self, duration)
            self.state = (self.state + 1) % len(self.sequence)


# *************************************************
#   VEHICLE
# *************************************************
class Vehicle(Process):
    def __init__(self, destination, road, lane, start_time, tracked=True):
        super().__init__()
        self.speed = car_speed
        self.destination = destination
        self.road = road
        self.lane = lane
        self.start_time = start_time
        self.tracked = tracked

    def run(self):
        self.cv.acquire()
        while self.destination >= 0:

            if self.destination < 10:
                if self.destination % 2 == 0:  # Turn Right
                    self.lane = 2
                    wait_until(LaneOpenCondition(self, self.road, self.lane))
                else:  # Turn Left
                    if self.lane == 2:
                        self.lane = 1
                        wait_until(LaneOpenCondition(self, self.road, self.lane))
                    lt_lane = self.road.lanes[0]
                    curr_lane = self.road.lanes[self.lane]
                    curr_lane.schedule()
                    advance_time(self, (curr_lane.length - lt_lane.length) / self.speed)
                    curr_lane.enter(self)
                    wait_until(LaneOpenCondition(self, self.road, 0))
                    curr_lane.exit(self)
                    self.lane = 0

            curr_lane = self.road.lanes[self.lane]

            # Drive to traffic
            rem = curr_lane.back_pos()
            curr_lane.schedule()
            advance_time(self, (curr_lane.length - rem) / self.speed)

            # If there is traffic, enter it
            was_empty = curr_lane.is_empty()
            if not was_empty:
                curr_lane.enter(self)
                wait_until(FrontOfLaneCondition(self, curr_lane))
                advance_time(self, reaction_time)

            if self.destination >= 10:
                next_lane = curr_lane.next
            else:
                next_lane = None

            if was_empty:
                curr_lane.enter(self)
            wait_until(CanMoveThroughIntersectionCondition(self, self.road, curr_lane, next_lane))
            curr_lane.exit(self)

            # print(fel.current_time, '\t', self.road.traffic_light.light())

            if next_lane is None:
                break
            else:
                self.road, self.lane = next_lane

            self.destination -= 10

        if self.tracked:
            output_record.record(fel.current_time - self.start_time)

        # print(fel.current_time, "Exit")
        self.finish()
