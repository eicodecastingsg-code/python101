import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Swaying Flower Animation")
pen = turtle.Turtle()

# turn off screen refresh (auto screen update)
screen.tracer(0)

def draw_flower(angle):
    # draw stem
    pen.hideturtle()
    pen.pensize(10)
    pen.color("SpringGreen")
    pen.penup()
    pen.goto(0, -300)
    pen.setheading(90)
    pen.pendown()

    # draw in steps
    for i in range(100):
        pen.forward(4)
        pen.right(angle)



curvature = 0
step = 0.1

while True:
    # erase existing drawing
    pen.clear()

    # draw a flower
    draw_flower(curvature)
    curvature = curvature + step

    if curvature > 1:
        step = -0.1
    elif curvature < -1:
        step = 0.1

    time.sleep(0.1)

    # refresh screen to present the graphic
    screen.update()





screen.mainloop()





















