
import time
import matplotlib.pyplot as plt
import constants as c
from road import Peachtree

def main():
    print("program start");

    peachtree = Peachtree()

    dt = 0.5
    for t in range(4000):
        # print("time", t)
        peachtree.update(dt);
        # time.sleep(0.001)
        print(peachtree)

    # plt.hist(c.car_lifespans)
    # plt.show()





if __name__ == "__main__":
    main()
