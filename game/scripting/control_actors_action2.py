"""controling snake 2"""
import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.control_actors_action import ControlActorsAction

class ControlActorsAction2(ControlActorsAction):
    """
    An input action that controls the 2nd snake.
    
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

        car2 = cast.get_second_actor("snakes")
        head = car2.get_segments()[0]
        position = head.get_position()
        x_position = position.get_x()

        # left
        # requires player 2 to be to the right of the middle of the screen to move left
        # when the 'j' key on the keyboard is pressed it moves the player to the left
        if 455 < x_position:
            if self._keyboard_service.is_key_down('j'):
                self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        # requires player 2 to be to the left of the right side of the screen to move right
        # when the 'l' key on the keyboard is pressed it moves the player to the right
        if x_position < 900:
            if self._keyboard_service.is_key_down('l'):
                self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        # if player is not moving left or right it is moving up
        if 445 < x_position < 900:
            if self._keyboard_service.is_key_up('j') and self._keyboard_service.is_key_up('l'):
                self._direction = Point(0, -constants.CELL_SIZE)
        
        snake = cast.get_second_actor("snakes")
        snake.turn_head(self._direction)
        #snake.grow_tail(1)
