# Day 17: The OOP Quiz Game 

This repository contains the Day 17 project of the "100 Days of Code" Python challenge. The core objective of this day was designing classes from scratch, implementing the `__init__` constructor, and practicing **Entity-Control-Boundary** data patterns.

## Architecture Design
The program separates raw data layouts from execution management using an object-oriented approach:

* **`Question` (Entity Model):** A rigid blueprint holding individual parameters (`text`, `answer`).
* **`QuizBrain` (Control Engine):** Tracks execution indices, increments global scoring states, and processes comparison parameters.

## How to Run

```bash
python3 main.py