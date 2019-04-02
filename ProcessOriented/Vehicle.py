from threading import Thread, Condition
import random
from Constants import *
from Engine import *
from Events import *
from ConditionRegistry import *


class Vehicle(Thread):
    def __init__(self, road, lane=0):
        super().__init__()
        self.speed = random.randint(15, 20) * 0.44704  # Feet per second
        self.destination = None
        self.cv = Condition()
        self.road = road
        self.lane = lane
        self.road.enter(self, lane)
        self.reached_destination = False

    def run(self):
        self.cv.acquire()
        while not self.reached_destination:
            while self.road.traffic_light.light() != LightState.GREEN:
                wait_until(WaitCondition(self))

            advance_time(MoveThroughIntersectionEvent(self), 0)
                         # self.road.lanes[self.lane].length / self.speed)
            self.cv.wait()
            # if traffic,
            #   enter traffic queue
            #   waitUntil(traffic continue)
            # if light is green:
            #   waitUntil(light is red, through intersection)
            #   if light is red
            #      waitUntil(traffic continue)

            # self.reached_destination = True

        self.cv.release()
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