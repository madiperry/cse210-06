import pyray
import random


class Background:


    def _draw_grid(self):
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
        #pyray.draw_line_3d((20,20,20), (40,40,40), pyray.RED)
        """Draws a grid on the screen."""
        
        
    def draw_lines(self):
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
