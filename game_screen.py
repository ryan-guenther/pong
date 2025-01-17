from turtle import Screen

SCREEN_COLOR = "black"
GAME_TITLE = "Pong"

class GameScreen:
    def __init__(self, width, height):
        self.screen = Screen()
        self.screen.setup(width=width, height=height)
        self.screen.bgcolor(SCREEN_COLOR)
        self.screen.title(GAME_TITLE)
        self.screen.listen()

        # Remove the Tracer, now need to update the screen manually
        self.screen.tracer(0)

    def exitonclick(self):
        self.screen.exitonclick()

    def onkey(self, fun, key):
        self.screen.onkey(fun, key)

    def update(self):
        self.screen.update()