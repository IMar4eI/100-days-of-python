from turtle import Turtle

STARTING_POSITION: list[tuple[float, float]] = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE: int = 20
UP: int = 90
DOWN: int = 270
LEFT: int = 180
RIGHT: int = 0

class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head: Turtle = self.segments[0]

    def create_snake(self) -> None:
        for position in STARTING_POSITION:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position: tuple[float, float]) -> None:
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())


    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self) -> None:
        for segment in self.segments:
            segment.goto(1000, 1000)
            segment.hideturtle()

        self.segments.clear()
        self.create_snake()
        print("[SUCCESS] Kinematic state machine reset complete.")

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
