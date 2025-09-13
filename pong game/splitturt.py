from turtle import Turtle

class MidLine(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.teleport(0,300)
        self.goto(0,-300)
        self.hideturtle()
        self.speed("fastest")
