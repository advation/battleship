import os

from random import randint

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    for row in board:
        print " ".join(row)

board = []
enemyPositions = []

clearScreen()

print "                                             |__"
print "                                             |\/"
print "                                             ---"
print "                                             / | ["
print "                                      !      | |||"
print "                                    _/|     _/|-++'"
print "                                +  +--|    |--|--|_ |-"
print "                             { /|__|  |/\__|  |--- |||__/"
print "                            +---------------___[}-_===_.'"
print "                        ____`-' ||___-{]_| _[}-  |     |_[___\==--"
print "         __..._____--==/___]_|__|_____________________________[___\==--____,---------7"
print "        |                                 BATTLESHIP                                /"
print "         \_________________________________________________________________________/"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

while True:
    try:
        boardSize = int(raw_input("Board Size:"))
    except ValueError:
        clearScreen()
        print("This is not a valid entry.")
        continue
    else:
        break

turns = int(boardSize * 1.5)

while True:
    try:
        enemyShips = int(raw_input("Number of enemy ships:"))
    except ValueError:
        clearScreen()
        print("This is not a valid entry.")
        continue
    else:
        break

for x in range(boardSize):
    board.append(["o"] * boardSize)

for x in range(enemyShips):
    coors = [randint(1,boardSize)]
    coors += [randint(1,boardSize)]
    enemyPositions.append(coors)

lockPositions = enemyPositions

for x in range(turns):

    clearScreen()

    print "== BATTLESHIP =="
    print_board(board)
    print "Miss (x) | Hit (*)"
    print "Shots remaining " + str(turns) + "."

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
        board[user_x-1][user_y-1] = "*"
        position = int(enemyPositions.index(shot))
        for b in range(len(enemyPositions)):
            if b == position:
                del enemyPositions[b]
    else:
        board[user_x-1][user_y-1] = "x"

    enemyCount = len(enemyPositions)

    if len(enemyPositions) == 0:
        print "Victory is yours!"
        exit();

    turns = turns-1;

clearScreen()

print "GAME OVER"
print "Enemy location " + "#" + " | " + "Missed shots " + "x"

for x in lockPositions:
    board[x[0]][x[1]] = "#"

print_board(board)

while True:
    try:
        answer = raw_input("Exit (y/n)?")
        if answer == "y" or answer == "Y":
            exit()
        else:
            continue
    except ValueError:
        continue
