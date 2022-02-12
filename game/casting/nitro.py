"""A class by Nathan S. Hoskins
This class creates a power-up for who ever picks it up"""
import constants
from game.casting.food import Food
from game.shared.point import Point

class Nitro(Food):
    def __init__(self):
        """Sets up the new information"""
        super().__init__()
        self.speedUP = -10
        self.set_color = constants.GREEN
    
    def change_bonus(self, bonus):
        """changes the value of all bonus items spawned from that object
        arguments:
        self -> The class and all it's parts.
        bonus -> a new numerical value (int)
        returns: Nothing"""
        self.speedUP = bonus
    def get_bonus(self):
        """Provides the bonus of the object
        arguments: Self -> the class and all it's parts
        returns: self.speedUP the bonus of a powerup. (int)"""
        return self.speedUP
    def accelerate(self):
        """Sets new velocity
        arguments: self -> the class and all it's parts
        returns: Nothing"""
        speedY = self._velocity.get_y()
        speedY += self.get_bonus()
        speedX = self.get_velocity
        speed = Point(speedX, speedY)
        self.set_velocity(speed)
