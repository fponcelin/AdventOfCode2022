f = open("input.txt", "r")
instructions = []
for line in f :
    instructions.append(line.split())

moveRef = {
    'R' : [1, 0],
    'L' : [-1, 0],
    'U' : [0, 1],
    'D' : [0, -1]
}

def moveTail(hPos, tPos) :
    if abs(hPos[0] - tPos[0]) > 1 and abs(hPos[1] - tPos[1]) > 1 :
        tPos[0] += 1 if hPos[0] > tPos[0] else -1
        tPos[1] += 1 if hPos[1] > tPos[1] else -1
    elif abs(hPos[0] - tPos[0]) > 1 :
        tPos[0] += 1 if hPos[0] > tPos[0] else -1
        tPos[1] += hPos[1] - tPos[1]
    elif abs(hPos[1] - tPos[1]) > 1 :
        tPos[0] += hPos[0] - tPos[0]
        tPos[1] += 1 if hPos[1] > tPos[1] else -1
    return tPos
    
# Part 1
hPos = [0, 0]
tPos = [0, 0]
visitedCoords = {'0,0'}
for instruction in instructions :
    for i in range(int(instruction[1])) :
        hPos[0] += moveRef[instruction[0]][0]
        hPos[1] += moveRef[instruction[0]][1]
        tPos = moveTail(hPos, tPos)
        newCoord = str(tPos[0]) + ',' + str(tPos[1])
        if not newCoord in visitedCoords :
            visitedCoords.add(newCoord)

print("Part 1 - Unique visited positions:", len(visitedCoords))

# Part 2
rope = []
visitedCoords = {'0,0'}
for i in range(10) :
    rope.append([0,0])

for instruction in instructions :
    for i in range(int(instruction[1])) :
        rope[0][0] += moveRef[instruction[0]][0]
        rope[0][1] += moveRef[instruction[0]][1]
        for index, knot in enumerate(rope) :
            if index == 0 : continue
            knot = moveTail(rope[index - 1], knot)
        tailCoord = str(rope[-1][0]) + ',' + str(rope[-1][1])
        if not tailCoord in visitedCoords :
            visitedCoords.add(tailCoord)

print("Part 2 - Unique visited positions:", len(visitedCoords))