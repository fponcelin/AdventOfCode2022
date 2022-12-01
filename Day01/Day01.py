import re

f = open("./input.txt", "r")
elvesCalories = []
count = 0

for l in f:
    if re.search('\d',l):
        count += int(l)
    else:
        elvesCalories.append(count)
        count = 0

if count != 0:
    elvesCalories.append(count)

elvesCalories.sort(reverse=True)
topThreeElves = elvesCalories[:3]

print("Elf with the most calories:", topThreeElves[0])
print("Total calories by top 3 elves:", sum(topThreeElves))