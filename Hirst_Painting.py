import random
from turtle import Turtle, Screen
tom = Turtle()
tom.speed('fastest')
tom.hideturtle()

coloring = ["Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral",
            "CornflowerBlue", "Crimson", "DarkBlue", "DarkGoldenRod", "DarkGray", "DarkGreen", "DarkMagenta"]
tom.penup()
tom.setheading(220)
tom.forward(350)
tom.left(140)


def just():
    for _ in range(10):
        tom.color(random.choice(coloring))
        tom.penup()
        tom.forward(50)
        tom.pendown()
        tom.begin_fill()
        tom.circle(10, 360)
        tom.end_fill()


just()

i = 1
do = 8
while i < do:
    tom.penup()
    tom.setheading(90)
    tom.forward(60)
    tom.setheading(180)
    tom.forward(500)
    tom.setheading(0)
    tom.pendown()
    just()
    i += 1


screen = Screen()
screen.exitonclick()
