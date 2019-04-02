import constants as c

tiles = [
    'L',  #Left turn only lane
    'S',  #General Lane
    'R',  #Right turn only lane
    'IL', #Intersection Left Lane
    'ILO', #Intersection Left Only Lane
    'IS', #Intersection General lane
    'IR', #Intersection Right lane
    'IRO', #Intersection Right Only lane
    'X']  #Not usable

tileRender = {
    'L': '^',
    'S': '-',
    'R': 'v',
    'IL': 'L',
    'ILO': 'A',
    'IS': '#',
    'IR': 'T',
    'IRO': 'R',
    'X': ' '
}

class RoadTile:
    def __init__(self, type="S", pos=(-1,-1)):
        self.occupant = None
        self.type = type
        self.pos = pos
        self.valid = (type != "X")
        self.intersection = None

    def __str__(self):
        if self.occupant != None:
            return "O"
        return tileRender[self.type]

    def giveSpace(self, car):
        self.occupant = car

    def clearSpace(self):
        self.occupant = None

    def getPos(self):
        return self.pos

    def getOccupant(self):
        return self.occupant

    def openForMove(self):
        if (self.intersection == None):
            return self.occupant == None
        if self.occupant:
            return False
        return self.intersection.ixnOpen()

    def isValid(self):
        return self.valid

    def isRedRightTurnOpen(self):
        return self.type == "IR"

    def setIntersection(self, ixn):
        self.intersection = ixn

    def getIntersection(self):
        return self.intersection

    def inIntersection(self):
        return self.intersection != None

    def getX(self):
        return self.pos[0]

lights = ["G", "Y", "R"]

class Intersection:
    def __init__(self, road=None, i=0, lights=["G","Y","R"], times=[10, 5, 10]):
        self.road = road
        self.i = i
        self.lights = lights
        self.times = times
        self.max_state = len(lights)
        self.state = 0
        self.timer = self.times[0]
        self.tiles = []

    def setRoad(self, road):
        self.road = road

    def update(self):
        self.timer -= 1
        if (self.timer <= 0):
            self.state = (self.state + 1) % self.max_state
            self.timer = self.times[self.state]

    def addTile(self, tile):
        self.tiles.append(tile)

    def ixnOpen(self):
        return self.lights[self.state] in ["G", "g", "Y", "y"]


    def getX(self):
        return self.i

    def __str__(self):
        return self.lights[self.state]
