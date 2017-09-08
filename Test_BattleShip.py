#Tyler Philips
#!/usr/bin/env python
import unittest
from PointT import*
from Board import*
from Ships import*
from BattleShip import*
# Tyler Philips
#April 1 the	work	being	submitted is	your	own	individual	work


class Test_BattleShip(unittest.TestCase):

    #pointT tests#####################################################################################################

    ## @brief This function tests the xcrd() function in pointADT.py
    #  @ param point point is a pointT object that is used to test the xcrd()
    def test_xcrd(self):
        point=PointT(3,4)
        self.assertTrue(point.xcrd()==3 )
        print("test_xcrd() passed.\nxcrd=3\n...")

    ## @brief This function tests the ycrd() function in pointADT.py
    #  @ param point point is a pointT object that is used to test the ycrd()
    def test_ycrd(self):
        point=PointT(3,4)
        self.assertTrue(point.ycrd()==4 )
        print("test_ycrd() passed.\nycrd=4\n...")


    ## @brief This function tests the dist() function in pointADT.py
    #  @ param point point is a pointT object that is used to test the distance
    #  @ param point2 point is another pointT object that is used to test the distance
    def test_dist(self):
        point=PointT(3,4)
        point2 = PointT(1, 4)
        self.assertTrue(point.dist(point2)==2 )
        print("test_dist() passed.\ndist=2\n...")

    ## @brief This function tests the rot() function in pointADT.py
    #  @ param point point is a pointT object that is used to test the distance
    def test_isValid(self):
        #test 1 test to trigger pointException
        point=PointT(10,4)
        board = Board()
        self.assertTrue(point.isValid(board.upper()))
        print("test_isValid() 1 passed.\n...")

    ## @brief This function tests the ycrd() function in pointADT.py
    #  @ param point point is a pointT object that is used to test the ycrd()
    def test_lower(self):
        b=Board()
        lowerBoard = [["_"] * 11 for i in range(9)]
        self.assertTrue(b.lower() == lowerBoard)
        print("test_lower() passed.\nycrd=4\n...")

    ## @brief This function tests the upper() function in Board.py
    #  @ param b is a Board() object
    def test_upper(self):
        b = Board()
        upperBoard = [["_"] * 11 for i in range(9)]
        self.assertTrue(b.upper() == upperBoard)
        print("test_upper() passed.\nycrd=4\n...")

    ## @brief This function tests the printLower() function in Board.py
    #  @ param b is a Board() object
    def test_printLlower(self):
            b = Board()
            b.printLower()
            print("test_printLower() passed.\ndist=2\n...")

    ## @brief This function tests the printUpper() function in Board.py
    #  @ param b is a Board() object
    def test_printUpper(self):
        b = Board()
        b.printUpper()
        print("test_printUpper() passed.\ndist=2\n...")

    ## @brief This function tests the placeShip() function in Board.py
    #  @ param b is a Board() object
    #  @ param lower is a 2-d list
    #  @ param ship is a Ships() object
    def test_placeShip(self):
            point = PointT(10, 4)
            b = Board()
            lower=[["_"]*11 for i in range(9)]
            lower[0][0]="s"
            lower[0][1]="s"
            ship=Ships(2,PointT(0,0),PointT(1,0))
            b.placeShip(ship.getCoords())

            self.assertTrue(lower==b.lower())
            print("test_placeShip() 1 passed.\n...")

    ## @brief This function tests the hitShip() function in Board.py
    #  @ param b is a Board() object
    #  @ param lower is a 2-d list
    #  @ param point is a PointT() object
    def test_hitShip(self):
            lower = [["_"] * 11 for i in range(9)]
            lower[3][9] = "d"
            #enter a point at position(10,4)
            point = PointT(10-1, 4-1)
            b = Board()
            b.hitShip(point)
            self.assertTrue(b.lower()==lower)
            print("test_hitShip() 1 passed.\n...")

    ## @brief This function tests the markUpper() function in Board.py
    #  @ param b is a Board() object
    #  @ param upper is a 2-d list
    #  @ param point is a PointT() object
    def test_markUpper(self):
        upper = [["_"] * 11 for i in range(9)]
        upper[3][9] = "x"
        # enter a point at position(10,4)
        point = PointT(10 - 1, 4 - 1)
        b = Board()
        b.markUpper(point)
        self.assertTrue(b.upper() == upper)
        print("test_markUpper() 1 passed.\n...")

    ## @brief This function tests the getCoords() function in Ships.py
    #  @ param ship is a Ships() object
    #  @ param start is a PointT() object.START OF SHIP
    #  @ param end is a PointT() object.end OF SHIP
    def test_getCoords(self):
            start = PointT(ord("A")-65, int(1)-1)
            end = PointT(ord("B")-65, int(1)-1)
            ship=Ships(2,start,end)

            expected=[start,end]
            coords=ship.getCoords()

            self.assertTrue(coords[0].xcrd()==expected[0].xcrd() and coords[0].ycrd()==expected[0].ycrd()and
                            coords[1].xcrd()==expected[1].xcrd() and coords[1].ycrd()==expected[1].ycrd())
            print("test_getCoords() 1 passed.\n...")

    ## @brief This function tests the isHIt() function in Ships.py
    #  @ param ship is a Ships() object
    #  @ param start is a PointT() object.START OF SHIP
    #  @ param end is a PointT() object.end OF SHIP
    def test_isHIt(self):
        start = PointT(ord("A") - 65, int(1) - 1)
        end = PointT(ord("B") - 65, int(1) - 1)
        ship = Ships(2, start, end)

        self.assertTrue(ship.isHit(start))
        print("test_isHIt() 1 passed.\n...")

    ## @brief This function tests the isSunk() function in Ships.py
    #  @ param ship is a Ships() object
    #  @ param start is a PointT() object.START OF SHIP
    #  @ param end is a PointT() object.end OF SHIP
    def test_isSunk(self):
        #make ship
        start = PointT(ord("A") - 65, int(1) - 1)
        end = PointT(ord("B") - 65, int(1) - 1)
        ship = Ships(2, start, end)
        ship.isHit(start)#shoot the ship twice and sink it

        ship.isHit(end)

        self.assertTrue(ship.isSunk())
        print("test_isSunk() 1 passed.\n...")


   # There is no way to test BattleSip.py because none of the functions take input or return values

if __name__=='__main__':
    unittest.main()