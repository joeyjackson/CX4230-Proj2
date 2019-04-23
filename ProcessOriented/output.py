from threading import Lock
from matplotlib import pyplot as plt


class Record:
    def __init__(self):
        self.lock = Lock()
        self.pts = []

    def record(self, x):
        self.lock.acquire()
        self.pts.append(x)
        self.lock.release()

    def show(self):
        self.lock.acquire()
        plt.hist(self.pts)
        plt.show()
        self.lock.release()


output_record = Record()
