import heapq
import threading


class FutureEventList:
    def __init__(self):
        self.current_time = 0
        self.pq = []
        self.lock = threading.Lock()

    def push(self, evt, duration):
        self.lock.acquire()
        ts = self.current_time + duration
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
