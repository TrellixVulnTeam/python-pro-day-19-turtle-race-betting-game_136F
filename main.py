from game_screen import screen
from turtles import turtles, colors
from race import race

screen.title("Turtle Race Betting Game")

user_choice_turtle = screen.textinput(f"Choose your turtle", f"Which turtle are you betting on ?\n{colors}").lower()
winner = race(turtles)
if winner == user_choice_turtle:
    screen.title(f"Your turtle won, congrats!!!! The winner was {winner}.")
else:
    screen.title(f"Sorry, your turtle lost. The winner was {winner}")

screen.exitonclick()
