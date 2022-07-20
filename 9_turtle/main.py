import turtle as t
import random
import colorgram


color_list = ["blue","deep sky blue", "cornflower blue","cyan","aquamarine","sea green","spring green", "lime green","chartreuse","yellow","brown","red","orange","pink","tomato","purple","slate blue"]



turtle = t.Turtle()
t.colormode(255)

turtle.shape("turtle")
turtle.speed("fastest")
turtle.pensize(2)
direction_list = [0,90,180,270]

num = 50
angle = 360/num
for i in range(0,num):
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    turtle.color((r,g,b))
    turtle.circle(120)
    turtle.left(angle)

# turtle.forward(35)
# turtle.left(random.choice(direction_list))

screen = t.Screen()
screen.exitonclick()
