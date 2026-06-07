# Day 10: Functions with Outputs & The Calculator

This repository contains the final project for Day 10 of the "100 Days of Code" Python challenge. The core focus was mastering the `return` statement, mapping functions to dictionary keys, and implementing recursive logic.

## Project Description: Terminal Calculator
A modular command-line calculator that performs basic arithmetic operations (`+`, `-`, `*`, `/`) and allows continuous calculations using the previous output.

* **Key Concept (Return Statements):** Functions do not just print results; they compute data and return values back to the program execution flow, allowing for fluid data recycling.
* **Data Mapping:** Operations are stored as values inside a dictionary where symbols (`+`, `-`) act as keys. This design pattern replaces messy `if/elif` chains.
* **Recursion:** The application uses self-calling functions to clean the memory state and launch a fresh calculator instance when the user decides to start a new session.

## How to Run

Navigate to the project directory inside your Ubuntu terminal and execute:

```bash
python3 main.py