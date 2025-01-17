import turtle

COLOR = "white"
SHAPE = "square"
MOVEMENT = 20
SPEED = "fastest"

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__(SHAPE)
        self.penup()

        self.shapesize(stretch_wid = 5, stretch_len=1, outline=None)
        self.color(COLOR)
        self.penup()
        self.speed(SPEED)

        self.setpos(position)


    def move_up(self):
        new_ycor = self.ycor() + MOVEMENT
        self.setpos(self.xcor(), new_ycor)


    def move_down(self):
        new_ycor = self.ycor() + MOVEMENT
        self.setpos(self.xcor(), self.ycor() - MOVEMENT)