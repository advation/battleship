import os
from random import randint

board = []
enemyPositions = []

os.system('clear')

while True:
    try:
        boardSize = int(raw_input("Board Size:"))
    except ValueError:
        os.system('clear')
        print("This is not a valid entry.")
        continue
    else:
        break

turns = int(boardSize * 1.5)

while True:
    try:
        enemyShips = int(raw_input("Number of enemy ships:"))
    except ValueError:
        os.system('clear')
        print("This is not a valid entry.")
        continue
    else:
        break

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

    while True:
        try:
            user_x = int(raw_input("Target X Coordinate:"))
            if user_x > boardSize or user_x < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("ERROR: Value must be numeric and between 1 and "+str(boardSize))
            continue
        else:
            break

    while True:
        try:
            user_y = int(raw_input("Target Y Coordinate:"))
            if user_y > boardSize or user_y < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("ERROR: Value must be numeric and between 1 and "+str(boardSize))
            continue
        else:
            break

    shot = []
    shot.append(user_x)
    shot.append(user_y)

    enemyCount = len(enemyPositions)

    if shot in enemyPositions:
        board[user_x-1][user_y-1] = "X"
        position = int(enemyPositions.index(shot))
        for b in range(len(enemyPositions)):
            if b == position:
                del enemyPositions[b]
    else:
        board[user_x-1][user_y-1] = u"\u25CF"

    #Uncomment for DEV
    #print enemyPositions

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
