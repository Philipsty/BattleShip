#!/usr/bin/env python
import math
from PointT import*
from InvalidShipException import*
# Tyler Philips
#April 1 the	work	being	submitted is	your	own	individual	work

#ASSUME: that start coord will have lower value than end coord. otherwise problems occur in constructor
## @brief
class Ships:
    ## @brief This is a constructor method
    # @param l is the length of the ship
    # @param start is the start point of ship
    # @param end is the end point of ship
    # @param holes is a list of the holes in a ship. used to keep track if it is shot or not
    # @param coords is a list of pointT if all the points are valid
    # @param count is a counter variable used to keep track of the position of the coordinate
    def __init__(self,l,start,end):
        coords=[None]*l

        if(start.dist(end)==l-1):#check to see if the ship is of proper size
            count = 0
            if(start.xcrd()==end.xcrd()):#if vertical
                for i in range(start.ycrd(),end.ycrd()+1):
                    coords[count]=PointT(start.xcrd(),i)
                    count+=1

            elif (start.ycrd() == end.ycrd()):#if horizontal
                for i in range(start.xcrd(), end.xcrd()+1):
                    coords[count] = PointT(i, start.ycrd())
                    count+=1
            else:
                raise InvalidShipException()

            self.holes = [0] * l
            self.coords=coords
        else:
            raise InvalidShipException()

    # @brief this function returns a list of coordinates for the ship
    # @return self.coords
    def getCoords(self):
        return self.coords

    #takes point p and tells if it hit
    # @param count is used to keep track of the location that the ship has been hit
    def isHit(self,p):
        count=0
        for x in self.coords:#goes through eacho point on ship
            if(p.xcrd()==x.xcrd() and p.ycrd()==x.ycrd()):#if same point
                self.holes[count]=1#mark hit location on ship
                return True
            count+=1

        return False

    # @brief checks to see if the ship is sunk
    # @param holes is a int list that holds ones  and 0's which tell if the ship has been shot
    # 1 means hit, 0 means not hit
    def isSunk(self):

        #check to see if all the holes have been shot
        for x in self.holes:
            if (x==0):  # not hit
                return False
        return True



