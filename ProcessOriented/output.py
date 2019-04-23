from threading import Lock
from matplotlib import pyplot as plt
import numpy as np
from engine import current_time


class Record:
    def __init__(self):
        self.lock = Lock()
        self.pts = []
        self.rtime = 0

    def set_record_time(self, time):
        self.lock.acquire()
        self.rtime = time
        self.lock.release()

    def record(self, x):
        self.lock.acquire()
        if current_time() >= self.rtime:
            self.pts.append(x)
        self.lock.release()

    def done(self):
        self.lock.acquire()
        self.pts = np.array(self.pts)
        self.lock.release()

    def show(self, bins=None):
        self.lock.acquire()
        plt.hist(self.pts, bins=bins)
        plt.show()
        self.lock.release()

    def average(self, end='\n'):
        self.lock.acquire()
        print(np.mean(self.pts), end=end)
        self.lock.release()

    def reset(self):
        self.lock.acquire()
        self.pts = []
        self.lock.release()


output_record = Record()
