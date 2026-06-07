import random

from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = ["_"] * word_length

guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another one.")
        continue

    guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Letter '{guess}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Game over! The world was: {chosen_word}")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("Congratulations! You win!")

    print(stages[lives])


