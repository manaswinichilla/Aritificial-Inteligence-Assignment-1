#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [MANASWINI CHILLA MACHILLA]
#
# Based on skeleton code in CSCI B551, Spring 2021
#

import sys

# Parse the map from a given filename

def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Count total # of pichus on board

def count_pichus(board):
    return sum([ row.count('p') for row in board ] )

# Return a string with the board rendered in a human-pichuly format

def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# checks for left up, left down, right up, right down diagonal coordinates from (row,col) and returns 0 if pichu can be placed else returns number greater than 0
def checkViolationofDiagonals(board, row, col):
    checkDgRightDown=0
    checkDgRightUp=0
    checkDgLeftDown=0
    checkDgleftUp=0

    for i, j in zip(range(row+1, len(board), 1),range(col+1, len(board[0]), 1)):
        if board[i][j] == "p":
            checkDgRightDown=1

    for i, j in zip(range(row-1, -1, -1),range(col-1, -1, -1)):
        if board[i][j] =="p":
            checkDgleftUp = 1

    for i, j in zip(range(row+1, len(board), 1),range(col-1, -1, -1)):
        if board[i][j] == "p":
            checkDgLeftDown = 1

    for i, j in zip(range(row-1, -1, -1),range(col+1, len(board[0]), 1)):
        if board[i][j] == "p":
            checkDgRightUp = 1

    return checkDgRightUp+checkDgRightDown+checkDgleftUp+checkDgLeftDown

# checks for row column of (row,col) and returns 0 if pichu can be placed otherwise number greater than 0
def checkViolationOfRowsColumns(board, row, col):
    checkStartToRow = 0
    checkRowToEnd = 0
    checkStartToCol = 0
    checkColtoEnd = 0

    for rs in range(0, col):
        if (board[row][rs] == "p"):
            checkStartToRow = 1
        if (board[row][rs] == 'X' or board[row][rs] == "@"):
            checkStartToRow = 0
    for re in range(len(board[0]) - 1, col, -1):
        if board[row][re] == "p":
            checkRowToEnd = 1
        if board[row][re] == "X" or board[row][re] == "@":
            checkRowToEnd = 0
    for cs in range(0, row):
        if (board[cs][col] == "p"):
            checkStartToCol = 1
        if (board[cs][col] == "X" or board[cs][col] == "@"):
            checkStartToCol = 0
    for ce in range(len(board) - 1, row, -1):
        if (board[ce][col] == "p"):
            checkColtoEnd = 1
        if (board[ce][col] == "X" or board[ce][col] == "@"):
            checkColtoEnd = 0

    return checkStartToRow+checkRowToEnd+checkStartToCol+checkColtoEnd

#add pichu function calls checkViolationOfRowsColumns, if extraCredit paramater is 0, calls checkViolationofDiagonals and returns board with pichu added at
# (row,col) only if the sum of value returned by both check functions is 0.
def add_pichu(board, row, col, extraCredit):
    checkRC=0
    checkDg=0
    checkRC = checkViolationOfRowsColumns(board, row, col)
    if(extraCredit==0):
        checkDg = checkViolationofDiagonals(board, row, col)
    check=checkRC +checkDg
    if check==0:
        return board[0:row] + [board[row][0:col] + ['p',] + board[row][col+1:]] + board[row+1:]
    else:
        return board

# Get list of successors of given board state
def successors(board, extraCredit):
    return [ add_pichu(board, r, c, extraCredit) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.']

# check if board is a goal state
def is_goal(board, k):
    return count_pichus(board) == k

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
# this function is called only when k=0 from solve function. this is used to send 0 to successor function so that extraCredit requirements can be done.
def solveForExtraCredit(initial_board, k):
    fringe = [initial_board]
    visitedBoards = []
    while len(fringe) > 0:
        for s in successors(fringe.pop(), 0):
            if is_goal(s, k):
                return (s, True)
            else:
                if s not in visitedBoards:
                    visitedBoards.append(s)
                    fringe.append(s)
    return ([],None)

# function takes initial board and k and returns new board and success as true after getting board with k pichus. if no solution is found, newboard
# is returned empty and success as False.
def solve(initial_board, k):
    try:
        for i in range(0, len(initial_board)):
            for j in range(0, len(initial_board[0])):
                if (initial_board[i][j] not in "X.@p"):
                    raise Exception("Invalid character in map")
        if(k<0):
            raise Exception("Invalid pichu value")
        #flag=0
        if k == 0:
            (newboard, success) = solve(house_map, k + 1)
            while (success == True):
                #flag=1
                k = k + 1
                (newboard, success) = solveForExtraCredit(house_map, k)
            (newboard, success) = solveForExtraCredit(house_map, k-1)
            return (newboard, success)
        else:
            fringe = [initial_board]
            visitedBoards=[]
            while len(fringe) > 0:
                for s in successors(fringe.pop(),5):
                    if is_goal(s, k):
                        return (s, True)
                    else:
                        if s not in visitedBoards:
                            visitedBoards.append(s)
                            fringe.append(s)

            return ([],None)
    except IndexError as indexerror:
        print("Exception ", str(indexerror), "occured")
        exit(-1)
    except TypeError as typeerror:
        print("Exception ", str(typeerror), "occured")
        exit(-1)
    except ValueError as valueerror:
        print("Exception ", str(valueerror), "occured")
    except Exception as exception:
        print("Exception ", str(exception),"occured")
        exit(-1)


# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(house_map)+ "\n\nLooking for solution...\n")

    (newboard, success) = solve(house_map, k)
    print ("Here's what we found:")
    print (printable_board(newboard) if success else "None")