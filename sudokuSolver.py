# Python Project 1: Sudoku Solver
# Started 8/8/2021
# Finished 8/11/2021
# Status: Completed
# -----------------------------------------------------
# Purpose of Project/Learning Goals:
#   -Understand Recursion
#   -Understand Backtracking
#   -Python Syntax (transitioning from C++)
# -----------------------------------------------------

def printGrid():  # print Grid
    print("\n")
    print(*grid, sep="\n")

def findEmpty(i, j):
    # Start from last 0
    for x in range(i,9):
        for y in range (j,9):
            if grid[x][y] == 0:
                print("Reset Empty: " + str(x) + ", " + str(y))
                return x, y
    # Starts from beginning
    for x in range(0,9):
        for y in range (0,9):
            if grid[x][y] == 0:
                print("Reset Empty: " + str(x) + ", " + str(y))
                return x, y
    print("No Empty: " + str(x)+ "," + str(y))
    return -1,-1

def isSafe(fillNum,i,j): # check if number is safe
    if checkBox(fillNum, i,j) and checkCol(fillNum, j) and checkRow(fillNum,i):
        return True
    else:
        return False

def checkRow(rowFill, i):
    for y in range(9):
        if grid[i][y] == rowFill:
            return False
    return True
def checkCol(colFill, j):
    for x in range(9):
        if grid[x][j] == colFill:
            return False
    return True
def checkBox(boxFill,x,y):
    startRow = x - x % 3
    startCol = y - y % 3
    for r in range(3):
        for c in range(3):
            if grid[startRow+r][startCol+c] == boxFill:
                return False
    return True

def sudokuSolver(grid, i=0, j=0):
    i,j = findEmpty(i,j)
    if i == -1:
        print("\n Solved!")
        return True
    for x in range(9):
        if isSafe(x+1,i,j):
            grid[i][j] = x+1
            printGrid()
            if sudokuSolver(grid,i,j):
                return True
            print("BEFORE RESET 0")
            printGrid()
            grid[i][j] = 0
            print("AFTER RESET 0")
            printGrid()
    print("FALSE SOLUTION")
    return False

if __name__ == '__main__':
    grid = [[0 for x in range(9)] for y in range(9)]
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 0, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    printGrid()
    sudokuSolver(grid)
    print("FINISHED")
    printGrid()