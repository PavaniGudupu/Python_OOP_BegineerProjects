from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.title('EtchSketch')
tim.shape('arrow')
tim.pendown()

def move():
    tim.forward(10)

def back():
    tim.backward(10)

def clock():
    tim.right(90)

def anticlock():
    tim.left(90)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key='w', fun=move)
screen.onkey(key='s', fun=back)
screen.onkey(key='d', fun=clock)
screen.onkey(key='a', fun=anticlock)
screen.onkey(key='c', fun=clear)


screen.exitonclick()