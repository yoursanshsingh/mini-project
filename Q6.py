#Number gussing game 
import random

def generate_number():
    return random.randint(1, 100)

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = generate_number()
    attempts = 0

    while True:
        guess = input("Take a guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts!")
            break

guess_number()
