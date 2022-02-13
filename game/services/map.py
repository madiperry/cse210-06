""" Background by Jermain Lopez """
import pyray
import random


class Background:
    """
    class Background:
    This class creates the game background for better viewing.
    """


    def _draw_grid(self):
        """
        _draw_grid(self):
        Draws a grid on the screen.
        """
        pyray.draw_rectangle(0, 0, 100, 600, pyray.GREEN)
        pyray.draw_rectangle(100, 0, 30, 600, pyray.WHITE)
        pyray.draw_rectangle(100, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(125, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(130, 0, 170, 600, pyray.GRAY)
        pyray.draw_rectangle(300, 0, 30, 600, pyray.WHITE)
        pyray.draw_rectangle(300, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(325, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(330, 0, 100, 600, pyray.GREEN)



        pyray.draw_rectangle(470, 0, 100, 600, pyray.GREEN)
        pyray.draw_rectangle(570, 0, 30, 600, pyray.WHITE)
        pyray.draw_rectangle(570, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(595, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(600, 0, 170, 600, pyray.GRAY)
        pyray.draw_rectangle(770, 0, 30, 600, pyray.WHITE)
        pyray.draw_rectangle(770, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(795, 0, 5, 600, pyray.BLACK)
        pyray.draw_rectangle(795, 0, 105, 600, pyray.GREEN)

        
        
    def draw_lines(self):
        """
        draw_lines(self):
        This method draws the lines of the track to give visibility of the movement.
        """

        self.X = random.randint(0, 1)
        if self.X == 0:
            for y in range(0, 600, 100):
                pyray.draw_line_bezier((210, y), (210, 30 +  y), 8, pyray.WHITE )
        if self.X == 1:
            for y in range(50 , 600, 100):
                pyray.draw_line_bezier((210, y), (210,  30 + y), 10, pyray.WHITE )
                    
        if self.X == 0:
            for y in range(0, 600, 100):
                pyray.draw_line_bezier((680, y), (680, 30 +  y), 8, pyray.WHITE )
        if self.X == 1:
            for y in range(50 , 600, 100):
                pyray.draw_line_bezier((680, y), (680,  30 + y), 10, pyray.WHITE )

                
    def draw_car(self, x , y):
        """
        draw_car(self, x , y):
        This method draws both cars for the output screen.
        """

        self.new_x = x
        self.new_y = y
        pyray.draw_line_bezier((self.new_x, self.new_y -20 ), (self.new_x,  self.new_y), 20, pyray.RED)
        pyray.draw_line_bezier((self.new_x-20, self.new_y ), (self.new_x-20, self.new_y+20), 10, pyray.BLACK)
        pyray.draw_line_bezier((self.new_x+20,  self.new_y), (self.new_x+20 , self.new_y+20), 10, pyray.BLACK)
        pyray.draw_line_bezier((self.new_x-20, self.new_y+30 ), (self.new_x-20, self.new_y+50), 10, pyray.BLACK)
        pyray.draw_line_bezier((self.new_x+20, self.new_y+30 ), (self.new_x+20, self.new_y+50), 10, pyray.BLACK)  
        pyray.draw_line_bezier((self.new_x , self.new_y ), ( self.new_x , self.new_y + 50 ), 30, pyray.RED)
        pyray.draw_line_bezier(( self.new_x , self.new_y-15 ), (self.new_x , self.new_y), 25, pyray.RED)
        pyray.draw_line_bezier((self.new_x, self.new_y-5 ), (self.new_x , self.new_y+8), 22, pyray.BLUE)
        pyray.draw_line_bezier((self.new_x-5  , self.new_y+15), (self.new_x-5 , self.new_y+45), 8, pyray.BLUE)
        pyray.draw_line_bezier((self.new_x+5, self.new_y+15), (self.new_x+5 , self.new_y+45), 8, pyray.BLUE)
        pyray.draw_line_bezier((self.new_x , self.new_y+27), (self.new_x , self.new_y+33), 30, pyray.RED)


    def draw_car_obstacle(self, x , y):
        """
        draw_car_obstacle(self, x , y):
        This method draws obtacles cars for the output screen.
        """
        self.new_x = x
        self.new_y = y
        pyray.draw_line_bezier((self.new_x, self.new_y -20 ), (self.new_x,  self.new_y), 20, pyray.YELLOW)
        pyray.draw_line_bezier((self.new_x-20, self.new_y ), (self.new_x-20, self.new_y+20), 10, pyray.BLACK)
        pyray.draw_line_bezier((self.new_x+20,  self.new_y), (self.new_x+20 , self.new_y+20), 10, pyray.BLACK)
        pyray.draw_line_bezier((self.new_x-20, self.new_y+30 ), (self.new_x-20, self.new_y+50), 10, pyray.BLACK)
        pyray.draw_line_bezier((self.new_x+20, self.new_y+30 ), (self.new_x+20, self.new_y+50), 10, pyray.BLACK)  
        pyray.draw_line_bezier((self.new_x , self.new_y ), ( self.new_x , self.new_y + 50 ), 30, pyray.YELLOW)
        pyray.draw_line_bezier(( self.new_x , self.new_y-15 ), (self.new_x , self.new_y), 25, pyray.YELLOW)
        pyray.draw_line_bezier((self.new_x, self.new_y-5 ), (self.new_x , self.new_y+8), 22, pyray.BLUE)
        pyray.draw_line_bezier((self.new_x-5  , self.new_y+15), (self.new_x-5 , self.new_y+45), 8, pyray.BLUE)
        pyray.draw_line_bezier((self.new_x+5, self.new_y+15), (self.new_x+5 , self.new_y+45), 8, pyray.BLUE)
        pyray.draw_line_bezier((self.new_x , self.new_y+27), (self.new_x , self.new_y+33), 30, pyray.YELLOW)
        pyray.draw_text("$", x - 10, y, 40, pyray.BLACK)     
    
