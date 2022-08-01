from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","green","cyan","blue","purple"]
user_bet = screen.textinput(title="make your bet", prompt="which turtle? ")

def make_turtle(name,num,y):
    name = Turtle(shape="turtle")
    name.penup()
    name.color(colors[num])
    name.goto(x=-230,y=y)




make_turtle("tim",0,-100)
make_turtle("apple",1,-70)
make_turtle("banana",2,-40)
make_turtle("candy",3,-10)
make_turtle("david",4,20)
make_turtle("echo",5,50)
make_turtle("fanny",6,80)

screen.exitonclick()