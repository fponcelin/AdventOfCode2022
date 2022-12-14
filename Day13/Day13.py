import ast
f = open("input.txt", "r")
pairs = []
newPair = True
for line in f :
    if line == '\n' : 
        newPair = True
        continue
    if newPair :
        pair = [ast.literal_eval(line.rstrip('\n')), ""]
        pairs.append(pair)
        newPair = False
    else :
        pairs[-1][1] = ast.literal_eval(line.rstrip('\n'))
f.close()

def compareData(left, right) :
    #print("Comparing:", left, " vs", right)
    # Compare values
    if type(left) is int  and type(right) is int:
        if left > right :
            return False
        elif left < right :
            return True
        else :
            return "continue"
    else :  
        # Address mixed types
        if type(left) != type(right) :
            if type(right) is int :
                right = [right]
            elif right is not None :
                left = [left]
            else :
                return False
        
        # Value is list, compare lengths and iterate recursively
        isLeftLonger = False
        isRightLonger = False
        if len(left) > len(right) :
            if len(right) > 0 :
                length = len(right)
                isLeftLonger = True
            else :
                return False
        else :
            length = len(left)
            if length < len(right) : 
                isRightLonger = True
        if length > 0 :
            for i in range(length) :
                isValid = compareData(left[i], right[i])
                #if not isValid or isValid != "continue" : break
                if isValid == "continue" :
                    continue
                else :
                    break
            if isLeftLonger :
                if isValid == "continue" : 
                    return False
                else :
                    return isValid
            elif isRightLonger :
                if isValid == "continue" :
                    return True
                else :
                    return isValid
            else :
                return isValid
        elif len(left) == len(right) :
            return "continue"
        else :
            return True
        
# Part 1
indiceSum = 0
for index, pair in enumerate(pairs) :
    isValid = compareData(pair[0], pair[1])
    if isValid : indiceSum += index + 1

print("Part 1 - indice sum:", indiceSum)

# Part 2
# Create a new list of packets
disorderedPackets = []
for pair in pairs :
    for packet in pair :
        disorderedPackets.append(packet)

# Put them in order in a new list
orderedPackets = [[[2]], [[6]]]
for newPacket in disorderedPackets :
    for i, packet in enumerate(orderedPackets) :
        if compareData(newPacket, packet) :
            orderedPackets.insert(i, newPacket)
            break

# Get the decoder key
decoderKey = 1
for i, packet in enumerate(orderedPackets) :
    if packet == [[2]] or packet == [[6]] :
        decoderKey *= i + 1
print("Part 2 - Decoder key:", decoderKey)