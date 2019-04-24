from engine import *
import time
from constants import *
import numpy as np
import scipy.stats

#You will need to uncomment these for historgrams
# import matplotlib.pyplot as plt




list_avetime = []
list_passed = []

#Confidence interval function
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

#If you want to put data to excel
def writeData():
    import xlwt
    from tempfile import TemporaryFile
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1')

    for i,e in enumerate(list_avetime):
        sheet1.write(i,1,e)

    for i,e in enumerate(list_passed):
        sheet1.write(i,3,e)

    name = "simdata.xls"
    book.save(name)
    book.save(TemporaryFile())

def main(ENTER_PROB, CAR_PROB, in101, in102, in103, in106, in112, in123):
    #Future Event List
    fel = FutureEventList()


    #Make Future Event List
    #Based on 15mins/900 seconds given and stoplight data
    for t in range(1, 901):
        index10=index11=index12=index14 = [0, 0, 0, 0]
        stop10 = [east10, west10, north10, south10]
        stop11 = [east11, west11, north11, south11]
        stop12 = [east12, west12, north12, south12]
        stop14 = [east14, west14, north14, south14]
        tval10 = [t%sum(east10), t%sum(west10), t%sum(north10), t%sum(south10)]
        tval11 = [t%sum(east11), t%sum(west11), t%sum(north11), t%sum(south11)]
        tval12 = [t%sum(east12), t%sum(west12), t%sum(north12), t%sum(south12)]
        # tval13 = [t%sum(east13), t%sum(west13), t%sum(north13), t%sum(south13)]
        tval14 = [t%sum(east14), t%sum(west14), t%sum(north14), t%sum(south14)]


        for i in range(4):
            count = 0
            for j in range(6):
                if tval10[i] > sum((stop10[i])[0:j+1]):
                    count+=1
            index10[i] = count


        for i in range(4):
            count = 0
            for j in range(6):
                if tval11[i] > sum((stop11[i])[0:j+1]):
                    count+=1
            index11[i] = count

        for i in range(4):
            count = 0
            for j in range(6):
                if tval12[i] > sum((stop12[i])[0:j+1]):
                    count+=1
            index12[i] = count

        for i in range(4):
            count = 0
            for j in range(6):
                if tval14[i] > sum((stop14[i])[0:j+1]):
                    count+=1
            index14[i] = count


        event = Event(t, index10, index11, index12, index14)
        fel.push(event)


    #Time statistics
    start_time = time.time()
    NEvents = 0

    #Event Processing Loop
    world = World(ENTER_PROB, CAR_PROB)
    fin_vehicles = []
    now = 0
    print("Now: " + str(now) + "\n")
    print("|10th|===" + str(world.q10to11.qsize()) + "===|11th|===" +  str(world.q11to12.qsize()) + "===|12th|===" +  str(world.q12to13.qsize()) + "===|13th|===" + str(world.q13to14.qsize()) + "===|14th|" +"\n")
    while not fel.is_empty():
        currEvent = fel.pop()

        world.updateServer(currEvent)
        timeDif = currEvent.ts - now
        now = currEvent.ts
        # eventHandler(in101, in102, in103, in106, in112, in123, ENTER_PROB, CAR_PROB, now, timeDif, currEvent, world, fin_vehicles)
        eventHandler(ENTER_PROB, CAR_PROB, now, timeDif, currEvent, world, fin_vehicles, in101, in102, in103, in106, in112, in123)
        print("Now: " + str(now) + "\n")
        print("|10th|===" + str(world.q10to11.qsize()) + "===|11th|===" +  str(world.q11to12.qsize()) + "===|12th|===" +  str(world.q12to13.qsize()) + "===|13th|===" + str(world.q13to14.qsize()) + "===|14th|" +"\n")


    vehicle10to14 = 0
    passtime = []
    for vehicle in fin_vehicles:
        if vehicle.type == True and vehicle.finished == True:
            vehicle10to14 += 1
            passtime.append(vehicle.time)
            print(str(vehicle10to14) + ": " + str(vehicle.time) + "seconds")

    # plt.hist(passtime, bins=22)
    # plt.show()

    print("There are: " + str(vehicle10to14) + " vehicles that travelled from 10th to 14th")
    end_time = time.time()
    list_avetime.append(sum(passtime)/len(passtime))
    list_passed.append(vehicle10to14)

if __name__ == '__main__':

    in101 = [0]
    in102 = [0]
    in123 = [0]
    in103 = [0]
    in106 = [0]
    in112 = [0]
    while in101[len(in101) - 1] < 900:
        Beta = 6.4713
        r = np.random.exponential(scale=Beta)
        in101.append(r+in101[len(in101)-1])
    while in102[len(in102) - 1] < 900:
        Beta = 19.9887
        r = np.random.exponential(scale=Beta)
        in102.append(r+in102[len(in102)-1])
    while in123[len(in123) - 1] < 900:
        Beta = 19.9887
        r = np.random.exponential(scale=Beta)
        in123.append(r+in123[len(in123)-1])
    while in112[len(in112) - 1] < 900:
        Beta = 85.7611
        r = np.random.exponential(scale=Beta)
        in112.append(r+in112[len(in112)-1])
    while in106[len(in106) - 1] < 900:
        Beta = 85.7611
        r = np.random.exponential(scale=Beta)
        in106.append(r+in106[len(in106)-1])
    while in103[len(in103) - 1] < 900:
        Beta = 85.7611
        r = np.random.exponential(scale=Beta)
        in103.append(r+in103[len(in103)-1])
    # print(in101)


    # # Beta =
    # # in = np.random.exponential(scale=Beta)
    # ENTER_PROB = [0.914 + random.uniform(-0.1, 0.1), 0.035, 0.01, 0.051, 0.12] #Calculated for 10th intersection was 0.13
    # CAR_PROB = 4.42 / 5.0
    # # CAR_PROB = random.uniform(4.30, 4.54) / 5.0 #calculated CAR_PROB was 4.42
    # main(ENTER_PROB, CAR_PROB)
    # main(ENTER_PROB, CAR_PROB, in101, in102, in103, in106, in112, in123)

    for i in range(10):
        ENTER_PROB = [0.914 + random.uniform(-0.1, 0.1), 0.035, 0.01, 0.051, 0.12] #Calculated for 10th intersection was 0.13
        CAR_PROB = 4.42 / 5.0 #calculated CAR_PROB was 4.42
        # print(CAR_PROB)
        main(ENTER_PROB, CAR_PROB, in101, in102, in103, in106, in112, in123)
    print("\n")
    print("List of simulation average time in seconds:")
    print(list_avetime)
    print("-------------------")
    print("List of the number of vehicles that travelled from 10th to 14th:")
    print(list_passed)
    m, l, h = mean_confidence_interval(list_avetime)
    print("mean: " + str(m) + "\n")
    print("low: " + str(l) + "\n")
    print("high: " + str(h) + "\n")



    #This is only for writing data to excel
    # writeData()
