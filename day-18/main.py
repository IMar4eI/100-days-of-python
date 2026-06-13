import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()

tim.speed(0)
tim.hideturtle()
t.bgcolor("whitesmoke")

color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 35, 60), (220, 128, 118), (62, 130, 152), (182, 205, 191)
]

start_x = -250
start_y = -250
dot_count = 100

tim.penup()
tim.goto(start_x, start_y)

for dot_number in range(1, dot_count + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_number % 10 == 0:
        row_index = dot_number // 10
        new_y = start_y + (row_index * 50)
        tim.goto(start_x, new_y)

screen.exitonclick()