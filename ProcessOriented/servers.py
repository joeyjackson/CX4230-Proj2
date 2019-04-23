from threading import Lock
from constants import *


# *************************************************
#   ROAD
# *************************************************
class Lane:
    def __init__(self, length, next_lane, pass_colors):
        self.lock = Lock()
        self.q = []
        self.length = length
        self.back_position = 0
        self.next = next_lane  # (road, lane) or None
        self.pass_colors = pass_colors  # GREEN OR L_GREEN if left turn lane

    def back_pos(self):
        self.lock.acquire()
        to_return = self.back_position
        self.lock.release()
        return to_return

    def schedule(self):
        self.lock.acquire()
        self.back_position += car_length
        self.lock.release()

    def unschedule(self):
        self.lock.acquire()
        self.back_position -= car_length
        self.lock.release()

    def enter(self, vehicle):
        self.lock.acquire()
        self.q.append(vehicle)
        self.lock.release()

    def exit(self, vehicle):
        self.lock.acquire()
        self.q.remove(vehicle)
        self.back_position -= car_length
        self.lock.release()

    def is_empty(self):
        self.lock.acquire()
        to_return = len(self.q) == 0
        self.lock.release()
        return to_return

    def is_open(self):
        self.lock.acquire()
        to_return = self.back_position + car_length <= self.length
        self.lock.release()
        return to_return


class RoadSegment:
    def __init__(self, lanes, traffic_light):
        self.lock = Lock()
        self.lanes = lanes
        self.traffic_light = traffic_light
