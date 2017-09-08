#!/usr/bin/env python
import math
from PointT import*
# Tyler Philips
#April 1 the	work	being	submitted is	your	own	individual	work

#ASSUME: size of each board is 11x 9
## @brief PointT is a class that creates a point object with an x and y coordinate with various function that can be applied to it
## The constructor PointT is called for each abstract object before any other access routine is called for that object. The constructor cannot be called on an existing object.
class Board:

    ## @brief This is a constructor that creates an upper board and lower board of 11x11
    # @param upperBoard is a 2D list that holds the values in the upperboard of a player.shows shots fired
    # @param lowerBoard is a 2D list that holds the values in the lower board of a player. shows ship location and damages
    def __init__(self):
        self.lowerBoard=[["_"]*11 for i in range(9)]
        self.upperBoard=[["_"]*11 for i in range(9)]

    ## @brief This function returns a given PointT's x coordinate
    #  @ param return returns the x value of the point(float)
    #  @return returns the 2D list called lowerBoard
    def lower(self):
        return self.lowerBoard

    # @brief this funciton prints the lower board. which shows the ships and hits
    # @param lowerBoard is a 2D list that holds the values in the lower board of a player. shows ship location and damages
    def printLower(self):
        print "   -----------------------------------------------------"
        for x in reversed(range(9)):
            print x + 1, self.lowerBoard[x]
        print "   -----------------------------------------------------"
        print "    A    B    C    D    E    F    G    H    I    J    K "

    # @brief this funciton prints ship onto board
    # @param coords is a list of PointTs that are the points of the given ship
    def placeShip(self,coords):
        #mark each spot where the ship is located with an "s"
        for x in coords:
            self.lowerBoard[x.ycrd()][x.xcrd()]="s"

    # @brief marks the spot on ship that has been damaged
    # @param shot is the coordinate of damaged ship
    def hitShip(self,shot):
        #mark spot with 'd' for damaged
        self.lowerBoard[shot.ycrd()][shot.xcrd()]="d"

    # @brief this funciton returns a 2D array list called upperBoard
    # @param upperBoard is a 2D list that holds the values in the upperboard of a player
    # @return self.upperBoard
    def upper(self):
        return self.upperBoard

    # @brief this funciton prints the upper board. which shows shots made
    # @param upperBoard is a 2D list that holds the values in the upperboard of a player
    def printUpper(self):
        print "   -----------------------------------------------------"

        for x in reversed(range(9)):
            print x+1,self.upperBoard[x]

        print "   -----------------------------------------------------"
        print "    A    B    C    D    E    F    G    H    I    J    K "

    # @brief this function marks the players upper board with an x so they can see the shots they have made so far
    # @param p is a pointT that is the shot the player made to opoonent
    def markUpper(self, p):
        self.upperBoard[p.ycrd()][p.xcrd()]="x"#x stands for fired




