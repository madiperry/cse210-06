""" Test by Jermain Lopez """
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.shared.color import Color
from game.shared.point import Point
import pytest

class Test4:
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
                snake_1 = Actor()
                position = Point(x, y)
                snake_1.set_text("S1")
                snake_1.set_font_size(3)
                snake_1.set_color("blue")
                snake_1.set_position(position)
                cast.add_actor("Snake1", snake_1)
                actor1 = cast.get_actors("Snake1")

                cast2 = Cast()
                snake_2 = Actor()
                position2 = Point(y + x, x * y)
                snake_2.set_text("S2")
                snake_2.set_font_size(3)
                snake_2.set_color("red")
                snake_2.set_position(position2)
                cast2.add_actor("Snake2", snake_2)
                actor2 = cast2.get_actors("Snake2")
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
        snake1 = Actor()
        snake2 = Actor()
        assert snake1.get_font_size() == snake2.get_font_size() 



    def test_get_text(self):
        """
        test_get_text():
        This method verifies that the actor returns the desired text to be used for subsequent groups of artifacts.
        """
        snakes = ["Snake1", "Snake2", "Snake3", "Snake4", "Snake5", "Snake6"]
        list_last_names = ["Owen", "Lopez", "Terwilleger", "Hoskins", " Hartfield", "Platt"]
        for i in range(len(snakes)):
            snake_1 = Actor()
            snake_1.set_text(snakes[i])
            text1 = snake_1.get_text()
            snake_2 = Actor()
            snake_2.set_text(list_last_names[i])
            text2 = snake_2.get_text()
            assert text1 != text2


    def get_velocity(self):
        """
        get_velocity():
        This method verifies that the velocity and position are always different at a point in the plane.
        """
        for i in range(50):
            sanke = Actor()
            assert sanke.get_velocity()  != sanke.get_position()  
    
    def print_test3(self):
        """printing out the results"""
        print(self.test_add_actor.__doc__)
        print(self.test_get_color.__doc__) 
        print(self.test_get_font_size.__doc__) 
        print(self.test_get_text.__doc__) 
        print(self.get_velocity.__doc__)      
         
        pytest.main(["-v", "--tb=line", "-rN", __file__])

main_test = Test4()
main_test.print_test3()
