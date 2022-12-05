import re, copy
f = open("input.txt", "r")

rawStacks = []
instructions = []

for line in f :
    if line[0] == "[" :
        rawStacks.append(line)
    elif line[0] == "m" :
        instructions.append(line.split())
    elif len(line) > 1 :
        indexes = line

f.close()

# Rearrange the raw stacks data in a dictionary of lists
rawStacks.reverse()
stacks = {
    "1" : [],
    "2" : [],
    "3" : [],
    "4" : [],
    "5" : [],
    "6" : [],
    "7" : [],
    "8" : [],
    "9" : []
}

for level in rawStacks :
    for i in range(len(level)) :
        if re.search('[1-9]', indexes[i]) and level[i] != ' ' :
            stacks[indexes[i]].append(level[i])

stacksCopy = copy.deepcopy(stacks)

# Now let's follow instructions
for instruction in instructions :
    # Part 2
    stacksCopy[instruction[5]].extend(stacksCopy[instruction[3]][-int(instruction[1]):])

    # Part 1
    for i in range(1, int(instruction[1])+1) :
        stacks[instruction[5]].append(stacks[instruction[3]][-1])
        stacks[instruction[3]].pop()
        stacksCopy[instruction[3]].pop()


# Get the top crate of each stack
part1Result = ""
for stack in stacks.values() :
    part1Result += stack[-1]

part2Result = ""
for stack in stacksCopy.values() :
    part2Result += stack[-1]

print("Part 1 result:", part1Result)
print("Part 2 result:", part2Result)