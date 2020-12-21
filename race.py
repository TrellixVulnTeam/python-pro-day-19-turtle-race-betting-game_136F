import random


def race(turtles):
    """Takes in turtles, race turtles and returns winner"""
    won = False
    while not won:
        for turtle in turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
            if turtle.xcor() >= 230:
                return turtle.pencolor()
