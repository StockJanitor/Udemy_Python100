from turtle import Screen, Turtle
import random



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
screen.update()

game_is_on= True
while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(20)












screen.exitonclick()