import turtle as t
import random as r

t.colormode(255)

def random_color():
    red,green,blue=r.randint(0,255),r.randint(0,255),r.randint(0,255)
    return red, green, blue


tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")

dimension = r.randint(5,10)
size_distance = dimension


for a in range(0,dimension):
    for i in range(0,dimension):
        tim.dot(size_distance,(random_color()))
        tim.penup()
        tim.forward(size_distance*2)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(size_distance*2)
    tim.pendown()
    tim.right(90)
    tim.setheading()
    





screen = t.Screen()
screen.exitonclick()
