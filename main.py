import turtle
import random

scr = turtle.Screen()

red_turtle = turtle.Turtle()
blue_turtle = turtle.Turtle()
purple_turtle = turtle.Turtle()
orange_turtle = turtle.Turtle()
green_turtle = turtle.Turtle()

red_turtle.name = "Red"
blue_turtle.name="Blue"
purple_turtle.name = "Purple"
orange_turtle.name = "Orange"
green_turtle.name = "Green"

green_turtle.color("green")
red_turtle.color("red")
blue_turtle.color("blue")
purple_turtle.color("purple")
orange_turtle.color("orange")

turtles = [red_turtle, blue_turtle, purple_turtle, orange_turtle, green_turtle]
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
