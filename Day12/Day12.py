import sys

f = open("input.txt", "r")
maze = []
for y, line in enumerate(f) :
    row = []
    for x, char in enumerate(line) :
        if char == "S" :
            start = (y, x)
            char = "a"
        if char == "E" :
            end = (y, x)
            char = "z"
        if char == '\n' :
            continue
        row.append(ord(char))
    maze.append(row)

f.close()

# A* pathfinding code copied from https://github.com/ryancollingwood/arcade-rabbit-herder/blob/master/pathfinding/astar.py and edited to fit the challenge 
# (actually making it more like Dijkstra’s algorithm)
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

    def __eq__(self, other):
        return self.position == other.position


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path

def printPath(path) :
    output = ""
    for y, row in enumerate(maze) :
        for x, point in enumerate(row) :
            if (y, x) in path :
                output += " "
            else :
                output += chr(point)
        output += '\n'
    return output


def findPath(maze, start, end):
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    
    # Counting iterations for funsies (used during debugging to assess if going for too long)
    outer_iterations = 0

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0))

    # Loop until you find the end
    while len(open_list) > 0 :
        outer_iterations += 1
        #sys.stdout.write("\rCurrent iteration: " + str(outer_iterations))
        #sys.stdout.flush()

        # Get the current node
        current_node = open_list[0]
        current_index = 0

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []
        
        for new_position in adjacent_squares:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            outside_range_criteria = [
                node_position[0] > (len(maze) - 1),
                node_position[0] < 0,
                node_position[1] > (len(maze[0]) - 1),
                node_position[1] < 0,
            ]
            
            if any(outside_range_criteria):
                continue
            
            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] > maze[current_node.position[0]][current_node.position[1]] + 1 :
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Child is already in the open list
            if len([open_node for open_node in open_list if child == open_node]) > 0:
                continue

            # Add the child to the open list
            open_list.append(child)
    
    # If we get to that point there is no path
    return False

# Part 1
path = findPath(maze, start, end)
print()
print(printPath(path))
print("Part 1 - shortest path steps:", len(path) - 1)
print()

# Part 2
part2Starts = []
for y, row in enumerate(maze) :
    for x, char in enumerate(row) :
        if chr(char) == "a" :
            adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0))
            for new_position in adjacent_squares: 
                # Get node position
                node_position = (y + new_position[0], x + new_position[1])

                # Make sure within range
                outside_range_criteria = [
                    node_position[0] > (len(maze) - 1),
                    node_position[0] < 0,
                    node_position[1] > (len(maze[0]) - 1),
                    node_position[1] < 0,
                ]
                
                if any(outside_range_criteria):
                    continue

                # Return True if current point valid start for part 2
                if maze[node_position[0]][node_position[1]] == char + 1 :
                    part2Starts.append((y,x))

length = len(path) - 1
shortestPath = path
iteration = 0
for startPoint in part2Starts :
    iteration += 1
    sys.stdout.write("\rCurrent a iteration: " + str(iteration) + "/" + str(len(part2Starts)) + " - Shortest path so far: " + str(len(shortestPath) - 1))
    sys.stdout.flush()
    path = findPath(maze, startPoint, end)
    if path :
        if len(path) < len(shortestPath) : shortestPath = path

print()
print(printPath(shortestPath))
print("Part 2 - shortest path steps:", len(shortestPath) - 1)