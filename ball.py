import turtle

COLOR = "white"
SHAPE = "circle"
MOVEMENT = 20
SPEED = "fastest"

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(SHAPE)
        self.penup()

        self.color(COLOR)
        self.speed(SPEED)

        self.setheading(37)

    def move(self):
        self.forward(MOVEMENT)