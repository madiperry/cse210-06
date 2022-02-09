from food import Food

class Obsticle(Food):
    def __init__(self):
        super().__init__()
        self.penality = -10
        