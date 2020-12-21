import turtle
import random
from turtles import turtles

scr = turtle.Screen()
y = 100
for turtle in turtles:
    turtle.penup()
    turtle.shape("turtle")
    turtle.setposition(-400, y)
    y -= 50

won = False
while not won:
    racer = random.choice(turtles)
    racer.forward(10)
    print(racer.position())
    if racer.xcor() >= 400:
        won = True
        winner = racer
print(winner.name)

scr.exitonclick()
