from threading import Thread, Lock, Condition
import heapq


# *************************************************
#   EVENTS
# *************************************************


class Event:
    def __gt__(self, evt):
        return False

    def handle(self):
        pass

    def message(self, ts):
        print("", end="")


class StartProcessEvent(Event):
    def __init__(self, process):
        self.p = process

    def handle(self):
        self.p.start()

    def message(self, ts):
        print("Started Process", ts)


class ResumeEvent(Event):
    def __init__(self, process):
        self.p = process

    def handle(self):
        self.p.resume()
        scv.wait()

    def message(self, ts):
        print("Process Resumed", ts)


class FutureEventList:
    def __init__(self):
        self.current_time = 0
        self.pq = []
        self.lock = Lock()

    def push(self, evt, time):
        self.lock.acquire()
        ts = self.current_time + time
        heapq.heappush(self.pq, (ts, evt))
        self.lock.release()

    def pop(self):
        self.lock.acquire()
        ts, evt = heapq.heappop(self.pq)
        self.current_time = ts
        self.lock.release()
        return ts, evt

    def remove(self, evt):
        self.lock.acquire()
        for i, (ts, e) in enumerate(self.pq):
            if e == evt:
                self.pq.pop(i)
                self.lock.release()
                return
        self.lock.release()
        raise Exception("Event Not Found")

    def is_empty(self):
        self.lock.acquire()
        empty = len(self.pq) == 0
        self.lock.release()
        return empty


# *************************************************
#   CONDITIONS
# *************************************************


class WaitCondition:
    def __init__(self, thread):
        self.thread = thread

    def __call__(self):
        return True


class Registry:
    def __init__(self):
        self.lock = Lock()
        self.registry = []

    def register(self, wait_condition):
        self.lock.acquire()
        self.registry.append(wait_condition)
        self.lock.release()

    def check(self):
        self.lock.acquire()
        temp = self.registry[:]
        self.registry.clear()

        for condition in temp:
            if condition():
                self.lock.release()
                condition.thread.resume()
                self.lock.acquire()
                scv.wait()
            else:
                self.registry.append(condition)

        self.lock.release()


# *************************************************
#   PROCESSES
# *************************************************


class Process(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.cv = Condition()
        self.count = 0

    def start(self):
        super().start()
        scv.wait()

    def run(self):
        self.cv.acquire()

        schedule_future_event(StartProcessEvent(Process()), 40)

        self.finish()

    def resume(self):
        self.cv.acquire()
        self.cv.notify()
        self.cv.release()

    def finish(self):
        resume_scheduler()


# *************************************************
#   SCHEDULER
# *************************************************


class Scheduler:
    def __init__(self, future_event_list, registry):
        self.cv = Condition()
        self.fel = future_event_list
        self.reg = registry
        self.cv.acquire()

    def run(self):
        while not self.fel.is_empty() and self.fel.current_time < 200:
            ts, evt = self.fel.pop()
            evt.handle()
            evt.message(ts)

            self.reg.check()


# *************************************************
#   ENGINE
# *************************************************
reg = Registry()
fel = FutureEventList()
scheduler = Scheduler(fel, reg)
scv = scheduler.cv


def schedule_future_event(evt, time):
    fel.push(evt, time)


def advance_time(thread, time):
    fel.push(ResumeEvent(thread), time)
    resume_scheduler()
    thread.cv.wait()


def wait_until(condition):
    reg.register(condition)
    resume_scheduler()
    condition.thread.cv.wait()


def wait_until_timeout(condition, duration):
    pass


def resume_scheduler():
    scv.acquire()
    scv.notify()
    scv.release()


# *************************************************
#   Simulator
# *************************************************
if __name__ == '__main__':
    schedule_future_event(StartProcessEvent(Process()), 10)
    schedule_future_event(StartProcessEvent(Process()), 20)
    schedule_future_event(StartProcessEvent(Process()), 30)
    schedule_future_event(StartProcessEvent(Process()), 40)

    scheduler.run()