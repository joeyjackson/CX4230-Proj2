from Engine import advance_time, fel
from threading import Thread
from Events import LightChangeEvent


class TrafficLight(Thread):
    def __init__(self, sequence, road):
        super().__init__()
        self.sequence = sequence
        self.state = 0
        self.road = road
        self.road.traffic_light = self

    def light(self):
        return self.sequence[self.state][0]

    def change(self):
        self.state = (self.state + 1) % len(self.sequence)
        _, duration = self.sequence[self.state]
        advance_time(LightChangeEvent(self), duration)
        # print(fel.current_time, self.sequence[self.state][0])

    def run(self):
        _, duration = self.sequence[self.state]
        advance_time(LightChangeEvent(self), duration)



