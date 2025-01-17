from turtle import Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"
GAME_TITLE = "Pong"

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(SCREEN_COLOR)
        self.screen.title(GAME_TITLE)
        self.screen.listen()

    def exitonclick(self):
        self.screen.exitonclick()

    def onkey(self, fun, key):
        self.screen.onkey(fun, key)