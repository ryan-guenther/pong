from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.current_score = 0
        self.speed("fastest")
        self.xcor = xcor
        self.ycor = ycor
        self.update_score()

    def write_text(self, text, xcor, ycor):
        self.goto(xcor, ycor)
        self.write(text, move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        # clear the text
        self.clear()
        self.write_text(self.current_score, self.xcor, self.ycor)

    def add_point(self):
        self.current_score += 1
        self.update_score()