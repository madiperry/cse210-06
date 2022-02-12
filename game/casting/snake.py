"""Draw those slithering friends"""

import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, start_x,start_y,color1, color2, player):
        """init class to start things off"""
        super().__init__()
        self._segments = []
        self.color_one = color1
        self.color_two = color2
        self._prepare_body(start_x,start_y)
        self._start_x = start_x
        self._player = player



    def get_segments(self):
        """ how many segments are there? look no further"""
        return self._segments

    def move_next(self):
        """get this reptile moving"""
        # move all segments

        for segment in self._segments:
                    segment.move_next()
                # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
                trailing = self._segments[i]
                previous = self._segments[i - 1]
                velocity = previous.get_velocity()
                trailing.set_velocity(velocity)


                    

    def get_head(self):
        """WHERE'S THE HEAD, oh there it is."""
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """A growing boy or girl, and this adds the segments as new actors."""
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self.color_two)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """TURN, TURN, TURN"""
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, start_x,start_y):
        """Draw me like one of those french girls, This creates the body segments and adds them to the list"""
        x = int(start_x)
        y = int(start_y)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "3" if i == 0 else "#"
            color = self.color_one if i == 0 else self.color_two
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
