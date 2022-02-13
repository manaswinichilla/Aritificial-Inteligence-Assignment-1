_**A bit of an Intro**_: 

This is Manaswini Chilla. I am 2018 UG-CS passout. I have been in production support and testing in the past 2 years. I have had a significant gap in prgramming, I am new to GIT, python etc but this assignment, was super fun and helpful to spark the budding programmer in me. 


**_Status of my progress_**: 

I was able to do a decent job with program for route pichu and arrange pichu. the arrange pichu program works for extra credit requirements as well. I have tested this code to some extent with some basic test cases. 

_**Acknowledgement**_: 

Before moving on to the assignment description, I would like to take up some space here to thank Professor David Crandall and the AIs for this platform, after attempting to solve the assignment I am fairly certain that I will be a much better programmer and problem solver by the end of this course.

_**Route Pichu**_:

**`Statespace`**: All "." places on the board where pichu can be placed

**`Initial state`**: one pichu on the board and an "@" on the board 

**`Goal state`**: number of steps to reach the goal state and a string with concatinated directions to get to the goal state

**`Successor function`**: returns list of coordinates in up, down, right, left directions where the pichu can move from its current location

**`Cost function`**: distance between two points can be considered as 1 unit. it is uniform throughout. 

**_Startegy_**:

While thinking of the strategy for this, first thing was to make sure visited states are not being visited again. Therefore I created a list visited, and before adding any state to fringe, it is checked whether it is already in visited.While the fringe is not empty, A state is popped from fringe and stored in (curr_move, curr_dist) the curr move will have the indices of state where pichu could move and curr_dist is the distance it has covered so far to this state. We traverse the successors from this, using a loop, “move” for each state, “moves” for set of successor states,  to find if we reach our goal state. If “move” is not the goal state and not in visited, the curr_dist ( which is zero initially) is appended by one, and stored in the tuple and this entry is appended in the fringe. So I figured, along with this distance, we could update the path too. I added the “direction” variable to the tuple(which is “” intially) , and each time an entry is made in the fringe this direction is appended with a Letter (R,U,D, or L) that is returned by a function ( findMyDirection) based on curr_move and move passed to it. if the move in successors is the goal state, we do one final update to the curr_state and direction and return this. If no solution is found [-1,’’] is returned. Also, after thorough testing, it came to my attention that BFS might be a better approach to get the solution, hence instead of fringe.pop() I used fringe.pop(0), so that FIFO(queue) strategy is implemented. 

**_Brief description of functions:_**

**`def parse_map(filename)`**:
Parses the map from a given filename

**`def printable_board(board):`**
Returns a string with the board rendered in a human/pichu-readable format

**`def valid_index(pos, n, m):`**
Checks if a row,col index pair is on the map, and also if it is ".".

**`def moves(map, row, col)`**: [successor function]
Finds the possible moves from position (row, col)

**`def findmydirection(curr, move):`**
this function, based on states given to it, returns direction from 1'st parameter to the second parameter either Left "L", Right "R", Up "U", or Down "D

**`def search(house_map):`**
This function takes single parameter as input  “the house map” and returns a tuple of the form (move_count, move_string), where  move_count is the number of moves required to navigate from start to finish, or -1  if no such route exists and move_string is a string indicating the path, consisting of U, L, R, and D characters. 


--------------------------------------------------------------------------------------------------------

**_Arrange Pichus_**:

**`State space:`** All possible boards where pichus are placed on "." places on the board.

**`Initial state`**: one pichu on the board and an "@" on the board 

**`Goal state:`** K pichus placed on the board such that no 2 pichus are on the same row or column without an X(s) or @ between them. 

**`Successor function:`** returns list s in up, down, right, left directions where the pichu can move from its current location

**`Cost function:`**  A board should be returned with k pichus on it without violating the row/column rule. A cost function has not been taken into consideration in this particular problem. 

**_Strategy_**: 

While thinking of the strategy for this, I created visitedBoards[] to make sure already visited boards are not being considered before being added to the fringe. I created a function (checkViolationOfRowsColumns) which, when board, row and column number is passed to it, it checks along the row and along the column and returns 0 if pichu can be placed at that coordinate or 1 otherwise. I am calling this function in add_pichu method, ie, everytime a pichu is added to a board, it makes sure that a pichu is not already there in the row/column without @/X in between. Now coming to the solve function, which is similar to the search function in route_pichu, while the fringe is not empty, we pop from the fringe store it in “s”, get the successor boards from s, which is in “successors”. The successor function, runs 2 loops, scans the entire “s”, and at which ever location it sees a “.”, it sends those coordinates to add_pichu. Add_pichu calls the check function I created to see if that point is safe to place. In this way, a bunch of safe boards are returned from the successor function. We traverse through these successors in the solve function, check if it is the goal state. If it is not, we confirm that it is not in visitedBoards list before we append it to fringe and visitedBoards. If s is  the goal state, we can confirm that right number of pichus are on the board and this gets returned.  If a goal state is never found we simply return ([],False).

