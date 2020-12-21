import random


def race(turtles):
    """Takes in turtles, race turtles and returns winner"""
    won = False
    while not won:
        racer = random.choice(turtles)
        racer.forward(10)
        if racer.xcor() >= 400:
            won = True
            winner = racer
            return winner
