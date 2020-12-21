import random


def race(turtles):
    """Takes in turtles, race turtles and returns winner"""
    won = False
    while not won:
        racer = random.choice(turtles)
        racer.forward(5)
        print(racer.xcor())
        if racer.xcor() >= 275:
            won = True
            winner = racer
            return winner
