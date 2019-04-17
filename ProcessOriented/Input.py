from engine import *
from events import *
from servers import *
from constants import *
from processes import *

tl = TrafficLight(seq10)
road = RoadSegment([Lane(100)], None, tl)


def initialize_simulation():
    schedule_future_event(StartProcessEvent(tl), 0)

    schedule_future_event(EnterRoadEvent(road, 0), 110)

