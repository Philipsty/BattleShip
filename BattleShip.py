from PointT import*
from Ships import*
from Board import*
# Tyler Philips
#April 1 the	work	being	submitted is	your	own	individual	work


#ASSUME: there are 2 real players. No cpu
## @brief this class has functinos that bring the other classes together and create a game
## @param boardsP1 is board abject for player 1. it keeps track of their state
## @param boardsP2 is board abject for player 2. it keeps track of their state
## @param shipsP1 is a list of ship objects for player 1
## @param shipsP2 is a list of ship objects for player 2
## The constructor PointT is called for each abstract object before any other access routine is called for that object. The constructor cannot be called on an existing object.

class BattleShip:
#start up
#give each player a board and a list of ships
    #they will have to decide the locations for the ship


    global boardsP1,boardsP2,shipsP1,shipsP2
    boardsP1= Board()
    boardsP2= Board()
    shipsP1=[None]*5
    shipsP2 = [None] *5

    ## @brief this function runs one turn for player 1
    ## @param word is a string input of the players shot
    ## @param shot is a pointT object of the shot
    ## @param x is string used to split word
    ## @param y is string used to split word
    ## @param hit is a boolean value that keeps track if the shot hit a ship
    ## @param shipsP2 is a list of ship objects for player 2
    ## @param boardsP1 is board abject for player 1. it keeps track of their state
    def turnP1(self):
        #take input point maybe check for validity if it has already been done
        print"\nP1's turn:"
        print "P1: upper board "
        boardsP1.printUpper()
        print "P1: lower board "
        boardsP1.printLower()

        #TAKE SHOT INPUT
        word = raw_input('P1 enter your shot: ')
        x, y = word.split(",")
        shot = PointT(ord(x)-65, int(y)-1)
        hit=False#keeps track of hit, used for output to screen

        if(shot.isValid(boardsP1.upper())):#if valid shot
            #add mark to upperboard 1
            boardsP1.markUpper(shot)

            #if its a hit mark lowerboard 2 adn to the ship that got hit
            for x in shipsP2:
                if(x.isHit(shot)):
                    boardsP2.hitShip(shot)#mark player 2s game board if their ship is hit
                    hit=True
                    break
        if(hit):print"Direct Hit!"
        else:print"Missed!"

    ## @brief this function runs one turn for player 2
    ## @param word is a string input of the players shot
    ## @param shot is a pointT object of the shot
    ## @param x is string used to split word
    ## @param y is string used to split word
    ## @param hit is a boolean value that keeps track if the shot hit a ship
    ## @param shipsP1 is a list of ship objects for player 1
    ## @param boardsP2 is board abject for player 2. it keeps track of their state
    def turnP2(self):
        #take input point maybe check for validity if it has already been done
        print"\nP2's turn:"
        print "P2: upper board "
        boardsP2.printUpper()
        print "P2: lower board "
        boardsP2.printLower()

        #TAKE SHOT INPUT
        word = raw_input('P2 enter your shot: ')
        x, y = word.split(",")
        shot = PointT(ord(x)-65, int(y)-1)
        hit = False  # keeps track of hit, used for output to screen

        if(shot.isValid(boardsP2.upper())):#if valid shot
            #add mark to upperboard 1
            boardsP2.markUpper(shot)

            #if its a hit mark lowerboard 2 adn to the ship that got hit
            for x in shipsP1:
                if(x.isHit(shot)):
                    boardsP1.hitShip(shot)#mark player 2s game board if their ship is hit
                    hit = True
                    break

        if (hit):
            print"Direct Hit!"
        else:
            print"Missed!"

    ## @brief this function creates the ships for each player
    ## @param word is a string input of the players shot
    ## @param p1 is a pointT object that is start of ship
    ## @param p2 is a pointT object that is end of ship
    ## @param x is string used to split word
    ## @param y is string used to split word
    ## @param x2 is string used to split word
    ## @param y2 is string used to split word
    ## @param ship is ship object
    ## @param shipLengths isan array that stores the length of the 5 ships for each user
    ## @param shipsP1 is a list of ship objects for player 1
    ## @param shipsP2 is a list of ship objects for player 2
    ## @param boardsP1 is board abject for player 1. it keeps track of their state
    ## @param boardsP2 is board abject for player 2. it keeps track of their state
    def setup(self):
            print"BATTLESHIP\n____________________________________________________________"
            shipLengths=[2,3,3,4,5]
            #get ships
            ##get SHIPS FOR P1

            print"Player 1..."
            for i in range(0,5):
                word = raw_input("Enter the starting point and end point of ship (eg.A,1,A,3):")
                x,y,x2,y2=word.split(",")
                p1,p2=PointT(ord(x)-65,int(y)-1),PointT(ord(x2)-65,int(y2)-1)#MAKE START AND END POINT OF SHIP
                ship=Ships(shipLengths[i],p1,p2)#MAKE SHIP
                boardsP1.placeShip(ship.getCoords())#MARK SHIP LOCATION ON GAMEBOARD
                shipsP1[i]=ship

            print "P1: lower"
            boardsP1.printLower()

            print"Player 2..."
            for i in range(0, 5):
                word = raw_input("Enter the starting point and end point of ship (eg.A,1,A,3):")
                x, y, x2, y2 = word.split(",")
                p1, p2 = PointT(ord(x) - 65, int(y) - 1), PointT(ord(x2) - 65,int(y2) - 1)  # MAKE START AND END POINT OF SHIP
                ship = Ships(shipLengths[i], p1, p2)  # MAKE SHIP
                boardsP2.placeShip(ship.getCoords())  # MARK SHIP LOCATION ON GAMEBOARD
                shipsP2[i] = ship

            print "P2: lower"
            boardsP2.printLower()


    ## @brief this function returns a boolean based on if someone has one the game or not
    ## @param p2Won is a boolean value used to keep track of whether p2 won the game of not
    ## @param p1Won is a boolean value used to keep track of whether p1 won the game of not
    ## @param p1 is a pointT object that is start of ship
    ## @param shipsP1 is a list of ship objects for player 1
    ## @param shipsP2 is a list of ship objects for player 2
    ## @return boolean on if game is over or not
    def finished(self):
        p2Won=False
        p1Won=False

        #check if p2 won
        for ship in shipsP1:#check each of p1's ships to see if they are all sunk
            if(ship.isSunk()):
                p2Won=True
            else:
                p2Won=False
                break
        # check if p1 won
        for ship in shipsP2:
            if(ship.isSunk()):#check each of p2's ships to see if they are all sunk
                p1Won=True
            else:
                p1Won=False
                break
        #return boolean value and print output based on if statements
        if(p1Won):
            print "P1 has won!"
            return True
        elif(p2Won):
            print "P2 has won!"
            return True
        else:
            return False

# @brief this function builds the game together, it calls all the other functions in BattleShip.py to setup and continue
#the game until finished returns True
def play():
        game = BattleShip()
        game.setup()
        while (not game.finished()):  # continue game until there is a victor
            game.turnP1()
            if (game.finished()): break  # if player one just defeated p2 end game
            game.turnP2()



#this will be the main function for this class. it will call all the other functions to play the game
def main():

        play()


if __name__=='__main__':
    main()