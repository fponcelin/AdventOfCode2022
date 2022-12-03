import re

f = open("input.txt", "r")

prioritiesSumPart1 = 0
prioritiesSumPart2 = 0
group = []

def getCharPriority(c) :
    if ord(c) >= 97 :
        return ord(c) - 96
    else :
        return ord(c) - 38

for line in f :
    # Part 1
    leftHalf = line[:int(len(line)/2)]
    rightHalf = line[int(len(line)/2):]
    for char in leftHalf :
        if re.search(char, rightHalf) and len(line) > 1 :
            prioritiesSumPart1 += getCharPriority(char)
            break

    # Part 2
    group.append(line)

    if len(group) == 3 :
        for char in group[0]:
            if re.search(char, group[1]) and re.search(char, group[2]) :
                prioritiesSumPart2 += getCharPriority(char)
                break
        group = []

print("Sum of priorities part 1:", prioritiesSumPart1)
print("Sum of priorities part 2:", prioritiesSumPart2)