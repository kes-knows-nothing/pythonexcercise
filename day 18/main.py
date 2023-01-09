from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("purple")
color = ["Blue", "Red", "Yellow", "Green", "Pink", "Silver", "Gold", "Purple", "Black", "SlateGray"]

def make_figure():
        tim.fd(100)
        tim.right(360 / number)


for number in range(3, 11):
        count = 0
        tim.color(random.choice(color))
        while count < number:
                count += 1
                make_figure()

screen = Screen()
screen.exitonclick()

