Markdown

# Day 3 - Treasure Island (Control Flow Text Adventure)

A text-based choose-your-own-adventure game that demonstrates nested conditional logic, data validation, and ASCII art rendering in the Linux terminal.

### Concepts Covered
- **Control Flow:** Mastering `if`, `elif`, and `else` blocks to construct complex decisions trees.
- **Logical Operators:** Combining multiple conditions using `and`, `or`, and `not`.
- **Comparison Operators:** Evaluated values using `>`, `<`, `>=`, `<=`, `==`, and `!=`.
- **Data Robustness:** Utilizing the `.lower()` method to handle case-insensitive user inputs and avoid runtime crashes.
- **Python String Handling:** Using raw multi-line strings (`r'''...'''`) to bypass string termination errors when rendering heavy ASCII graphics.

### How it works (Decision Tree):
To win the game and find the treasure chest, the input sequence must exactly match:
`left` -> `wait` -> `yellow`

Any other branch triggers a unique "Game over" scenario.

### How to Run:
Make sure you are in the project root directory and execute:
```bash
python3 day-03/main.py