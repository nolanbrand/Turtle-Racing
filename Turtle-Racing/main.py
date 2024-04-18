from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.title('Turtle Racing!')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
all_turtles = []


def ask_user_bet():
    valid_input = False
    while not valid_input:
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? 'red', 'orange', 'yellow', "
                                                                  "'green', 'blue', 'violet' \nEnter a color: ").lower()
        if user_bet in colors:
            valid_input = True
            return user_bet


def create_turtles():
    y = -100
    for turtle_index in range(len(colors)):
        new_turtle = Turtle('turtle')
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y)
        y += 40
        all_turtles.append(new_turtle)


def play_again(winning_turtle):
    valid_input = False
    while not valid_input:
        if winning_turtle == user_input_bet:
            user_continue = screen.textinput(title="Play again?",
                                             prompt=f"You've won! The {winning_turtle} turtle is the "
                                                    f"winner! \nPlay again 'yes', or 'no': ").lower()
        else:
            user_continue = screen.textinput(title="Play again?",
                                             prompt=f"You've lost! The {winning_turtle} turtle is the "
                                                    f"winner! \nPlay again 'yes', or 'no': ").lower()

        if user_continue == 'yes':
            valid_input = True
            return True
        elif user_continue == 'no':
            valid_input = True
            return False


def move_forward(input_turtle):
    rand_num = random.randint(0, 10)
    input_turtle.forward(rand_num)


def move_right(input_turtle):
    rand_num = random.randint(0, 1)
    input_turtle.right(rand_num)


def move_left(input_turtle):
    rand_num = random.randint(0, 1)
    input_turtle.left(rand_num)


def random_move(input_turtle):
    move_dict = {
        0: move_forward(input_turtle),
        1: move_left(input_turtle),
        2: move_right(input_turtle)
    }

    rand_num = random.randint(0, 2)

    return move_dict[rand_num]


user_play_again = True

while user_play_again:

    create_turtles()
    user_input_bet = ask_user_bet()
    is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if play_again(winning_color):
                    for i in range(6):
                        all_turtles[i].hideturtle()
                    all_turtles = []

                else:
                    screen.bye()
            random_move(turtle)
