import sys
f = open("input.txt", "r")
rocks = []
maxX = 0
maxY = 0

class Rock() :
    def __init__(self, path):
        pathCorners = path.rstrip('\n').split(' -> ')
        corners = []
        for pathCorner in pathCorners :
            corners.append((int(pathCorner.split(',')[0]), int(pathCorner.split(',')[1])))

        # Now build all the points between each corner
        points = []
        for i in range(len(corners) - 1) :
            if corners[i][0] <= corners[i+1][0] :
                left = corners[i][0]
                right = corners[i+1][0]
            else :
                left = corners[i+1][0]
                right = corners[i][0]
            if corners[i][1] <= corners[i+1][1] :
                low = corners[i][1]
                high = corners[i+1][1]
            else :
                low = corners[i+1][1]
                high = corners[i][1]

            for x in range(left, right +1) :
                for y in range(low, high +1) :
                    if (x,y) not in points : points.append((x,y))
        self.points = points

class Sand() :
    def __init__(self, position=(500,0)) :
        self.position = position
        self.falling = True
        self.fallenOut = False

    def fall(self) :
        current = self.position
        moves = [(current[0], current[1] + 1), (current[0] - 1, current[1] + 1), (current[0] + 1, current[1] + 1)]
        falling = False
        for next in moves :
            if next[1] >= len(cave) :
                self.fallenOut = True
                break
            if next[0] >= len(cave[0]) :
                extendCave()
            if cave[next[1]][next[0]] != "." :
                continue
            else :
                falling = True
                self.position = next
                break
        self.falling = falling
        
def produceSand() :
    sand = Sand()
    while sand.falling :
        sand.fall()
        if sand.fallenOut :
            return False
    cave[sand.position[1]][sand.position[0]] = "o"
    if sand.position == (500,0) :
        return False
    return True

def extendCave() :
    for y, row in enumerate(cave) :
        if y < len(cave) - 1 :
            row.append('.')
        else :
            row.append('#')
                

for line in f :
    rock = Rock(line)
    rocks.append(rock)
    for coord in rock.points :
        if coord[0] > maxX : maxX = coord[0]
        if coord[1] > maxY : maxY = coord[1]

# Let's draw the cave to visualise it
cave = []
for y in range(maxY + 1) :
    line = []
    for x in range(0, maxX + 1) :
        line.append(".")
    cave.append(line)

for rock in rocks :
    for point in rock.points :
        cave[point[1]][point[0]] = "#"

# Part 1
sandGrains = 0
while produceSand() :
    sandGrains += 1

# Draw the cave
for line in cave :
    row = ""
    for x, point in enumerate(line) :
        if x < 400 : continue
        row += point
    print(row)

print()
print("Part 1 - Sand grains at rest:", sandGrains)

# Part 2
# Let's redraw the cave
cave = []
for y in range(maxY + 3) :
    line = []
    if y < maxY + 2 :
        for x in range(0, maxX + 1) :
            line.append(".")
    else :
        for x in range(0, maxX + 1) :
            line.append("#")
    cave.append(line)

for rock in rocks :
    for point in rock.points :
        cave[point[1]][point[0]] = "#"

sandGrains = 0
while produceSand() :
    sandGrains += 1
    
print("Part 2 - Sand grains at rest:", sandGrains + 1)