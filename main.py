from turtle import Turtle, Screen
from random import randint

# turtle_race game

tr = Turtle()
sr = Screen()

sr.listen()
sr.setup(width=500, height=400)

is_race_on = False

user_chosen_turtle = sr.textinput("Select a turtle", "write name of your preferred turtle:")
turtle_color_arr = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_direction_arr = [100, 60, 20, -20, -60, -100]
turtle_player_index = []

for turtle_color_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(turtle_color_arr[turtle_color_index])
    new_turtle.goto(x=-230, y=y_direction_arr[turtle_color_index])
    turtle_player_index.append(new_turtle)


if user_chosen_turtle != '' and user_chosen_turtle is not None:
    is_race_on = True

while is_race_on:
    for turtle_player in turtle_player_index:
        if turtle_player.xcor() > 230:
            is_race_on = False
            winning_color = turtle_player.pencolor()
            if winning_color == user_chosen_turtle:
                print(f'you\'ve won the winning color is {winning_color}')
            else:
                print(f'you\'ve lost the winning color is {winning_color}')

        turtle_player.forward(randint(0, 10))



# etch_A_sketch App

# def clear_and_return_home():
#     tr.clear()
#     tr.penup()
#     tr.home()
#     tr.pendown()
#
#
# sr.onkey(fun=lambda: tr.forward(10), key='w')
# sr.onkey(fun=lambda: tr.back(10), key='s')
# sr.onkey(fun=lambda: tr.setheading(tr.heading() + 10), key='a')
# sr.onkey(fun=lambda: tr.setheading(tr.heading() - 10), key='d')
# sr.onkey(fun=clear_and_return_home, key='c')


sr.exitonclick()
