"""controling snake 1"""
import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        car = cast.get_first_actor("snakes")
        head = car.get_segments()[0]
        position = head.get_position()
        x_position = position.get_x()
        y_position = position.get_y()
        

        # left
        # requires player 1 to be to the right of the left side of the screen to move left
        if 1 < x_position:
            if self._keyboard_service.is_key_down('a'):
                self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        # requires player 1 to be to the left of the middle of the screen to move right
        if x_position < 445:
            if self._keyboard_service.is_key_down('d'):
                self._direction = Point(constants.CELL_SIZE, 0)


        # up
        # if player is not moving left or right it is moving up
        if 0 < x_position < 445:
            if self._keyboard_service.is_key_up('a') and self._keyboard_service.is_key_up('d'):
                self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        #if self._keyboard_service.is_key_down('s'):
            #self._direction = Point(0, constants.CELL_SIZE)
        

        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)
        #snake.grow_tail(1)
