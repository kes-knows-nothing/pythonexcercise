import random
import turtle
import turtle as t
from turtle import Screen
import math

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
color_list = [(0, 0, 0), (49, 102, 191), (142, 89, 39), (188, 41, 80), (106, 189, 123), (69, 119, 192), (46, 106, 79),
              (240, 208, 80), (170, 4, 63), (61, 40, 64), (201, 100, 159), (201, 110, 161), (199, 68, 59),
              (117, 154, 192), (86, 104, 19), (185, 156, 132), (224, 172, 190), (56, 46, 71), (167, 207, 178),
              (175, 186, 218), (132, 142, 93), (62, 53, 79), (107, 142, 125), (226, 174, 166), (74, 139, 179),
              (179, 195, 201)]
tim.penup()



def one_line():
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.fd(50)


go = 0
a = 0

while a < 10:

    for i in range(10):
        one_line()
    go += 50
    tim.goto(math.sqrt(125), go)
    a += 1
tim.hideturtle()








screen = Screen()
screen.exitonclick()

