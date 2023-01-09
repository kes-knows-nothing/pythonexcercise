import turtle
FONT = ("Arial", 24, "normal")


class Name(Turtle):

    def __init__(self):
        self.state_name = ""
        self.penup()
        self.color("black")
        self.write(f"{self.state_name}", align="center", font=FONT)