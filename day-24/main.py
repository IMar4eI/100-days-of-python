from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake: Snake = Snake()
food: Food = Food()
scoreboard: Scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
print("[START] Simulation loop initialized at 10Hz frequency")

try:
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if (snake.head.xcor() > 285 or snake.head.xcor() < -285 or
            snake.head.ycor() > 285 or snake.head.ycor() < -285):
            scoreboard.reset_score()
            snake.reset_snake()


        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_score()
                snake.reset_snake()
except Exception as fatal_exception:
    print(f"[FATAL] Application runtime thread crashed: {fatal_exception}")
finally:
    print("[INFO] Synchronizing remaining logs. Thread safely terminated.")

screen.exitonclick()
