import re
f = open("input.txt", "r")

def findMarkerCharNum(data, length) :
    found = False
    i = 0
    while not found :
        marker = data[i:i+length]
        duplicateCount = 0
        for c in marker :
            pattern = c + ".*" + c
            if re.search(pattern, marker) :
                duplicateCount += 1
        found = (duplicateCount == 0)
        i += 1
    return i + length - 1
    
data = f.readline()

print("Part 1: first marker found after character", findMarkerCharNum(data, 4))
print("Part 2: first marker found after character", findMarkerCharNum(data, 14))
f.close()