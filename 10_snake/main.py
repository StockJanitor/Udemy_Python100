from turtle import Screen, Turtle
import random



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")














screen.exitonclick()