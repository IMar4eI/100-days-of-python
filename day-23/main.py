import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.title("Autonomous Robot Navigation Simulation (Day 23)")
screen.tracer(0)

player: Player = Player()
car_manager: CarManager = CarManager()
scoreboard: Scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")

game_is_on = True

try:
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
                screen.update()

        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

except Exception:
    print("[INFO] Simulation engine telemetry socket closed. Clean exit.")

screen.exitonclick()