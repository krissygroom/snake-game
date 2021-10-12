from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# create a new screen - 600 x 600 pixels
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # background color of screen
screen.title("My Snake Game")
# turn of the tracer so we can have a seamless animation:
screen.tracer(0)  # turns off the turtle on the screen


def start_game():
    # ******* Step 1: Create Snake Body *******
    snake = Snake()

    # create the food
    food = Food()

    # create the scoreboard
    scoreboard = Scoreboard()

    # and create listener for key strokes
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    return snake, food, scoreboard


def create_listener(snake):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


# ******* Step 2: Move the Snake *******
game_is_on = True
snake, food, scoreboard = start_game()

while game_is_on:
    screen.update()  # turn the snake on once all the segments have moved forward
    time.sleep(0.1)

    # every time the screen refreshes, we'll get snake to move
    snake.move()

    # ******* Step 3: Control the Snake *******
    # see the screen.listen() and onkey() methods in start_game()

    # ******* Step 4: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # ******* Step 5: Detect collision with wall *******
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False

    # ******* Step 6: Detect collision with your own tail *******
    # if the head collides with any segment, game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False

    if not game_is_on:
        play_again = screen.textinput("", "Would you like to play again? (y or n)").lower()
        if play_again == 'y':
            game_is_on = True
            scoreboard.reset()
            snake.reset()
            food.refresh()
            create_listener(snake)
        else:
            snake.remove_snake()
            food.reset()
            scoreboard.thanks_for_playing()


        





















screen.exitonclick()

