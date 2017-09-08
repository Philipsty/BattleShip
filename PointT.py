#!/usr/bin/env python
import math
from InvalidPointException import*
# Tyler Philips
#April 1 the	work	being	submitted is	your	own	individual	work

#this class dealas with shots and points on the ships

## @brief PointT is a class that creates a point object with an x and y coordinate with various function that can be applied to it
## The constructor PointT is called for each abstract object before any other access routine is called for that object. The constructor cannot be called on an existing object.
class PointT:
    ## @brief This is a constructor method that initializes a PointT's x and y cordinates
    # @param x x is the x coordinate of the point its a string
    # @param y y is the y coordinate of the point its a string
    # num is the int form of x
    def __init__(self,x,y):
        if((0<=x and x<=11) and(0<=y and y<=9)):
            self.x = x
            self.y = y
        else:
            raise InvalidPointException()


    ## @brief This function returns a given PointT's x coordinate
    #  @ param return returns the x value of the point(float)
    def xcrd(self):
        return self.x
    ## @brief This function returns a given PointT's y coordinate
    #  @ param return returns the y value of the point(float)
    def ycrd(self):
        return self.y

    ## @brief this tests if the point is allowed. if it has not already been inputted
    #
    # @param p2 p2 is a PointT object that will be in the distance calculations
    # @param x1 x1 is the x coordinate of the first point
    # @param upper is the upperboard of the user whos atacking
    def isValid(self,upper):
        print upper[self.y][self.x]
        if(upper[self.y][self.x]=="x"):
            raise InvalidPointException()
        return True

    ## @brief This function caluates the distance between 2 point objects and returns it
    # @param p2 p2 is a PointT object that will be in the distance calculations
    # @param x1 x1 is the x coordinate of the first point
    # @param x2 x2 is the x coordinate of the second point
    # @param y1 y1 is the y coordinate of the first point
    # @param y2 y2 is the y coordinate of the second point
    #  @ param return returns the distance between the 2 point objects(float)
    def dist(self,p2):
        x2,x1=p2.x,self.x
        y2,y1=p2.y,self.y
        return (((x2 - x1)**2)+((y2-y1)**2))**.5