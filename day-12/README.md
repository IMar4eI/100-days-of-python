# Day 12: Scope & The Number Guessing Game 

This repository contains the final project for Day 12 of the "100 Days of Code" Python challenge. The core objective of this day was mastering **Namespaces**, distinguishing between **Local and Global Scope**, and avoiding mutable global state bugs.

## Project Description: Number Guessing Game
A command-line game where the computer selects a random number between 1 and 100, and the player attempts to guess it within a limited number of turns based on the chosen difficulty level.

* **Namespace Management:** Demonstrates the use of upper-case global constants (`EASY_LEVEL_TURNS`, `HARD_LEVEL_TURNS`) to define rigid game rules while keeping state modification strictly local.
* **State Modification via Returns:** Instead of using the bad practice `global` keyword to modify turns, the code safely passes variables into functions and re-assigns them via `return` values.
* **Error Handling:** Implements a basic `try/except` block to prevent terminal crashes if a player types non-integer characters.

## How to Run

Navigate to the project directory inside your Ubuntu terminal and execute:

```bash
python3 main.py