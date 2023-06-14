from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def bounce_wall(self):
        self.ymove *= -1

    def bounce_paddle(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.move_speed = 0.1
