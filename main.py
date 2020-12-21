import turtle
from turtles import turtles, colors
from race import race

scr = turtle.Screen()
scr.title("Turtle Race Betting Game")

user_choice_turtle = scr.textinput(f"Choose your turtle", f"Which turtle are you betting on ?\n{colors}").lower()
winner = race(turtles)
if winner.name.lower() == user_choice_turtle:
    scr.title(f"Your turtle won, congrats!!!! The winner was {winner.name}.")
else:
    scr.title(f"Sorry, your turtle lost. The winner was {winner.name}")

scr.exitonclick()
