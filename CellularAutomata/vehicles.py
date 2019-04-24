import constants as c
import numpy as np

class Car:
    def __init__(self, road, destf):
        self.road = road
        self.pos = (-1, -1)
        self.tile = None
        self.justLaneChanged = False
        self.goal = destf()
        self.dest = self.goal[1]
        self.dest_lane = c.dests_side_to_lane[self.dest]
        self.dixn_i = int(self.goal[0])
        self.dixn = road.getNthIxn(self.dixn_i)
        self.straight = "S" in self.goal
        self.lifespan = 0
        self.timeInSpot = 0
        return

    def update(self, dt):
        self.lifespan += dt
        self.timeInSpot += dt
        x, y = self.pos


        if self.timeInSpot >= self.tile.getWaitTime():
            if self.dixn != None and self.tile.getIntersection() == self.dixn:
                self.die()
                return
            if not self.justLaneChanged:
                # go to dixn
                if self.dixn != None:
                    # if i'm before my destination
                    if x < self.dixn.getX() and self.dixn == self.road.getNextIxn(x):
                        #let's swap lanes towards my dest
                        dir = c.dests_side_to_dir[self.dest]
                        #if there's space
                        if self.road.checkStretch(self.pos, 1, dir):
                            if (y+dir >= 0 and y+dir < 3) and self.road.tiles[x, y+dir].openForMove():
                                self.setSpace(self.road.tiles[x, y+dir])
                                return
                # move forward
                if (x+1 >= c.road_length):
                    self.die()
                    return
                if isSpotFree(self.road, x+1, y):
                    self.setSpace(self.road.tiles[x+1,y])
                elif not self.straight and self.dest == "R":
                    tile = self.road.tiles[x+1, y]
                    if tile.isRedRightTurnOpen():
                        self.setSpace(self.road.tiles[x+1,y])
                        # print("right on red!")

        self.justLaneChanged = False
        return

    def die(self):
        if self.straight:
            c.car_lifespans.append(self.lifespan)
        self.setSpace(None)
        self.tile.clearSpace()


    def setSpace(self, tile):

        self.timeInSpot = 0
        if self.tile != None:
            self.tile.clearSpace()
            self.pos = (-1, -1)
        if tile != None:
            tile.giveSpace(self)
            self.pos = tile.getPos()
            self.tile = tile

    def changeLane(self):
        self.justLaneChanged = True

    def getDesiredLane(self):
        return self.dest_lane

    def approachingIxn(self):
        if self.dixn == None:
            return None
        return self.pos[0] < self.dixn.getX() and self.dixn == self.road.getNextIxn(self.pos[0])

    def __str__(self):
        if self.straight:
            return "D"
        if self.dixn != None and self.dixn.getX() < self.pos[0]:
            # print("MISSED")
            return "M"
        return str(self.dixn_i)

def isSpotFree(road, x, y):
    spot = road.tiles[x, y]
    return spot.openForMove()
    #(spot != None and spot.getOccupant() == None)
