import re
from sympy import sympify, solve

f = open("input.txt", "r")
monkeys = dict()
for line in f :
    input = line.rstrip('\n').split(': ')
    monkeys[input[0]] = input[1]
f.close()

def calculate(num1, num2, operator) :
    return eval(str(num1) + operator + str(num2))

def getValue(monkey) :
    #pattern = '\d+'
    if re.search('\d+', monkeys[monkey]) :
        return monkeys[monkey]
    else :
        input = monkeys[monkey].split()
        num1 = getValue(input[0])
        num2 = getValue(input[2])
        operator = input[1]
        result = calculate(num1, num2, operator)
        return result

# Part 1
root = getValue('root')
print("Part 1:", int(root))


# Part 2
def buildEq(eq) :
    while True :
        if re.search('[a-z]{4}', eq) :
            subMonkeys = re.findall('[a-z]{4}', eq)
            for monkey in subMonkeys :
                if re.search('\d+', monkeys[monkey]) :
                    eq = re.sub(monkey, monkeys[monkey], eq)
                else :
                    eq = re.sub(monkey, '(' + monkeys[monkey] + ')', eq)
        else :
            return eq


rootLeft = monkeys['root'].split()[0]
rootRight = monkeys['root'].split()[2]
monkeys['humn'] = 'x'
eq = buildEq(rootLeft + ' - ' + rootRight)
eq = sympify(eq)
print("Part 2:", solve(eq)[0])