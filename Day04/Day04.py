f = open("input.txt", "r")

part1Count = 0
part2Count = 0

for line in f :
    pairs = line.rsplit(',')
    leftPair = pairs[0].rsplit('-')
    rightPair = pairs[1].rsplit('-')

    if int(leftPair[0]) >= int(rightPair[0]) and int(leftPair[1]) <= int(rightPair[1]) or int(rightPair[0]) >= int(leftPair[0]) and int(rightPair[1]) <= int(leftPair[1]) :
        part1Count += 1

    if int(leftPair[0]) <= int(rightPair[1]) and int(leftPair[1]) >= int(rightPair[0]) or int(rightPair[0]) <= int(leftPair[1]) and int(rightPair[1]) >= int(leftPair[0]) :
        part2Count += 1

f.close()

print("Part 1 count:", part1Count)
print("Part 2 count:", part2Count)