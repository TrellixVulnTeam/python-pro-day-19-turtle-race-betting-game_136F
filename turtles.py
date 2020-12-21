import turtle

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

red_turtle.color("red")
blue_turtle.color("blue")
purple_turtle.color("purple")
orange_turtle.color("orange")
green_turtle.color("green")

turtles = [red_turtle, blue_turtle, purple_turtle, orange_turtle, green_turtle]

y = 100
for each_turtle in turtles:
    each_turtle.penup()
    each_turtle.shape("turtle")
    each_turtle.setposition(-400, y)
    y -= 50
