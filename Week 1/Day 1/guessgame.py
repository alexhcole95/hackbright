# this is a python guessing game

import random

print("Hello! What is your name? ")
name = input()

# f makes the statement a template
print(f"Well, {name}, I am thinking of a number between 1 and 20")

secret_number = random.randint(1, 20)

for guesses_taken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low!")
    elif guess > secret_number:
        print("Your guess is too high!")
    else:
        # number was guessed correctly
        break

    if guess == secret_number:
        print(f"Good Job, {name}!")
        print(f"You guessed my number in {guesses_taken} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {secret_number}")
