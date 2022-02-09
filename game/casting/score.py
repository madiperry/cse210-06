"""Score Class lovingly modified by The one and old Nathan S. Hoskins.  Comment placed here to pass DIDT tests."""
from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _name (Str): The player's identifier
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        self.name = ""

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")
    
    def set_player_name(self, name):
        """sets players name
        arguments:
            self -> the class and its attributes and methods
            name -> the on screen name for the player (string)
        Return: Nothing"""
        self.name = name
    def get_player_name(self):
        """Returns player Name for others to see
        Arguments:
            self -> the class and its attributes and methods 
        returns -> Player name (string)"""
        return self.name

    def get_points(self):
        """Returns points for the who wins"""
        return self._points