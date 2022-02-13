#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [MANASWINI CHILLA AND MACHILLA]
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Check if a row,col index pair is on the map, and also if it is ".".
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

#successor function
# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

	# Return only moves that are within the board and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# this function, based on states given to it, returns direction from 1'st parameter to the second parameter
#either Left "L", Right "R", Up "U", Down "D
def findmydirection(curr, move):
        a=move[1]-curr[1]
        b=curr[1]-move[1]
        c=curr[0]-move[0]
        d=move[0]-curr[0]
        if(a==1):
                return "R"
        elif(b==1):
                return "L"
        elif(c==1):
                return "U"
        elif(d==1):
                return "D"

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#

def search(house_map):
        try:
                # Find pichu start position
                for i in range(0, len(house_map)):
                        for j in range(0, len(house_map[0])):
                                if(house_map[i][j] not in "X.@p"):
                                        raise Exception ("Invalid character in map")

                visited = []
                direction=""
                pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
                fringe=[(pichu_loc,0,direction)]
                visited=[]
                while fringe:
                        (curr_move, curr_dist, direction)=fringe.pop(0)
                        visited.append(curr_move)

                        for move in moves(house_map, *curr_move):
                                if house_map[move[0]][move[1]]=="@":
                                        return(curr_dist+1, direction+findmydirection(curr_move,move))

                                else:
                                        if move not in visited:
                                                fringe.append((move, curr_dist+1, direction+findmydirection(curr_move,move)))
                return (-1,'')
        except IndexError:
                print("Please check input")
                exit(-1)
        except TypeError:
                print("Please ")
                exit(-1)
        except Exception :
                print("Invalid character in map")
                exit(-1)
# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Routing in this board:\n" + printable_board(house_map) + "\n")
        print("Shhhh... quiet while I navigate!")

        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + str(solution[1]))



