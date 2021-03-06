"""Without movement, why are we even playing? This is what this class does."""

from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        #snake1 = cast.
        #snake2 = cast.
        for actor in actors:
            print(actor)
            actor.move_next()
            #snake.grow_tail(points)