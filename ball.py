import turtle

COLOR = "white"
SHAPE = "circle"
MOVEMENT = 10
SPEED = "fastest"

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(SHAPE)
        self.penup()

        self.color(COLOR)
        self.speed(SPEED)

        self.x_movement = 10
        self.y_movement = 10


    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)


    def wall_bounce(self):
        self.y_movement *= -1


    def paddle_bounce(self):
        self.x_movement *= -1

    def reset(self):
        self.goto(0,0)