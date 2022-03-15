from turtle import Screen
from players import Players
import time


game_over = False


screen = Screen()
screen.setup(width=1800, height=900)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


players = Players()
players.create_players()


# Inputs
screen.listen()
screen.onkeypress(key="w", fun=players.move_up_p1)
screen.onkeypress(key="s", fun=players.move_down_p1)
screen.onkeypress(key="Up", fun=players.move_up_p2)
screen.onkeypress(key="Down", fun=players.move_down_p2)

while not game_over:
    screen.update()
    time.sleep(0.01)










screen.exitonclick()
