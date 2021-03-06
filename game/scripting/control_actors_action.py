"""controling snake 1"""
from pyexpat.errors import messages
from game.casting.actor import Actor
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
        player_1_skid_message = Actor()
        car = cast.get_first_actor("snakes")
        head = car.get_segments()[0]
        position = head.get_position()
        x_position = position.get_x()
        y_position = position.get_y()
        message_position = Point(200, 225)
        
        def reset_x_y(thishead):
            """ when we go in the grass the cell_size get's out of sync, this is to reset the values to fix that """
            x = thishead.get_position().get_x()
            y = thishead.get_position().get_y()
            if x % 10 == 1:
                x -= 1
            if x % 10 == 2:
                x -= 2
            if x % 10 == 4:
                x += 1
            if x % 10 == 6:
                x -= 1
            if x % 10 == 7:
                x -= 2
            if x % 10 == 8:
                x += 2
            if x % 10 == 9:
                x += 1

            if y % 10 == 1:
                y -= 1
            if y % 10 == 2:
                y -= 2
            if y % 10 == 4:
                y -= 4
            if y % 10 == 6:
                y -= 1
            if y % 10 == 7:
                y -= 2
            if y % 10 == 8:
                y -= 3
            if y % 10 == 9:
                y -= 4

            position = Point(x, y)
            thishead.set_position(position) 

        # left
        # requires player 1 to be to the right of the left side of the screen to move left
        # when the 'a' key on the keyboard is pressed it moves the player to the left
        
        if self._keyboard_service.is_key_down('a'):
            if 5 < x_position:
                self._direction = Point(-constants.CELL_SIZE * 2, 0)
            else:
                self._direction = Point(0,0)
        
        # right
        # requires player 1 to be to the left of the middle of the screen to move right
        # when the 'd' key on the keyboard is pressed it moves the player to the right
        
        if self._keyboard_service.is_key_down('d'):
            if x_position < 430:
                self._direction = Point(constants.CELL_SIZE * 2, 0)
            else:
                self._direction = Point(0,0)



        # up
        # if player is not moving left or right it is moving up automatically
        if 5  < x_position < 100:
            if self._keyboard_service.is_key_up('a') and self._keyboard_service.is_key_up('d'):
                self._direction = Point(0, -1)
        elif 101 < x_position < 320:

            if self._keyboard_service.is_key_up('a') and self._keyboard_service.is_key_up('d'):
                reset_x_y(head)
                self._direction = Point(0, -constants.CELL_SIZE)
        elif 321 < x_position < 430:
            if self._keyboard_service.is_key_up('a') and self._keyboard_service.is_key_up('d'):
                self._direction = Point(0, -1)
        
        # down
        #if self._keyboard_service.is_key_down('s'):
            #self._direction = Point(0, constants.CELL_SIZE)
        

        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)
        #snake.grow_tail(1)
