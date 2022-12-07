f = open("input.txt", "r")

def writePath(pathList) :
    path = ""
    for dir in pathList :
        path += dir
    return path

directories = {
    "/" : 0
}
cd = ["/"]
for line in f :
    command = line.split()
    if command[0] == "$" :
        if command[1] == "cd" :
            if command[2] == ".." :
                cd.pop()
            elif command[2] != "/" :
                cd.append(command[2] + "/")
    else :
        if command[0] == "dir" :
            directories[writePath(cd) + command[1] + "/"] = 0
        else :
            filePath = ""
            for dir in cd :
                filePath += dir
                directories[filePath] += int(command[0])
f.close()

# Part 1
sizesSum = 0
for dirSize in directories.values() :
    if dirSize <= 100000 :
        sizesSum += dirSize

print("Part 1 sizes sum result:", sizesSum)

# Part 2
diskSize = 70000000
freeSpace = diskSize - directories["/"]
requiredSize = 30000000 - freeSpace
smallestDir = diskSize

for dirSize in directories.values() :
    if dirSize >= requiredSize and dirSize < smallestDir :
        smallestDir = dirSize

print("Part 2 directory size:", smallestDir)