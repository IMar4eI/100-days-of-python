from pathlib import Path
from turtle import Turtle

ALIGNMENT: str = "center"
FONT: tuple[str, int, str] = ("Courier", 22, "bold")
TEXT_COLOR: str = "white"

DATA_FILE_PATH: Path = Path(__file__).parent / "data.txt"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score: int = 0
        self.high_score: int = self.read_high_score()

        self.color(TEXT_COLOR)
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def read_high_score(self) -> int:
        try:
            if DATA_FILE_PATH.exists():
                content: str = DATA_FILE_PATH.read_text(encoding="utf-8").strip()
                return int(content) if content.isdigit() else 0
            return 0
        except IOError as error:
            print(f"[ERROR] Volatile storage stream failure during read operation: {error}")
            return 0

    def write_high_score(self) -> None:
        try:
            DATA_FILE_PATH.write_text(str(self.high_score), encoding="utf-8")
            print(f"[SUCCESS] High score successfully synced to disk: {self.high_score}")
        except IOError as error:
            print(f"[CRITICAL] Volatile memory serialization aborted: {error}")

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def reset_score(self) -> None:
        print("[INFO] Target collision registered. Evaluating high score threshold...")
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
