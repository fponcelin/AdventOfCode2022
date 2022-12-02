f = open("input.txt", "r")

shapeScores = {
    "X" : { "shapeScore" : 1, "A" : 3, "B" : 0, "C" : 6 },
    "Y" : { "shapeScore" : 2, "A" : 6, "B" : 3, "C" : 0 },
    "Z" : { "shapeScore" : 3, "A" : 0, "B" : 6, "C" : 3 }
}

roundScores = {
    "X" : { "roundScore" : 0, "A" : 3, "B" : 1, "C" : 2 },
    "Y" : { "roundScore" : 3, "A" : 1, "B" : 2, "C" : 3 },
    "Z" : { "roundScore" : 6, "A" : 2, "B" : 3, "C" : 1 }
}

scorePart1 = 0
scorePart2 = 0

for line in f :
    scorePart1 = scorePart1 + shapeScores[line[2]]["shapeScore"] + shapeScores[line[2]][line[0]]
    scorePart2 = scorePart2 + roundScores[line[2]]["roundScore"] + roundScores[line[2]][line[0]]

print("Part 1 score:", scorePart1)
print("Part 2 score:", scorePart2)