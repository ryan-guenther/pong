from game_screen import GameScreen
from paddle import Paddle
from time import sleep
from ball import Ball

GAME_SPEED = 0.1
LEFT_PADDLE_POS = (-350, 0)
RIGHT_PADDLE_POS = (350, 0)

LEFT_PADDLE_KEYUP = "w"
LEFT_PADDLE_KEYDOWN = "d"

RIGHT_PADDLE_KEYUP = "Up"
RIGHT_PADDLE_KEYDOWN = "Down"

# Create the game screen
game_screen = GameScreen()

# Create the paddles on the screen
left_paddle = Paddle(LEFT_PADDLE_POS)
right_paddle = Paddle(RIGHT_PADDLE_POS)

# Add the Ball
ball = Ball()

# Left Paddle Key Events
game_screen.onkey(left_paddle.move_up, LEFT_PADDLE_KEYUP)
game_screen.onkey(left_paddle.move_down, LEFT_PADDLE_KEYDOWN)

# Right Paddle Key Events
game_screen.onkey(right_paddle.move_up, RIGHT_PADDLE_KEYUP)
game_screen.onkey(right_paddle.move_down, RIGHT_PADDLE_KEYDOWN)

# Start the game
game_on = True

while game_on:
    ball.move()
    game_screen.update()
    sleep(GAME_SPEED)


# TODO Add collision for paddle and UPPER and LOWER bounds
# TODO Add collision for ball between UPPER and LOWER wall for bounce
# TODO Add collision for ball and paddles

# TODO add Scoring for ball when passes sides of walls
# TODO Configure and setup Scoreboard

game_screen.exitonclick()