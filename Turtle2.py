# Two spinning triangles animation

import turtle
import time

# setup the screen
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("#6bb391")


t1 = turtle.Turtle()
t1.color("magenta")
t1.shape("triangle")
t1.shapesize(5)

angle1 = 0
timer = 0
cooldown1 = 10
cooldown2 = 20


while True:
    # the bg is only allowed to change color if timer > cooldown
    timer = timer + 1

    if timer > cooldown1:
        t1.color("#5eff00")

    if timer > cooldown2:
        t1.color("#2c7502")
        timer = 0

    angle1 = angle1 + 10
    t1.setheading(angle1)


screen.mainloop()
















