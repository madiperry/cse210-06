"""drawing the positions of the actors"""

from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")
        food = cast.get_first_actor("foods")
        food2 = cast.get_second_actor("foods") #CAHNGE
        obstacle = cast.get_first_actor("obstacles")
        obstacle2 = cast.get_second_actor("obstacles") #CAHNGE
        

        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")
        segments = snake.get_segments()
        segments2 = snake2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actor(food2) #CAHNGE
        self._video_service.draw_actor(obstacle2) #CAHNGE
        self._video_service.draw_actor(obstacle)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
        self._video_service._draw_midline()
