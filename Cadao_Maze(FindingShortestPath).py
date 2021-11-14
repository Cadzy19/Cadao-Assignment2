import queue


def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze

# "0" is the starting point ,"+" is shortest path found,"#" border and "X" is the destination or end point
def createMaze2():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", "#", "#", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#", "#"])
    return maze


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Shortest Path Found: " + moves) #D-down,L-left and R-right
        printMaze(maze, moves)
        return True

    return False


nums = queue.Queue()
nums.put("")
add = ""
maze = createMaze2()

while not findEnd(maze, add):
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)