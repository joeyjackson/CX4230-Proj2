class Event:
    def __gt__(self, evt):
        return False

    def handle(self):
        pass

    def message(self, ts):
        print("", end="")


class EnterRoadEvent(Event):
    def __init__(self, road, lane):
        self.road = road
        self.lane = lane
        self.v = None

    def handle(self):
        from Vehicle import Vehicle
        self.v = Vehicle(self.road, self.lane)
        self.v.start()

    def message(self, ts):
        print(round(ts, 2), "\t", self.v, "entered road", self.road, "in lane", self.lane)


class LightChangeEvent(Event):
    def __init__(self, traffic_light):
        self.traffic_light = traffic_light

    def handle(self):
        self.traffic_light.change()

    def message(self, ts):
        print(round(ts, 2), "\t", self.traffic_light, "changed to", self.traffic_light.light())


class MoveThroughIntersectionEvent(Event):
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.v = None

    def handle(self):
        self.vehicle.cv.acquire()
        self.v = self.vehicle.road.exit(self.vehicle.lane)
        self.vehicle.reached_destination = True
        self.vehicle.cv.notify()
        self.vehicle.cv.release()

    def message(self, ts):
        print(round(ts, 2), "\t", self.v, "has exited lane", self.v.lane, "from road", self.vehicle.road)


class MoveEvent(Event):
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def handle(self):
        self.vehicle.cv.acquire()
        self.vehicle.cv.notify()
        self.vehicle.cv.release()

    def message(self, ts):
        print(round(ts, 2), "\t", self.vehicle, "has moved down road", self.vehicle.road)

