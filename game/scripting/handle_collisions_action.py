"""setting what happens when they start hitting eachother."""
import constants
from game.services.video_service import VideoService
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.winner = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            self._handle_top_collision(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")
        nitro = cast.get_first_actor("nitros")
        food = cast.get_first_actor("foods")
        food2 = cast.get_second_actor("foods") #ADDED
        obstacle = cast.get_first_actor("obstacles")
        obstacle2 = cast.get_second_actor("obstacles") #ADDED
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")   # added
        head = snake.get_segments()[0]
        head2 = snake2.get_segments()[0]   # added
        
        if head.get_position().equals(nitro.get_position()):
            nitro.accelerate()
            nitro.reset()
        elif head2.get_position().equals(nitro.get_position()):
            nitro.accelerate()
            nitro.reset()
        elif head.get_position().equals(food.get_position()):
            points = food.get_points()                          # added     
            score1.add_points(points)                                # added       
            food.reset() 
            food2.reset() 
            obstacle.reset()                                     # added     
            obstacle2.reset()     
        elif head2.get_position().equals(food.get_position()):
            points = food.get_points()                          # added     
            score2.add_points(points)                                # added       
            food.reset()  
            food2.reset() 
            obstacle.reset() 
            obstacle2.reset() 
        elif head.get_position().equals(food2.get_position()):
            points = food2.get_points()                          # added     
            score1.add_points(points)                                # added       
            food.reset() 
            food2.reset() 
            obstacle.reset()                                # added   
            obstacle2.reset()       
        elif head2.get_position().equals(food2.get_position()):
            points = food2.get_points()                          # added     
            score2.add_points(points)                                # added       
            food.reset() 
            food2.reset() 
            obstacle.reset() 
            obstacle2.reset() 
        elif head2.get_position().equals(obstacle.get_position()):   # added
            points = obstacle.get_points()                          # added     
            score2.add_points(points)                                # added       
            food.reset() 
            food2.reset() 
            obstacle.reset()
            obstacle2.reset() 
        elif head.get_position().equals(obstacle.get_position()):   #cahnged head2
            points = obstacle.get_points()                          # added     
            score1.add_points(points)                                # added       
            obstacle.reset() 
            food.reset() 
            food2.reset() 
            obstacle.reset()    
            obstacle2.reset()                                  # added  
        elif head.get_position().equals(obstacle2.get_position()):
            points = food2.get_points()                          # added     
            score1.add_points(points)                                # added       
            food.reset() 
            food2.reset() 
            obstacle.reset()  
            obstacle2.reset()                               # added         
        elif head2.get_position().equals(obstacle2.get_position()):
            points = food2.get_points()                          # added     
            score2.add_points(points)                                # added       
            food.reset() 
            food2.reset() 
            obstacle.reset() 
            obstacle2.reset()

        if score1.get_points() >= 1000:
            self._is_game_over = True
            self.winner = 1    
        elif score2.get_points() >= 1000:
            self._is_game_over = True
            self.winner = 2 


    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes") # added

        head = snake.get_head()
        head2 = snake2.get_head() # added

        segments = snake.get_segments()[1:]
        segments2 = snake2.get_segments()[1:] # added

        for segment in segments:
            if head2.get_position().equals(head.get_position()):     # If snake 2 hits snake 1 
                score2.add_points(50)


        for segment in segments2:                                      # added
            if head.get_position().equals(head.get_position()):     # if snake 1 hits snake 2
                score1.add_points(50)

    


    def _handle_top_collision(self, cast):
        """Updates the score when car collides with the top of screen.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_second_actor("snakes")

        head = snake.get_head()
        head2 = snake2.get_head() # added
        top = 0
        
        if head.get_position().equals2(top):
                points = 100
                score1.add_points(points)

        if head2.get_position().equals2(top):
                points = 100
                score2.add_points(points)
        if score1.get_points() >= 1000:
            self._is_game_over = True
            self.winner = 1    
        elif score2.get_points() >= 1000:
            self._is_game_over = True
            self.winner = 2 

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            snake2 = cast.get_second_actor("snakes") # added

            segments2 = snake2.get_segments() # added
            segments = snake.get_segments()
            #food = cast.get_first_actor("foods")
            obstacle = cast.get_first_actor("obstacles")
            food = cast.get_first_actor("foods")
            
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            winnerbanner = VideoService()

            message = Actor()
            if self.winner == 1:
                message.set_color(constants.RED)
                message.set_text("Game Over! Player 1 wins!")
                winnerbanner.winner(1)
            if self.winner == 2:
                message.set_color(constants.BLUE)
                message.set_text("Game Over! Player 2 wins!")
                winnerbanner.winner(2)
            if self.winner == 3:
                message.set_color(constants.YELLOW)

                message.set_text("Game Over! It was a tie!")
                
            message.set_position(position)
            cast.add_actor("messages", message)
            winnerbanner = VideoService()
