import math, re, copy
f = open("input.txt", "r")

monkeys = []

class Monkey() :
    def __init__(self) :
        self.items = [] # List of item values
        self.operation = [] # Math operation, provided as a list of 3 strings (both arguments and operator)
        self.test = 1 # Value to be divisible by
        self.monkeyPass = 0 # Index of monkey to throw to if test passes
        self.monkeyFail = 0 # Index of monkey to throw to if test fails
        self.inspectedItems = 0

    def doOperation(self, item) :
        if self.operation[2] == "old" :
            arg = item
        else :
            arg = int(self.operation[2])
        
        if self.operation[1] == "+" :
            item = item + arg
        elif self.operation[1] == "*" :
            item = item * arg

        return item

    def takeTurn(self, relief) :
        for item in self.items :
            item = self.doOperation(item)
            if relief : 
                item = item // 3
            else :
                item = item % lcm

            if item % self.test == 0 :
                if relief :
                    monkeysPart1[self.monkeyPass].items.append(item)
                else :
                    monkeysPart2[self.monkeyPass].items.append(item)
            else :
                if relief :
                    monkeysPart1[self.monkeyFail].items.append(item)
                else:
                    monkeysPart2[self.monkeyFail].items.append(item)
            self.inspectedItems += 1
        self.items.clear()

for line in f :
    if line[0] == "M" :
        monkeys.append(Monkey())
    elif re.search("Starting items:", line) :
        items = line.split(": ")[1].split(", ")
        for item in items :
            monkeys[-1].items.append(int(item))
    elif re.search("Operation:", line) :
        monkeys[-1].operation = line.split("= ")[1].split()
    elif re.search("Test:", line) :
        monkeys[-1].test = int(line.split()[-1])
    elif re.search("If true:", line) :
        monkeys[-1].monkeyPass = int(line.split()[-1])
    elif re.search("If false:", line) :
        monkeys[-1].monkeyFail = int(line.split()[-1])

f.close()
lcm = math.lcm(*([monkey.test for monkey in monkeys]))

# Part 1
monkeysPart1 = copy.deepcopy(monkeys)
for i in range(20) :
    for monkey in monkeysPart1 :
        monkey.takeTurn(True)

monkeysActivity = []
for monkey in monkeysPart1 :
    monkeysActivity.append(monkey.inspectedItems)

monkeysActivity.sort(reverse = True)
print("Part 1 - Monkey business:", monkeysActivity[0] * monkeysActivity[1])

# Part 2 - I needed some help on this one, did not figure out the math.lcm and the modulo reducion bit by myself
monkeysPart2 = copy.deepcopy(monkeys)
for i in range(10000) :
    for monkey in monkeysPart2 :
        monkey.takeTurn(False)

monkeysActivity = []
for monkey in monkeysPart2 :
    monkeysActivity.append(monkey.inspectedItems)

monkeysActivity.sort(reverse = True)
print("Part 2 - Monkey business:", monkeysActivity[0] * monkeysActivity[1])