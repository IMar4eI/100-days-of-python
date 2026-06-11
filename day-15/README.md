# Day 15: The Coffee Machine Simulator (Procedural Architecture) ☕

This repository contains the Day 15 project of the "100 Days of Code" Python challenge. The core objective was simulating real-world hardware logic using procedural design principles (functions and global state dictionaries).

## Project Description: Digital Coffee Machine
A command-line terminal interface that processes coffee orders (`espresso`, `latte`, `custom_latte`), monitors hardware tank limits, calculates coin changes, and tracks cash generation.

* **Global State Tracking:** Manages resources and internal state configurations through nested dictionaries.
* **Input Validation Guards:** Implements preventative safety checks ensuring the physical machine cannot process calculations if resource criteria (Water, Milk, Coffee) fail to meet standard specifications.

## How to Run

```bash
python3 main.py