"""without any visuals we might as well be playing a text based game."""
import pyray
import constants
from game.services.map import Background

class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        
        Background()._draw_grid()  #MODIFIC
        Background().draw_lines()
        
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        if "Score" in text:
            pyray.draw_text(text, x, y, font_size, color)
        else:
            self._draw_car_obstacle(x, y)
        
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            if actor.get_text() == "3":
                self.draw_actor2(actor, centered) #MODIFY
            elif actor.get_text() == "@":
                self.draw_actor(actor, centered)
            elif actor.get_text() == "0":
                self.draw_actor(actor, centered)

    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)
            
        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)


    def _draw_midline(self):
            """Draws a line down the middle of the screen."""
            for y in range(0, constants.MAX_Y, (constants.CELL_SIZE * 2)):
                pyray.draw_line(constants.MID_LEFT_X, y, constants.MID_RIGHT_X, y, pyray.WHITE)
                
            #for x in range(0, constants.MAX_X, constants.CELL_SIZE):
                #pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)
                
    def _draw_car(self, x, y):
        """ draw the car over the 'head' """
        self.new_x = x
        self.new_y = y
        Background().draw_car(self.new_x, self.new_y)

    def _draw_car_obstacle(self, x, y):
        """draw the obstacle sprite"""
        self.new_x = x
        self.new_y = y
        Background().draw_car_obstacle(self.new_x, self.new_y)        
    
    def _get_x_offset(self, text, font_size):
        """as the name suggests, offsets the x postion by half of the text"""
        width = pyray.measure_text(text, font_size)
        return int(width / 2)
    
    def draw_actor2(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
        self._draw_car(x, y)

    
    def draw_actor2(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
        self._draw_car(x, y)
        
    def winner(self, player):
        """display winner message"""
        self.player = player
        return pyray.draw_text("PLAYER  " + str(self.player) + "  WIN", 75, 300, 100, pyray.VIOLET)
