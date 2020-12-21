import random


def race(turtles):
    """Takes in turtles, race turtles and returns winner"""
    while True:
        for turtle in turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
            if turtle.xcor() >= 255:
                return turtle.pencolor()
