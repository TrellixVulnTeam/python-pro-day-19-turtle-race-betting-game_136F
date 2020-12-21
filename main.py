import turtle
import random

scr = turtle.Screen()

Raphael = turtle.Turtle()
Leonardo = turtle.Turtle()
Donatello = turtle.Turtle()
Michelangelo = turtle.Turtle()
Roshi = turtle.Turtle()

Roshi.color("green")
Raphael.color("red")
Leonardo.color("blue")
Donatello.color("purple")
Michelangelo.color("orange")

turtles = [Raphael, Leonardo, Donatello, Michelangelo, Roshi]
y = 100
for turtle in turtles:
    turtle.penup()
    turtle.shape("turtle")
    turtle.setposition(-400, y)
    y -= 50

scr.exitonclick()
