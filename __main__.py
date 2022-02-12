"""Functions to start the game"""

import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.snake import Snake
from game.casting.nitro import Nitro
from game.casting.blockage import Blockage
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.control_actors_action2 import ControlActorsAction2
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.obstacle import Obstacle

def main():
    """ start the game already"""
    # create the cast
    cast = Cast()
    cast.add_actor("nitros", Nitro())
    cast.add_actor("obstacles", Blockage())
    cast.add_actor("snakes", Snake(205,400,constants.RED,constants.RED, 'player1'))
    cast.add_actor("snakes", Snake(675,400,constants.BLUE,constants.BLUE, 'player2'))

    cast.add_actor("scores", Score())
    cast.add_actor("scores", Score())
    score2 = cast.get_second_actor("scores")
    x = int(constants.MAX_X -100)
    y = 0
    position = Point(x, y)
    score2.set_position(position)
    #cast.add_actor("foods", Food())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlActorsAction2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
