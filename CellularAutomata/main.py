
import time
from road import Peachtree

def main():
    print("program start");

    peachtree = Peachtree()

    for t in range(1000):
        # print("time", t)
        peachtree.update();
        time.sleep(0.05)
        print(peachtree)





if __name__ == "__main__":
    main()
