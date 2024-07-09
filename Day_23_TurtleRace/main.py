from turtle import Turtle, Screen
from car import Car
import random

turtle = Turtle()
screen = Screen()
screen.tracer(0)

game = True

def up():
    turtle.forward(10)

screen.setup(width=600, height=600)
screen.title('Turtle Race Game')
screen.listen()
screen.onkey(up, "Up")

turtle.shape('turtle')
turtle.left(90)
turtle.penup()
turtle.goto(0, -280)


while game:
    screen.update()
    car = Car()
    car.move_cars()

screen.exitonclick()