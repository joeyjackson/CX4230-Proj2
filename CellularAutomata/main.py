import time
import matplotlib.pyplot as plt
import numpy as np
import constants as c
import scipy.stats
from tqdm import tqdm
from road import Peachtree

np.random.seed(1337);

def main():
    print("program start");

    means = []

    for run in tqdm(range(3)):
        peachtree = Peachtree()
        c.car_lifespans = []

        rows = []

        dt = 0.05
        for t in (range(int(1000/dt))):
            # print("time", t)
            peachtree.update(dt);
            # time.sleep(0.001)
            # print(peachtree)
            # rows.append(peachtree.getVisRow())

        # plt.imshow(rows[-4000::10])
        print("ARRIVAL TIME \n ---------")
        mean = np.mean(c.car_lifespans)
        print("Mean  ", mean)
        print("StDev ", np.std(c.car_lifespans))
        # plt.hist(c.car_lifespans, bins=20)
        # plt.show()
        means.append(mean)

    print("ARRIVAL TIME ACROSS RUNSS \n ---------")
    print("Mean of Means ", np.mean(mean))
    print("StDev of Means", np.std(mean))
    m, ml, mh = mean_confidence_interval((means), 0.95)
    print("95% confidence interval")
    print("mean: ", m)
    print("low:  ", ml)
    print("high: ", mh)

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h




if __name__ == "__main__":
    main()
