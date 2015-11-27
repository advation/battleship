import os
from random import randint

board = []
enemyPositions = []

os.system('clear')
boardSize = int(raw_input("Board Size:"))
turns = int(boardSize * 1.5)
#turns = 1
enemyShips = int(raw_input("Number of enemy ships:"))

for x in range(boardSize):
    board.append([u"\u25A1"] * boardSize)

def print_board(board):
    for row in board:
        print " ".join(row)

for x in range(enemyShips):
    coors = [randint(1,boardSize)]
    coors += [randint(1,boardSize)]
    enemyPositions.append(coors)

lockPositions = enemyPositions

for x in range(turns):
    os.system('clear')
    print "Shot " + str(x+1) + " out of " + str(turns) + "."
    print_board(board)

    user_x = int(raw_input("Target X Coordinate:"))
    user_y = int(raw_input("Target Y Coordinate:"))

    shot = []
    shot.append(user_x)
    shot.append(user_y)

    enemyCount = len(enemyPositions)

    #Need to fix this
    for y in range(enemyCount):
	    k = 0
	    if lockPositions[k] == shot:
	        print "HIT!"
	        board[user_x-1][user_y-1] = "X"
	        enemyPositions.remove(shot)
	    else:
	        print "MISS"
	        board[user_x-1][user_y-1] = u"\u25CF"
	    k+1

    enemyCount = len(enemyPositions)

    if len(enemyPositions) == 0:
        print "Victory is yours!"
        exit();

os.system('clear')
print "GAME OVER"
print "Enemy location " + u"\u25A0"
print "Missed shots " + u"\u25CF"

for x in lockPositions:
    board[x[0]][x[1]] = u"\u25A0"

print_board(board)
exit()
