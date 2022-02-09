""" Test by Jermain Lopez """
from point import Point
from color import Color
import pytest

class Test2:
    """
    class Test2:
    This class checks the inputs and outputs of points on the game plane from X and Y and also checks the color.
    """
    def test_add_point(self):
        """
        test_add_point(): 
        This method tests and verifies that the points are different 
        after adding to their respective x and y components the components of the other point.
        
        """
        for x in range(20):
            for y in range (20):
                self.point1 = Point(x,y)
                self.point_add_1 = self.point1.add(self.point1)
                assert self.point_add_1 != self.point1

    def test_get_x(self):
        """
        test_get_x():
        This method verifies that the x-component is obtained from the required point.
        
        """

        for x in range(20):
            for y in range (20):
                self.point1 = Point(x,y)
                assert x == self.point1.get_x()
    def test_get_y(self):
        """
        test_get_y():
        This method verifies that the y-component is obtained from the required point.
        
        """
        for x in range(20):
            for y in range (20):
                self.point1 = Point(x,y)
                assert y == self.point1.get_y()

    def test_equals(self):
        """
        test_equals():
        This method checks that the x-component and y-component are equal to those of the suggested point.
        """

        for x in range(20):
            for y in range (20):
                self.point1 = Point(x,y)
                assert self.point1.equals(self.point1) == True

    def test_scale(self):
        """
        test_scale():
        This method checks that the x component and y component are multiplied by checking the new position.
        """
        for x in range(20):
            for y in range (20):
                self.point = Point(x,y)
                self.m = list(str(self.point.scale(x)))
                self.z = list(str(Point(x * x, y * x)))
                for i in range(len(self.m)):
                    assert self.m[i] == self.z[i]
    def test_reverse(self):
        """
        test_reverse():
        This method verifies that the x component and y component 
        are multiplied by (-1) to verify that there is a reverse in the plane variables.
        """
        for x in range(20):
            for y in range (20):
                self.point = Point(x,y)
                self.m = list(str(self.point.scale(x)))
                self.z = list(str(Point(x * (-1), y * (-1))))
                for i in range(len(self.m)):
                    assert self.m[i] == self.z[i]

    def test_to_tuple(self):
        """
        test_to_tuple():
        This method verifies that the components of the colo are sent correctly.
        """
        for x in range(20):
            for y in range (20):
                for w in range(20):
                    for z in range(20):
                        color1 = Color(x, y, z, w)
                        color2 = color1.to_tuple()
                        assert (x, y, z, w) == color2

    def print_test2(self):
        print(self.test_add_point.__doc__) 
        print(self.test_get_x.__doc__) 
        print(self.test_get_y.__doc__) 
        print(self.test_equals.__doc__)      
        print(self.test_scale.__doc__) 
        print(self.test_reverse.__doc__)
        print(self.test_to_tuple.__doc__)

test2 = Test2()
test2.print_test2()
pytest.main(["-v", "--tb=line", "-rN", __file__])
