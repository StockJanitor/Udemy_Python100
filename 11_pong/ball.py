from turtle import Turtle
Y_DIRECTION = 7
X_DIRECTION = 10



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.y_direction = 1
        self.x_direction = 1


    def move(self):
        new_x = self.xcor()+X_DIRECTION*self.x_direction
        new_y = self.ycor()+Y_DIRECTION*self.y_direction
        self.goto(new_x,new_y)

    def reset_position(self):
        self.goto(0,0)