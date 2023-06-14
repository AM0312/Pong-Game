from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(pos_x, pos_y)

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)
