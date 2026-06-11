# Day 14: Higher Lower Game Capstone Project 

This repository contains the Day 14 Capstone Project, marking the completion of the basic core Python fundamentals package in the "100 Days of Code" challenge.

## Project Description: Terminal Higher Lower Game
A command-line game where players compare two random high-profile Instagram accounts to guess which one has a higher follower count. The game runs continuously until the first incorrect guess.

* **Data Shifting (State Continuity):** Implements dynamic data assignment where `account_b` seamlessly shifts into `account_a` upon a successful round, maintaining game state continuity.
* **Complex Data Extraction:** Practices deep navigation through lists containing multi-key dictionaries to extract specific string values and integer parameters.
* **Modular Code Separation:** Utilizes dedicated parsing functions to format terminal UI rendering independently from core mathematical comparison logic.

## How to Run

Navigate to the project directory inside your Ubuntu terminal and execute:

```bash
python3 main.py