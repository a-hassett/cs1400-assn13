# Alexandra Hassett, CS 1400

import time
SLEEPTIME = 0.1
FILENAME = "maze.txt"
VERBOSE = False

###################################################################################################################


def solve(maze, row, col):
    if (col == len(maze[0]) - 1 or row == len(maze) - 1) and maze[row][col] == " ":  # check if its our final square
        maze[row][col] = "."
        return True
    elif col not in range(len(maze[0])):  # if column is outside the grid, return false
        return False
    elif row not in range(len(maze)):  # if row is outside the grid, return false
        return False
    elif maze[row][col] == " ":  # if square is open, test out the path and set trackers
        maze[row][col] = "."
        if VERBOSE:
            printMaze(maze)
    else:  # if square is a wall or already has a tracker
        return False

    # test each side of the square for paths
    if solve(maze, row - 1, col):
        return True
    elif solve(maze, row, col - 1):
        return True
    elif solve(maze, row, col + 1):
        return True
    elif solve(maze, row + 1, col):
        return True
    maze[row][col] = " "  # pick up trackers when path fails
    return False  # if there are no paths at all, the entire maze is unsolvable

###################################################################################################################


def readMaze(maze):
    # turn text from maze.txt into a 2x2 array
    mazefile = open(FILENAME, "r")
    for line in mazefile.read().splitlines():
        maze.append([])
        for c in line:
            maze[-1].append(c)
    mazefile.close()


def printMaze(maze):
    print("\n\n\n\n\n\n\n\n\n")
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end="")
        print()
    time.sleep(SLEEPTIME)
    print()


def main():
    maze = []
    readMaze(maze)
    if not solve(maze, 1, 0):
        print("no solution is possible.")
    else:
        printMaze(maze)


main()
