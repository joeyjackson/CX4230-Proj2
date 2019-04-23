from engine import WaitCondition


class LightIsColorCondition(WaitCondition):
    def __init__(self, thread, light, colors):
        super().__init__(thread)
        self.light = light
        self.colors = colors

    def __call__(self):
        return self.light.light() in self.colors


class FrontOfLaneCondition(WaitCondition):
    def __init__(self, thread, lane):
        super().__init__(thread)
        self.thread = thread
        self.lane = lane

    def __call__(self):
        return len(self.lane.q) > 0 and self.lane.q[0] == self.thread


class CanMoveThroughIntersectionCondition(WaitCondition):
    def __init__(self, thread, road, curr_lane, next_lane):
        super().__init__(thread)
        self.light = road.traffic_light
        if next_lane is None:
            self.next_lane = None
        else:
            self.next_road, self.next_lane = next_lane
        self.colors = curr_lane.pass_colors

    def __call__(self):
        return self.light.light() in self.colors and (self.next_lane is None
                                                      or self.next_road.lanes[self.next_lane].is_open())


class LaneOpenCondition(WaitCondition):
    def __init__(self, thread, road, lane):
        super().__init__(thread)
        self.lane = road.lanes[lane]

    def __call__(self):
        return self.lane.is_open()


class WaitForever(WaitCondition):
    def __init__(self, thread):
        super().__init__(thread)

    def __call__(self):
        return False
