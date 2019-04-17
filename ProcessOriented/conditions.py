from engine import *
from constants import *


class LightIsColorCondition(WaitCondition):
    def __init__(self, thread, light, colors):
        super().__init__(thread)
        self.light = light
        self.colors = colors

    def __call__(self):
        return self.light.light() in self.colors


class FrontOfQueueCondition(WaitCondition):
    def __init__(self, thread, q):
        super().__init__(thread)
        self.q = q

    def __call__(self):
        return len(self.q) > 0 and self.q[0] is self.thread
