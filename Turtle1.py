import turtle
import random

screen = turtle.Screen()

home = []

# summon 100 turtles
for i in range(0, 200, 1):
    clone = turtle.Turtle()  # create a turtle clone
    home.append(clone)   # add a turtle clone to home list

# iterate home list
for t in home:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.speed(10)
    t.goto(x, y)


screen.mainloop()











