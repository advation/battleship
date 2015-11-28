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
        for row in self.board:
            print " ".join(row)
        #print self.board

    def build_board(self, boardSize):
        for x in range(boardSize+1):
            if x == 0:
                temp = []
                for y in range(boardSize+1):
                   if y == 0:
                       temp.append("  ")
                   else:
                       if y < 10:
                            temp.append(str(y) + " ")
                       else:
                            temp.append(str(y))
                self.board.append(temp)
            else:
                temp = []
                if x is not 0:
                    if x < 10:
                        temp.append(str(x) + " " )
                    else:
                        temp.append(str(x))
                    for c in range(boardSize):
                        temp.append("o ")
                self.board.append(temp)


    def gen_enemy(self, enemyShips):
        x = 1
        while x <= enemyShips:
            enemyShipcoords = [randint(1,boardSize)]
            enemyShipcoords += [randint(1,boardSize)]
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
        shotcoord.append(x)
        shotcoord.append(y)

        if shotcoord in self.enemyPositions:
            self.board[x][y] = "* "

        if shotcoord not in self.shots:
            self.shots.append(shotcoord)
        else:
            self.board[x][y] = "x "

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

    if len(Game.enemyPositions) == len(Game.shots):
        print "Victory is yours!"
        exit();

clearScreen()


print "GAME OVER"
print "Enemy location " + "#" + " | " + "Missed shots " + "x"

for x in Game.enemyPositions:
    Game.board[x[0]][x[1]] = "# "

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
