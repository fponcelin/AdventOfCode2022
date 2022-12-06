import re
f = open("input.txt", "r")

def findMarker(str) :
    duplicateCount = 0
    for c in str :
        pattern = c + ".*" + c
        if re.search(pattern, str) :
            duplicateCount += 1
    if duplicateCount == 0 :
        return True
    else :
        return False
    
data = f.readline()

# Part 1
found = False
i = 0
while not found :
    marker = data[i:i+4]
    found = findMarker(marker)
    i += 1

# Part 2
found = False
j = 0
while not found :
    marker = data[j:j+14]
    found = findMarker(marker)
    j += 1

print("Part 1: first marker found after character", i+3)
print("Part 2: first marker found after character", j+13)
f.close()