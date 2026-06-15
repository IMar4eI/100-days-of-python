import turtle
from pathlib import Path
import pandas as pd

BASE_DIR: Path = Path(__file__).parent
IMAGE_PATH: str = str(BASE_DIR / "blank_states_img.gif")
DATE_PATH: Path = BASE_DIR / "50_states.csv"

screen = turtle.Screen()
screen.title("U.S. States Quiz - Vector Mapping")

if not Path(IMAGE_PATH).exists() or not Path(DATE_PATH).exists():
    print("[FATAL] Critical game assets are missing in the workspace.")
    screen.bye()
else:
    screen.addshape(IMAGE_PATH)
    turtle.shape(IMAGE_PATH)

    data_frame: pd.DataFrame = pd.read_csv(DATE_PATH)
    all_states: list[str] = data_frame["state"].to_list()
    guessed_states: list[str] = []

    print("[START] States tracking engine synchronized.")

    while len(guessed_states) < 50:
        user_answer: str = screen.textinput(
            title=f"{len(guessed_states)} / 50 States Correct",
            prompt="Enter a state name (or type 'Exit' to save missed states):"
        )

        if not user_answer:
            continue

        answer_formatted: str = user_answer.title()

        if answer_formatted == "Exit":
            print("[INFO] Generating learning report for missed data points...")
            missing_states: list[str] = [state for state in all_states if state not in guessed_states]

            output_df: pd.DataFrame = pd.DataFrame(missing_states, columns=["state"])
            output_df.to_csv(BASE_DIR / "states_to_learn.csv", index=False)

            print("[SUCCESS] Export complete. Check 'states_to_learn.csv'.")
            break

        if answer_formatted in all_states and answer_formatted not in guessed_states:
            guessed_states.append(answer_formatted)

            state_data: pd.DataFrame = data_frame[data_frame["state"] == answer_formatted]

            state_x: float = float(state_data["x"].iloc[0])
            state_y: float = float(state_data["y"].iloc[0])

            writer: turtle.Turtle = turtle.Turtle()
            writer.hideturtle()
            writer.penup()
            writer.goto(state_x, state_y)
            writer.write(answer_formatted, align="center", font=("Arial", 10, "normal"))

            print(f"[REGISTERED] State identified: {answer_formatted} at coordinates ({state_x}, {state_y}")

    screen.bye()