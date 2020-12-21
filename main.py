import turtle
import random
from turtles import turtles

scr = turtle.Screen()
scr.title("Turtle Race Betting Game")
y = 100
for turtle in turtles:
    turtle.penup()
    turtle.shape("turtle")
    turtle.setposition(-400, y)
    y -= 50

user_choice_turtle = scr.textinput("Choose your turtle", "Which turtle are you betting on ?\n [Red , Blue , Purple , "
                                                         "Orange , Green").lower()

won = False
while not won:
    racer = random.choice(turtles)
    racer.forward(10)
    if racer.xcor() >= 400:
        won = True
        winner = racer
        if winner.name.lower() == user_choice_turtle:
            print("Your turtle won, congrats")
        else:
            print("Sorry, your turtle lost")
        print(f"The winner was {winner.name}")

scr.exitonclick()
