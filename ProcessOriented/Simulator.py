from TrafficLight import TrafficLight
from RoadSegment import RoadSegment, Lane
from Vehicle import Vehicle
from Engine import *
from Constants import *
from Events import *


if __name__ == '__main__':
    rd = RoadSegment([Lane(100), Lane(100)], None)

    TrafficLight(seq11, rd).start()

    advance_time(EnterRoadEvent(rd, 0), 42)
    # advance_time(EnterRoadEvent(rd, 1), 0)
    # advance_time(EnterRoadEvent(rd, 0), 20)

    # TrafficLight(seq11, None).start()
    # TrafficLight(seq12, None).start()
    # TrafficLight(seq14, None).start()

    count = 0
    while not fel.is_empty() and fel.current_time < 200:
        ts, evt = fel.pop()
        evt.execute()
        evt.message(ts)
        reg.check()
        count += 1

    print(rd.lanes[0].light_q)

