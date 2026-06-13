## High-Res Gameplay Preview
![Snake Gameplay Resolution](gameplay.gif)

# Day 21: Complete Snake Game (Inheritance & Spatial Perception)

This repository contains the production-ready build of the Snake Game from the "100 Days of Code" challenge.

## Architectural Concept: Object Inheritance
The project heavily utilizes OOP **Inheritance** patterns. Both `Food` and `Scoreboard` classes inherit directly from the `turtle.Turtle` base class blueprint, invoking `super().__init__()` parameters.

* **Euclidean Distance Vectors:** Uses matrix spatial checks (`snake.head.distance(food) < 15`) to handle bounding-box proximity metrics.
* **Array Slicing Resolution:** Python sequence slicing (`snake.segments[1:]`) isolates data blocks to monitor internal self-intersection vectors without high computational load.

## How to Run

```bash
python3 main.py