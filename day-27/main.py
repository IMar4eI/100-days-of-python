import tkinter as tk
from typing import Final

WINDOW_TITLE: Final[str] = "Telemetry Unit Scaler"
FONT_CONFIG: Final[tuple[str, int, str]] = ("Arial", 12, "bold")
MILES_TO_KM_FACTOR: Final[float] = 1.60934


def convert_metrics() -> None:
    try:
        miles: float = float(miles_input.get())
        kilometers: float = miles * MILES_TO_KM_FACTOR

        result_label.config(text=f"{kilometers:.2f}")
        print(f"[INFO] Matrix transformation successful: {miles} miles scaled to {kilometers:.2f} km.")
    except ValueError as error:
        result_label.config(text="Error")
        print(f"[ERROR] Invalid numeric literal string in input buffer: {error}")


window = tk.Tk()
window.title(WINDOW_TITLE)
window.config(padx=20, pady=20)

miles_input = tk.Entry(width=10, font=FONT_CONFIG)
miles_input.grid(column=1, row=0)
miles_input.insert(0, "0")

miles_label = tk.Label(text="Miles", font=FONT_CONFIG)
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to", font=FONT_CONFIG)
is_equal_label.grid(column=0, row=1)

result_label = tk.Label(text="0.00", font=FONT_CONFIG)
result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km", font=FONT_CONFIG)
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", font=FONT_CONFIG, command=convert_metrics)
calculate_button.grid(column=1, row=2)

print("[START] Graphical user interface thread initialized successfully.")

window.mainloop()