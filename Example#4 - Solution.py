# Example 4 - Guessing Game - Correct Solution

import random

random_num = random.randrange(1, 101)

guess = int(input("Enter your guess: "))

while guess != random_num:
    if guess > random_num:
        print("Guess is too high. Guess again.\n")
    else:
        print("Guess is too low. Guess again.\n")
    guess = int(input("Enter your guess: "))

print("Congratulations! Your guess is correct.")