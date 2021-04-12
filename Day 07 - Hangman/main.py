import random
from ascii import hangmanpics

word = ["stalker","awkward","studio","diagram","fortunate"]

game_running = True
total_lives = 8

def drawhangman(x):
    '''Function for drawing the ascii art. Note: This prints the index of the list as reverse'''
    print(hangmanpics[-x])

# Randomly select a word from the 'word' list and create a copy of the list in 'blank aka _' format
chosen_word = list(random.choice(word))
chosen_word_blank = []

for num in range(len(chosen_word)):
    chosen_word_blank.append("_")

while game_running:
        if "_" in chosen_word_blank and total_lives > 1:
            guess = input("Guess a letter :").lower()
            indice_location = -1
            for letter in chosen_word:
                indice_location += 1
                if guess == letter:
                    chosen_word_blank[indice_location] = guess
            if guess not in chosen_word:
                print("\n\tWrong answer") 
                total_lives -= 1
                drawhangman(total_lives)
            print(chosen_word_blank)               

        elif "_" not in chosen_word_blank and total_lives > 2:
            print("\n\tYou won")
            game_running = False

        elif "_" in chosen_word_blank and total_lives == 1:
            print("\n\tYou suck!!")
            game_running = False


# Features to be added in future edition:
# - Display previous guesses
# - Show incorrect guesses upon losing