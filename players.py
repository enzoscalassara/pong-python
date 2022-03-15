from turtle import Turtle


class Players:
    def __init__(self):
        self.player = []

    def create_players(self):
        j = 1
        for i in range(2):
            player = Turtle()
            player.goto(-850 * j, 0)
            player.color("white")
            player.penup()
            player.shape("square")
            player.resizemode("user")
            player.shapesize(stretch_wid=6, stretch_len=1, outline=0)
            self.player.append(player)
            j -= 2

    def move_up_p1(self):
        self.player[0].goto((self.player[0].xcor()), ((self.player[0].ycor()) + 20))

    def move_down_p1(self):
        self.player[0].goto((self.player[0].xcor()), (self.player[0].ycor() - 20))

    def move_up_p2(self):
        self.player[1].goto((self.player[1].xcor()), ((self.player[1].ycor()) + 20))

    def move_down_p2(self):
        self.player[1].goto((self.player[1].xcor()), (self.player[1].ycor() - 20))
