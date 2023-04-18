from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x, new_y = self.xcor() + self.x_move, self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    # hits top wall - x sign no change, y sign change decreases
    # hits bottom wall - y sign changes
