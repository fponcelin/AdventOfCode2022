import re
import math
from scipy.spatial.distance import cityblock
f = open("input.txt", "r")

sensors = []
edges = {
    "left" : math.inf,
    "right" : -math.inf,
    "top" : math.inf,
    "bottom" : -math.inf
}

class Sensor() :
    def __init__(self, position, beaconPos) :
        self.position = position
        self.closestBeacon = beaconPos
        self.distance = cityblock(position, beaconPos)

    def findRowCoverage(self, row) :
        if self.position[1] <= row :
            if not row in range(self.position[1], self.position[1] + self.distance + 1) : 
                return
            else :
                distance = self.distance - (row - self.position[1])
        else :
            if not row in range(self.position[1] - self.distance, self.position[1] + 1) : 
                return
            else : 
                distance = self.distance - (self.position[1] - row)

        if self.position[0] - distance < edges["left"] :
            left = edges["left"]
        else :
            left = self.position[0] - distance
        if self.position[0] + distance > edges["right"] :
            right = edges["right"]
        else :
            right = self.position[0] + distance
        return (left, right)


for line in f :
    coords = list(map(int, re.findall('-?\d+', line)))
    sensor = Sensor((coords[0], coords[1]), (coords[2], coords[3]))
    sensors.append(sensor)
    # find map edges
    if sensor.position[0] - sensor.distance < edges["left"] : edges["left"] = sensor.position[0] - sensor.distance
    if sensor.position[0] + sensor.distance > edges["right"] : edges["right"] = sensor.position[0] + sensor.distance
    if sensor.position[1] - sensor.distance < edges["top"] : edges["top"] = sensor.position[1] - sensor.distance
    if sensor.position[1] + sensor.distance > edges["bottom"] : edges["bottom"] = sensor.position[1] + sensor.distance

    if coords[2] < edges["left"] : edges["left"] = coords[2]
    if coords[2] > edges["right"] : edges["right"] = coords[2]
    if coords[3] < edges["top"] : edges["top"] = coords[3]
    if coords[3] > edges["bottom"] : edges["bottom"] = coords[3]
f.close()

def getRowCoveredRange(row) :
    rowCoverageRanges = []
    for sensor in sensors :
        coverageRange = sensor.findRowCoverage(row)
        if coverageRange : rowCoverageRanges.append(coverageRange)

    reducedCoverage = []
    for begin,end in sorted(rowCoverageRanges):
        if reducedCoverage and reducedCoverage[-1][1] >= begin - 1:
            reducedCoverage[-1][1] = max(reducedCoverage[-1][1], end)
        else:
            reducedCoverage.append([begin, end])
    return reducedCoverage

# Part 1
y = 2000000
coverageRanges = getRowCoveredRange(y)
count = 0
for coverage in coverageRanges :
    count += coverage[1] - coverage[0]

print("Part 1 - Positions count:", count)

# Part 2
edges["left"] = 0
edges["right"] = 4000000
edges["top"] = 0
edges["bottom"] = 4000000

for y in range(4000001) :
    coverageRanges = getRowCoveredRange(y)
    if len(coverageRanges) > 1 :
        x = coverageRanges[0][1] + 1
        break
    elif coverageRanges[0][1] - coverageRanges[0][0] == 1 :
        if coverageRanges[0][0] > 0 : 
            x = 0
        else :
            x = 4000000
        break

print("Part 2 - Tuning frequency:", x * 4000000 + y)