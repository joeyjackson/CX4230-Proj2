from Engine import advance_time, fel
from threading import Thread, Lock
from Events import LightChangeEvent


class TrafficLight(Thread):
    def __init__(self, sequence, road):
        super().__init__(daemon=True)
        self.lock = Lock()
        self.sequence = sequence
        self.state = 0
        self.road = road
        self.road.traffic_light = self

    def light(self):
        self.lock.acquire()
        l = self.sequence[self.state][0]
        self.lock.release()
        return l

    def change(self):
        self.lock.acquire()
        self.state = (self.state + 1) % len(self.sequence)
        _, duration = self.sequence[self.state]
        advance_time(LightChangeEvent(self), duration)
        # print(fel.current_time, self.sequence[self.state][0])
        self.lock.release()

    def run(self):
        self.lock.acquire()
        _, duration = self.sequence[self.state]
        advance_time(LightChangeEvent(self), duration)
        self.lock.release()



