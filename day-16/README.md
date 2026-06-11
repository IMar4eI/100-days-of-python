# Day 16: The Coffee Machine Simulator (Object-Oriented Programming) 

This repository contains the Day 16 project of the "100 Days of Code" Python challenge. The core objective was migrating the procedural architecture from Day 15 into the **Object-Oriented Programming (OOP)** paradigm.

## Architectural Transition
Instead of relying on global dictionaries and mutating states inside procedural nested functions, the system is now divided into independent, decoupled objects acting as black boxes:

* **`Menu` & `MenuItem`:** Handles data blueprints for drink formulas, prices, and search querying.
* **`CoffeeMaker`:** Manages internal physical resource tanks (Water, Milk, Coffee) and handles the manufacturing state.
* **`MoneyMachine`:** Operates as a distinct financial ledger handling coin counting, transactions, and cash profits.

## How to Run

Ensure all module files (`menu.py`, `coffee_maker.py`, `money_machine.py`, `main.py`) reside in the same folder.

```bash
python3 main.py