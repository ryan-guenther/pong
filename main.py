from game_screen import GameScreen
from paddle import Paddle
from time import sleep
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCORE_BOUNDARY_POS = SCREEN_WIDTH / 2

GAME_SPEED = 0.1

# Paddles will be offset slightly from the sides of the screen
PADDLE_OFFSET = 0.0625
PADDLE_DEFAULT_POS = SCREEN_WIDTH / 2 - int(SCREEN_WIDTH * PADDLE_OFFSET)

# Paddle boundary will be the default position, subtracting half the width of the paddle
PADDLE_BOUNDARY_POS = PADDLE_DEFAULT_POS - 30

LEFT_PADDLE_POS = (-PADDLE_DEFAULT_POS, 0)
RIGHT_PADDLE_POS = (PADDLE_DEFAULT_POS, 0)

LEFT_PADDLE_KEYUP = "w"
LEFT_PADDLE_KEYDOWN = "s"

RIGHT_PADDLE_KEYUP = "Up"
RIGHT_PADDLE_KEYDOWN = "Down"

# Wall is Ball Width away from the top or bottom
WALL_POS = SCREEN_HEIGHT / 2 - 20

# Create the game screen
game_screen = GameScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

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

    # if ball hit the wall then a bounce is required
    if abs(ball.ycor()) > WALL_POS:
        ball.wall_bounce()

    # Detect collision with paddle
    if abs(ball.xcor()) > PADDLE_BOUNDARY_POS and (ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50):
        ball.paddle_bounce()

    # Reset Ball if Score Zone Hit
    if abs(ball.xcor()) > SCORE_BOUNDARY_POS:
        ball.reset()


# TODO add Scoring for ball when passes sides of walls
# TODO Configure and setup Scoreboard

game_screen.exitonclick()