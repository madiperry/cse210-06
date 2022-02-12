"""This class is the speed reducing obstacle of the racing game.
Class by Nathan S. Hoskins"""
from game.casting.nitro import Nitro
from game.shared.point import Point
import constants

class Blockage(Nitro):
    def __init__(self) -> None:
        """Init.  Sets up class
        Arguments:
        Self -> The class and all of it's componets"""
        super().__init__()
        self.speedDown = 10
    def get_bonus(self):
        """polymorphed get for speed penalty
        Arguments: none
        returns speedDown -> int"""
        return self.speedDown
    def accelerate(self):
        """this implimention polymporphs the pervious version
        This is designed to impliment the penalty
        arguments: self -> the class and all it's parts
        returns: Nothing"""
        speedY = self._velocity.get_y()
        speedY += self.get_bonus()
        speedX = self.get_velocity
        speed = Point(speedX, speedY)
        self.set_velocity(speed)
    