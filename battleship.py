import os
import time

from random import randint

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

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





class game:

    board = []
    enemyPositions = []
    shots = []
    turns = 0

    def create_game(self, boardSize, enemyShips):
        self.build_board(boardSize)
        self.gen_enemy(enemyShips)
        self.gen_turns(boardSize)

    def print_board(self):
        temp = []
        for x in range(len(self.board)+1):
            if x == 0:
                temp.append("  ")
            elif x < 10:
                temp.append(" " + str(x))
            else:
                temp.append(str(x))
        print " ".join(temp)

        rows = 1
        for row in self.board:
            if rows < 10:
                print str(rows) + "  " + " ".join(row)
            else:
                print str(rows) + " " + " ".join(row)
            rows = rows+1
        #print self.board

    def build_board(self, boardSize):
        for x in range(boardSize):
            self.board.append([" ."] * boardSize)


    def gen_enemy(self, enemyShips):
        x = 1
        while x <= enemyShips:
            enemyShipcoords = [randint(0,boardSize-1)]
            enemyShipcoords += [randint(0,boardSize-1)]
            if enemyShipcoords not in self.enemyPositions:
                self.enemyPositions.append(enemyShipcoords)
                x = x+1

        self._enemyPositons = self.enemyPositions

    def enemyCount(self):
        return len(self.enemyPositions)

    def gen_turns(self, boardSize):
        self.turns = int(boardSize * 1.5)

    def shot(self, x, y):

        shotcoord = []
        shotcoord.append(x-1)
        shotcoord.append(y-1)

        if shotcoord in self.enemyPositions:
            self.board[x-1][y-1] = " *"
        else:
            self.board[x-1][y-1] = " x"

        if shotcoord not in self.shots:
            self.shots.append(shotcoord)

        self.turns = self.turns-1;







Game = game()

while True:
    try:
        boardSize = int(raw_input("Board Size:"))
    except ValueError:
        clearScreen()
        print("This is not a valid entry.")
        continue
    else:
        break

while True:
    try:
        enemyShips = int(raw_input("Number of enemy ships:"))
    except ValueError:
        clearScreen()
        print("This is not a valid entry.")
        continue
    else:
        break

Game.create_game(boardSize, enemyShips)


for x in range(Game.turns):

    clearScreen()
    print "== BATTLESHIP =="
    Game.print_board()
    print "Miss (x) | Hit (*)"
    print "Shots remaining " + str(Game.turns) + "."

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


    Game.shot(user_x, user_y)

    if Game.enemyPositions == Game.shots:
        print "Victory is yours!"
        exit();

clearScreen()

print "GAME OVER"
print "Enemy location " + "#" + " | " + "Missed shots " + "x"

for x in Game.enemyPositions:
    if Game.board[x[0]][x[1]] != " *":
        Game.board[x[0]][x[1]] = " #"

Game.print_board()

while True:
    try:
        answer = raw_input("Exit (y/n)?")
        if answer == "y" or answer == "Y":
            exit()
        else:
            continue
    except ValueError:
        continue
