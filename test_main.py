""" Test by Jermain Lopez """
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.shared.color import Color
from game.shared.point import Point
import pytest

class Test_car:
    """class to test the cast functions of main."""
    #Test Cast

    def test_add_actor(self):
        """
        test_add_actor():
        This method checks the creation of multiple objects to determine if they will be different.
        """

        for x in range(5):
            for y in range(5):
                cast = Cast()
                car_1 = Actor()
                position = Point(x, y)
                car_1.set_text("S1")
                car_1.set_font_size(3)
                car_1.set_color("blue")
                car_1.set_position(position)
                cast.add_actor("car1", car_1)
                actor1 = cast.get_actors("car1")

                cast2 = Cast()
                Car_ = Actor()
                position2 = Point(y + x, x * y)
                Car_.set_text("S2")
                Car_.set_font_size(3)
                Car_.set_color("red")
                Car_.set_position(position2)
                cast2.add_actor("car2", Car_)
                actor2 = cast2.get_actors("car2")
                assert actor1 != actor2
    #actor test

    def test_get_color(self):
        """
        test_get_color():
        This method verifies that the actor safely starts the color and its return is similar to the one started.
        """
        for i in range(20):
            color1 = Color(255, 255, 255)
            color2 = Color(i * 5, i * 4, i * 3)
            assert color1.to_tuple() != color2.to_tuple()

    def test_get_font_size(self):
        """
        test_get_font_size():
        This method verifies that the actor returns the ideal size for artifacts.
        """
        car_1 = Actor()
        car_2 = Actor()
        assert car_1.get_font_size() == car_2.get_font_size() 



    def test_get_text(self):
        """
        test_get_text():
        This method verifies that the actor returns the desired text to be used for subsequent groups of artifacts.
        """
        car_list = ["car1", "car2", "car3", "car4", "car5", "car6"]
        list_last_names = ["Owen", "Lopez", "Terwilleger", "Hoskins", " Hartfield", "Platt"]
        for i in range(len(car_list)):
            car_1 = Actor()
            car_1.set_text(car_list[i])
            text1 = car_1.get_text()
            car_2 = Actor()
            car_2.set_text(list_last_names[i])
            text2 = car_2.get_text()
            assert text1 != text2


    def get_velocity(self):
        """
        get_velocity():
        This method verifies that the velocity and position are always different at a point in the plane.
        """
        for i in range(50):
            car_actor = Actor()
            assert car_actor.get_velocity()  != car_actor.get_position()  
    
    def print_test3(self):
        """printing out the results"""
        print(self.test_add_actor.__doc__)
        print(self.test_get_color.__doc__) 
        print(self.test_get_font_size.__doc__) 
        print(self.test_get_text.__doc__) 
        print(self.get_velocity.__doc__)      
         
        pytest.main(["-v", "--tb=line", "-rN", __file__])

main_test = Test_car()
main_test.print_test3()
