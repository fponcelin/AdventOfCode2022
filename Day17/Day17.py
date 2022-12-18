import sys
f = open("input.txt", "r")

for line in f :
    jetPattern = line.rstrip('\n')
    break
f.close()

shapes = []
shapes.append([[0,0], [1,0], [2,0], [3,0]])
shapes.append([[1,0], [0,1], [1,1], [2,1], [1,2]])
shapes.append([[0,0], [1,0], [2,0], [2,1], [2,2]])
shapes.append([[0,0], [0,1], [0,2], [0,3]])
shapes.append([[0,0], [1,0], [0,1], [1,1]])

jetCoords = {
    "<" : -1,
    ">" : 1
}

height = 0
rocksCoords = []

class Rock() :
    def __init__(self, shape) :
        self.shape = []
        for coord in shape :
            self.shape.append([coord[0] + 2, coord[1] + 3 + height])

def printOutput(rock) :
    output = ["+-------+"]
    for y in range(height + 5) :
        row = "|"
        for x in range(7) :
            if [x,y] in rocksCoords or [x,y] in rock.shape :
                row += "#"
            else :
                row += "."
        row += "|"
        output.append(row)

    print()
    for row in reversed(output) :
        print(row)

def dropRock(rock, jetIndex) :
    global height
    start = True
    while True :
        for index, jet in enumerate(jetPattern) :
            if index < jetIndex and start : continue
            isPushed = True
            isGoingDown = True
            start = False

            # Check for lateral collision
            for coord in rock.shape :
                if [coord[0] + jetCoords[jet], coord[1]] in rocksCoords or not 0 <= coord[0] + jetCoords[jet] <= 6 :
                    isPushed = False
                    break
            
            # Push rock
            if isPushed :
                for coord in rock.shape :
                    coord[0] += jetCoords[jet]

            # Check for vertical collision
            for coord in rock.shape :
                if [coord[0], coord[1] - 1] in rocksCoords or coord[1] - 1 < 0 :
                    isGoingDown = False
                    break
            
            # Drop one unit and repeat or rest
            if isGoingDown :
                for coord in rock.shape :
                    coord[1] -= 1
            else :
                for coord in rock.shape :
                    rocksCoords.append(coord)
                    if coord[1] >= height : 
                        height = coord[1] + 1
                #printOutput(rock)
                if index + 1 >= len(jetPattern) :
                    return 0
                return index + 1


# Part 1
rocksCount = 0
nextJet = 0
rocksLimit = 2022
while rocksCount < rocksLimit :
    for shape in shapes :
        rock = Rock(shape)
        nextJet = dropRock(rock, nextJet)
        rocksCount += 1
        sys.stdout.write("\rCurrent rock count: " + str(rocksCount))
        sys.stdout.flush()
        if rocksCount == rocksLimit : break
    
print()
print("Part 1 - height:", height)

# Part 2
# Repeat part 1 with a trillion rocks and wait a week for the result ¯\_(ツ)_/¯