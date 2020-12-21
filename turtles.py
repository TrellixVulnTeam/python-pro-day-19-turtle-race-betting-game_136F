import turtle

colors = ["red", "orange", "yellow", "green", "indigo", "purple"]
turtles = []
y = 100
for each_color in colors:
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(each_color)
    new_turtle.name = each_color
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y -= 30
    turtles.append(new_turtle)

