from threading import Thread, Lock, Condition


class WaitCondition:
    def __init__(self, thread):
        # print("created")
        self.thread = thread

    def check(self):
        self.thread.cv.acquire()
        self.thread.cv.notify()
        self.thread.cv.release()
        # print("checked")
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
        temp = []
        for cond in self.registry:
            satisfied = cond.check()
            if not satisfied:
                temp.append(cond)
        self.registry = temp
        self.lock.release()