**_For extra Credit:_**

The requirements of extra credit that were different from above were the fact that diagonals also need to be checked, and we need to enter maximum number of pichus. For diagonals, I created a similar function one for rows/columns called “checkViolationOfDiagonals” which from coordinate checks in left up, left down, right up right down directions, if there are 2 pichus with no X or @ in between them it returns a number greater than 0, else it returns 0, this is combined with the row/column check in the addpichu function. When k is given as 0, from the solve, solveForExtraCredit function is called, 0 is passed to the successor function, successor function takes the 0 in extraCredit variable and passes it to add_pichu, in add_pichu if the extraCredit variable is 0 then diagonals are checked. In the solveForExtraCredit function, we are running a while loop starting from k=1, and each time the success is checked, if it is true the loop continues by incrementing k. as soon as we encounter success as false, we exit out of the loop and get the map for k-1 and return it. 

**_Breif description of functions:_**

**`def parse_map(filename):`**
Parses the map from a given filename

**`def count_pichus(board):`**
Counts total number of pichus on board

**`def printable_board(board):`**
Returns a string with the board rendered in a human-pichuly format

**`def checkViolationOfRowsColumns(board, row, col):`**
this function based on the coordinates row,col, traverses the row and column, if there are no 2 pichus that don’t have X or @ between them it returns 0 else it returns a number greater than 0 

**`def checkViolationofDiagonals(board, row, col):`**
this function based on the coordinates row,col, traverses the left up, left down, right down, right up, diagonals if there are no 2 pichus that don’t have X or @ between them it returns 0 else it returns a number greater than 0

**`def add_pichu(board, row, col, extraCredit):`**
Adds a pichu to the board at the given position, if rows and columns are safe, if extraCredit passed to this function has the value 0 then diagonals are also checked before placing the pichu at row,col and returns the new board. If any violations are there, it returns the board passed to it as it is.

**`def successors(board, extraCredit):`**
Gets list of successors of given board state, the extraCredit parameter is passed to the add_pichu method.

**`def is_goal(board, k):`**
checks if board is a goal state

**`def solveForExtraCredit(initial_board, k):`**
This function, does the same thing as solve, except it calls add pichu function with extra credit value as 0 so that diagonals are checked for the extra credit requirements. 

**`def solve(initial_board, k):`**
This function takes two parameters as input the house map and the value k and returns a tuple of the form (new_map, success), where new_map is a new version of the map with k agents,  success is True if a solution was found, and False otherwise.if k is 0 then it calls the solveForExtraCredit function.


-----------------------------------------------------------------------------------------------------------------------

**_What I am proud of:_**

I was able to recognize that BFS was a better approach for solving the route pichu problem as it gives the optimal path from p to @ in any map given to it. Also I feel I have done a decent job with exception handling in the program. If the map dimensions are incorrect, or if there is a weird character in the map, or if k is less than zero, the program is capable of handling these exceptions.

**_What I need to improve:_**

one of the many advantages of python  the fact that we can compress a lot of the code and write in single lines, having a lesser grip on python I often found myself typing mutiple lines of code. There is also a scope for improvement in time management, and documentation. Also, in the arrange pichu while solving for extra credit I called another function because i couldnt think of another way, other than using a global variable. There may be a way to use the same solve function to do this. I regret that I couldnt dedicate time to think through this possibility.Also, I couldnt dedicate time to explore the possibility of priority queue and heuristic functions. With these in place may be I could have reduced the running time by a significant amount.Last but not the least, I pushed the last solutions to GIT, and realised that I should have kept pushing code as and when possible, and that version control is a blessing in disguise :) 

**_Citations:_**

https://www.w3schools.com/python/ - python tutorial

Any python related syntax errors including exception handling, I took help from the above link.

https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/ - diagonals 

For the extra credit, for checking in the diagonals, I took help from the above site to understand the ranges of the loops to traverse the diagonals in all 4 directions

Aritificial Intelligence- Peter Norvig and Stuart J. Russell

I went through the textbook to go ver the concept of BFS, DFS