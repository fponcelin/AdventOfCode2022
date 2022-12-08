f = open("input.txt", "r")
trees = []

for line in f :
    trees.append([])
    for d in line.rstrip('\n') :
        trees[-1].append(int(d))

# Part 1
visibleTreesCoords = set()
def findVisibleTrees(treeLine, rangeOrder, orientation, index) :
    highest = -1
    for i in rangeOrder :
        if orientation == "h" :
            coords = str(i) + "," + str(index)
        else :
            coords = str(index) + "," + str(i)
        if treeLine[i] > highest :
            highest = treeLine[i]
            if not coords in visibleTreesCoords :
                visibleTreesCoords.add(coords)

# Horizontal
for rowIndex, treeRow in enumerate(trees) :
    # from left to right
    findVisibleTrees(treeRow, range(0, len(treeRow)), "h", rowIndex)
    # from right to left
    findVisibleTrees(treeRow, reversed(range(0, len(treeRow))), "h", rowIndex)

# Vertical
for colIndex in range (0, len(trees[0])) :
    # Build new list
    treeCol = []
    for i in range(0, len(trees)) :
        treeCol.append(trees[i][colIndex])
    # from top to bottom
    findVisibleTrees(treeCol, range(0, len(treeCol)), "v", colIndex)
    # from bottom to top
    findVisibleTrees(treeCol, reversed(range(0, len(treeCol))), "v", colIndex)

print("Part 1 - Visible trees count:", len(visibleTreesCoords))

# Part 2
def getScenicScore(x, y) :
    height = trees[y][x]

    # Look left
    dist = 0
    for i in reversed(range(x)) :
        if trees[y][i] < height :
            dist += 1
        else :
            dist += 1
            break
    score = dist

    # Look right
    dist = 0
    for i in range(x + 1, len(trees[0])) :
        if trees[y][i] < height :
            dist += 1
        else :
            dist += 1
            break
    score = score * dist

    # Look up
    dist = 0
    for i in reversed(range(y)) :
        if trees[i][x] < height :
            dist += 1
        else :
            dist += 1
            break
    score = score * dist

    # Look down
    dist = 0
    for i in range(y + 1, len(trees)) :
        if trees[i][x] < height :
            dist += 1
        else :
            dist += 1
            break
    score = score * dist
    return score

highScore = 0
for rowIndex, treeRow in enumerate(trees) :
    if rowIndex == 0 or rowIndex == len(trees) :
        continue
    for colIndex, tree in enumerate(treeRow) :
        if colIndex == 0 or colIndex == len(treeRow) :
            continue
        treeScore = getScenicScore(colIndex, rowIndex)
        if treeScore > highScore :
            highScore = treeScore

print("Part 2 - Highest scenic score:", highScore)