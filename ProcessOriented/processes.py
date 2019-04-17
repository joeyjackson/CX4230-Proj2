from engine import *
from events import *
from conditions import *
from constants import *
import random


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
            print(fel.current_time, '\t', color)
            advance_time(self, duration)
            self.state = (self.state + 1) % len(self.sequence)

        # self.finish()


# *************************************************
#   VEHICLE
# *************************************************
class Vehicle(Process):
    def __init__(self, road, lane=0):
        super().__init__()
        self.speed = random.randint(15, 20) * 0.44704  # Feet per second
        self.destination = 50
        self.road = road
        self.lane = lane
        self.road.enter(self, lane)
        self.reached_destination = False

    def run(self):
        self.cv.acquire()
        while not self.reached_destination:

            advance_time(self, self.road.lanes[self.lane].length / self.speed)
            wait_until(LightIsColorCondition(self, self.road.traffic_light, [LightState.GREEN]))

            # if traffic,
            #   enter traffic queue
            #   waitUntil(traffic continue)
            # if light is green:
            #   waitUntil(light is red, through intersection)
            #   if light is red
            #      waitUntil(traffic continue)

            self.reached_destination = True
            print(fel.current_time, '\t', "Through Intersection")

        self.finish()
        """
        Enter Road Segment (List/Queue) if space
            Enter Back Moving Queue

        If destination = straight:
            Move to most open lane (excluding turn lane)
        else if destination = left:
            Move to left/turn lane
        else (destination = right):
            Move to right lane

        If stopped queue not isEmpty:
            AdvanceTime(Distance to Back of stoppedQueue / speed)
            Add to stopped queue
            WaitUntil(Front of stopped queue)
            AdvanceTime(Reaction Time)
            Dequeue from stopped queue

        while (not moved to next segment):
            WaitUntil(Light Changes to red, (Segment Length - Progress) * SpeedConst
                + Reaction delay (place in queue))
            if (light changes to red):
                move to next segment
            else (time expires):
                add to light stopped queue
                WaitUntil(Light changes to green)
        """
        pass

