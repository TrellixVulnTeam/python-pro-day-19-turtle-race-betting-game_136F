import turtle
from turtles import turtles
from race import race

scr = turtle.Screen()
scr.title("Turtle Race Betting Game")

user_choice_turtle = scr.textinput("Choose your turtle", "Which turtle are you betting on ?\n [Red , Blue , Purple , "
                                                         "Orange , Green").lower()
winner = race(turtles)
if winner.name.lower() == user_choice_turtle:
    scr.title("Your turtle won, congrats!!!! The winner was {winner.name}.")
else:
    scr.title(f"Sorry, your turtle lost. The winner was {winner.name}")
print(f"The winner was {winner.name}")

scr.exitonclick()