from turtle import Turtle, Screen
import random

screen = Screen()
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
position = [-70, -40, -10, 20, 50, 80]
game = False
all_turtle = []

screen.title('Turtle Racing')
screen.setup(500, 400)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


for i in range(0, 6):    
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x= -230 , y=position[i])
    all_turtle.append(new_turtle)

if user_bet:
    game = True

while game:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            game = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()