## Gameplay Demo
![Snake Gameplay](gameplay.gif)

# Day 20: The Snake Game - Part 1 (Kinematic Vector Movement) 

This repository contains Part 1 of the iconic Snake Game from the "100 Days of Code" Python challenge. The core engineering focus was designing a multi-segment vector rendering loop.

## Kinematic Logic & Game Loop
Unlike basic static layout applications, a custom real-time **Game Loop** controls execution frames. It overrides screen rendering states using refresh buffers (`screen.tracer(0)`) to maintain stability.

* **Trajectory Linkage Array:** Implements linked positional shifting where segment $N$ pulls coordinates from segment $N-1$, simulating joint-chain kinetics.
* **Vector Constraints:** Overrides event listeners to lock execution angles, preventing $180^\circ$ linear self-collisions.

## How to Run

```bash
python3 main.py