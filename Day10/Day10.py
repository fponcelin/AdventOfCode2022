import math
f = open("input.txt", "r")

instructions = []
for line in f :
    instructions.append(line.split())

# Part 1
cycle = 0
register = 1
signalStrengthSum = 0
signalStrengthCycles = {20, 60, 100, 140, 180, 220}

def checkSignalStrength() :
    global signalStrengthSum, cycle
    cycle += 1
    if cycle in signalStrengthCycles :
        signalStrengthSum += register * cycle

for instruction in instructions :
    if instruction[0] == "noop" : 
        checkSignalStrength()
    else :
        checkSignalStrength()
        checkSignalStrength()
        register += int(instruction[1])
        

print("Part 1 - Signal strengths sum:", signalStrengthSum)

# Part 2
cycle = 0
register = 1
output = ["", "", "", "", "", ""]

def processInstruction() :
    global cycle, output
    cycle += 1
    if cycle % 40 - 1 in { register - 1, register, register + 1 } :
        output[math.floor((cycle - 1) / 40)] += '#'
    else :
        output[math.floor((cycle - 1) / 40)] += '.'
 
for instruction in instructions :
    if instruction[0] == "noop" : 
        processInstruction()
    else :
        processInstruction()
        processInstruction()
        register += int(instruction[1])

print("Part 2:")
print()
for line in output :
    print(line)
print()