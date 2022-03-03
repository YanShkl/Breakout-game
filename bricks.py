from turtle import Turtle
from random import choice



class Target(Turtle):
    colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown', 'white']
    tx, ty = -250, 300
    def __init__(self, x, y):
        super().__init__()
        self.white = False
        self.shapesize(1, 2.5)
        self.color(choice(self.colors))
        self.shape('square')
        self.penup()
        self.goto(x, y)

