# Day 22: Arcade Pong - Vector Collision Physics

This repository contains the Day 22 Arcade Pong build from the "100 Days of Code" challenge.

## Physics & Object Collision Engine
The game architecture isolates independent object velocity vectors inside dedicated loops. 

* **Elastic Vector Bouncing:** Simulates basic kinematics by applying scalar inversion ($v_x = -v_x$) upon boundary intersection.
* **Dynamic Frame Throttle:** Implements custom frame-rate stepping (`ball.move_speed *= 0.9`) to simulate acceleration metrics after every successful collision.

## 📊 Gameplay Simulation
![Pong Gameplay](gameplay.gif)

## How to Run
```bash
python3 main.py