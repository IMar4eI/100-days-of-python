from turtle import Turtle

FONT: tuple[str, int, str] = ("Courier", 24, "bold")
TEXT_COLOR: str = "black"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level: int = 1
        self.hideturtle()
        self.penup()
        self.color(TEXT_COLOR)
        self.goto(-280, 280)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self) -> None:
        self.level += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("CRITICAL COLLISION DETECTED", align="center", font=FONT)
