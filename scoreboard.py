from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    # # class var
    # high_score = 0

    def __init__(self):
        super().__init__()
        # turtle that knows how to keep score and can display it
        # 1) keep track of the score
        self.score = 0
        with open("data.txt", 'r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        # this order mattered - needed to make it goto before writing it
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write("Score = {}   High Score = {}".format(self.score, self.high_score), align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def thanks_for_playing(self):
        self.goto(0, 0)
        self.write("Thanks for playing!", align=ALIGNMENT, font=FONT)

