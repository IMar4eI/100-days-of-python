import random
import os

logo = r'''
  ________                               ___________ _            _______                      
 /  _____/ __  _  __ ____   ______ _____ \__    ___/| |__   ____  \      \  __ __  _____       
/   \  ___ \ \/ \/ // __ \ /  ___//  ___/   |    |   |  |  _/ __ \ /   |   \|  |  \/     \      
\    \_\  \ \     //  ___/ \___ \ \___ \    |    |   |   |  \  ___//    |    \  |  /  Y Y  \     
 \______  /  \/\_/  \___  >____  >____  >   |____|   |___|  /\___  >____|__  /____/|__|_|  /     
        \/              \/     \/     \/                  \/     \/        \/            \/      
'''

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return turns

def game():
    clear_screen()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You've run out of guesses, you lose. The answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")
            print("-" * 30)

game()