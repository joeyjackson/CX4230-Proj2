import numpy as np;
import constants as c
import tiles
import vehicles

np.random.seed(1969)

class Peachtree:
    def __init__(self):
        self.tiles = np.empty((c.road_length, c.road_width), dtype=object)
        #self.spots = np.empty((c.road_length, c.road_width), dtype=object)
        self.ixns = np.empty((c.road_length), dtype=object)

        for i, row in enumerate(c.peachTreeMap):
            for j, tileSymbol in enumerate(row):
                self.tiles[i, j] = tiles.RoadTile(tileSymbol, (i,j))

        for protoixn in c.ixns:
            ixn = tiles.Intersection(road=self,
                i=protoixn["i"],
                lights=protoixn["lights"],
                times=protoixn["times"])

            for j in range(c.road_width):
                self.tiles[protoixn["i"], j].setIntersection(ixn)
                ixn.addTile(self.tiles[protoixn["i"], j])

            self.ixns[protoixn["i"]] = ixn

        self.only_ixns = [ixn for ixn in self.ixns if ixn != None]

        car = vehicles.Car(self)
        car.setSpace(self.tiles[1,2])

        self.start_spots = []
        for j in range(c.road_width):
            tile = self.tiles[0,j]
            if tile.isValid():
                self.start_spots.append(tile)


    def update(self, dt):
        for ixn in self.ixns:
            if ixn != None:
                ixn.update(dt)

        self.laneChangeUpdate(dt)
        self.movementUpdate(dt)

        # new cars arrive
        for tile in self.start_spots:
            car = tile.getOccupant()
            if car == None:
                if np.random.uniform() < c.arrival_rate:
                    car = vehicles.Car(self)
                    car.setSpace(tile)
        return

    def laneChangeUpdate(self, dt):
        for i in reversed(range(c.road_length)):
            for j in range(c.road_width):
                car = self.tiles[i,j].getOccupant()
                if car != None:
                    # don't try cheesing lane changes in critical timing
                    if not car.approachingIxn():
                        # if not at end
                        if i+1 < c.road_length:
                            # if car in front
                            if not self.tiles[i+1,j].openForMove():
                                dir = 0
                                if j == 2:
                                    dir = -1
                                elif j == 1:
                                    dir = 1
                                if dir != 0:
                                    if self.checkStretch((i,j), 3, dir):
                                        car.setSpace(self.tiles[i,j+dir])
                                        car.changeLane()
                                    #print("swap")
        return

    def checkStretch(self, pos, dist, dir):
        cx, cy = pos
        # if lane out of bounds
        if (cy+dir < 0 or cy+dir >= c.road_width):
            return False

        for d in range(dist):
            # if within road length
            if (cx+d > 0 and cx+d < c.road_length):
                tile = self.tiles[cx+d, cy+dir]
                if not tile.openForMove():
                    return False
            else:
                return False
        #print('swap')
        return True

    def movementUpdate(self, dt):
        # move existing cars
        for i in reversed(range(c.road_length)):
            for j in range(c.road_width):
                car = self.tiles[i,j].getOccupant()
                if car != None:
                    car.update(dt)
        return

    def getNthIxn(self, n):
        if n < 0 or n >= len(self.only_ixns):
            return None
        return self.only_ixns[n]

    def getNextIxn(self, x):
        for ixn in self.ixns[x:]:
            if ixn != None:
                return ixn
        return None

    def getLastIxn(self, x):
        for ixn in self.ixns[:x:-1]:
            if ixn != None:
                return ixn
        return None

    def __str__(self):
        s = ""
        for i in range(c.road_length):
            ixn = self.tiles[i, 0].getIntersection()
            if ixn != None:
                s += str(ixn)
            else:
                s += " "
        s += "\n"

        for j in range(c.road_width):
            for i in range(c.road_length):
                tile = self.tiles[i,j]
                car = tile.getOccupant()
                if car != None:
                    s += str(car)
                else:
                    s += str(tile)
            s += "\n"
        return s
