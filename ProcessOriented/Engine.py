from FutureEventList import FutureEventList
from ConditionRegistry import Registry

fel = FutureEventList()
reg = Registry()


def advance_time(evt, duration):
    fel.push(evt, duration)


def wait_until(condition):
    reg.register(condition)
    condition.thread.cv.wait()


def wait_until_timeout(condition, duration):
    # TODO
    pass


