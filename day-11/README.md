# Day 11: The Blackjack Capstone Project

This repository contains the Day 11 Capstone Project of the "100 Days of Code" Python challenge. This project combines lists, loops, complex logical conditions, and state manipulation.

## Project Description: Terminal Blackjack
A command-line implementation of the classic Blackjack casino game using dealer AI constraints.

* **Dynamic Value Scaling (The Ace):** Implements logic where the Ace (`11`) automatically scales down to `1` using list methods (`.remove()` and `.append()`) if the player's total hand value exceeds 21.
* **Dealer Constraints:** Simulates standard casino rules where the computer must continuously draw cards until its total score reaches at least 17.

## How to Run

Navigate to the project directory inside your Ubuntu terminal and execute:

```bash
python3 main.py