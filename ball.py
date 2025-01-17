import turtle
from random import randint

COLOR = "white"
SHAPE = "circle"
MOVEMENT = 10
SPEED = "fastest"

def random_direction():
    value = randint(0, 1)
    if value == 0:
        return MOVEMENT
    else:
        return -MOVEMENT

def random_angle(current_direction = None):
    if current_direction is None:
        value = random_direction()
    else:
        value = current_direction

    y_value = randint(3,10)

    if value > 0:
        return y_value
    else:
        return -y_value

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(SHAPE)
        self.penup()

        self.color(COLOR)
        self.speed(SPEED)

        self.x_movement = random_direction()
        self.y_movement = random_angle()


    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)


    def wall_bounce(self):
        self.y_movement *= -1


    def paddle_bounce(self):
        self.x_movement *= -1


    def reset(self):
        # When resetting then the ball should start the other direction
        self.paddle_bounce()
        self.y_movement = random_angle(self.y_movement)
        self.goto(0,0)