# Generate Random Number 1-100

from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def set_difficulty(input):
    if input.lower() == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def guess(num,randnum):
    if num < randnum:
        print("Too low")
    elif num > randnum:
        print("Too high")
    else:
        print("You got it right!")
def start_game():
    random_number = randint(1,100)

    # print(f"Psst... {random_number}")
    print("Welcome to the number guessing game")
    print("Attempt to guess a number between 1 - 100")
    attempts = set_difficulty(input("\nSelect difficulty - Type 'easy' or 'hard':"))

    while attempts > 0 or guess == random_number:
        print(f"You have {attempts} attempts remaining")
        guess(int(input("\nEnter your guess :")), random_number)
        attempts -= 1

        if attempts == 0:
            print(f"\nGame over. You're out of guesses.")
            print(f"The correct number was {random_number}")

        if guess == random_number:
            print(f"Well done. You got it right!")

    if input("Would you like to play again?").lower() == "y":
        start_game()

start_game()