from turtle import Turtle, Screen

turtle = Turtle()

turtle.shape("turtle")

# x=0
# for i in range(5):
#     turtle.forward(50)
#     turtle.setx(x)
#     x+=10


x=0
move=10
for i in range(15):
    turtle.forward(move)
    turtle.penup()
    turtle.forward(move)
    turtle.pendown()


screen = Screen()
screen.exitonclick()
