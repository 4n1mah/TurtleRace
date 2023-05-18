from turtle import Turtle, Screen
import random

game_on = False
screen = Screen()
screen.setup(width=720, height=600)
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'pink', 'orange', 'black', 'brown']
y_position = [-70, -40, -10, 20, 50, 80, 110, 140, 170]
turtles = []

for turtle in range(0, 9):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-345 - 10, y=y_position[turtle])
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Make a bet", prompt="Who do you think will win? Enter a color: ")
if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() > 330:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)

screen.exitonclick()
