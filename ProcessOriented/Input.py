from threading import Lock, Thread, Condition


class InputQueue(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.lock = Lock()
        self.cv = Condition(self.lock)
        self.q = []

    def push(self, vehicle):
        self.cv.acquire()
        self.q.append(vehicle)
        self.cv.notify()
        self.cv.release()

    def pop(self):
        self.lock.acquire()
        if len(self.q) > 0:
            p = self.q.pop(0)
        else:
            p = None
        self.lock.release()
        return p

    def run(self):
        while True:
            self.cv.acquire()
            if len(self.q) == 0:
                self.cv.wait()
            else:
                pass
            self.cv.release()


