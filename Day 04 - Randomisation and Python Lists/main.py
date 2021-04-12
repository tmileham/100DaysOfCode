# Day 4 - Rock, Paper and Scissors
#######

# 0 for Rock
# 1 for Paper
# 2 for Scissors
import random


rock = '''\t
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

paper = '''\t
        _______
    ---'    ____)___
               _____)
              ______)
            _______)
    ---.__________)
    '''
scissors = '''\t
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)    
    '''

game_images = [rock,paper,scissors]

def drawImages():
    print(game_images[player_choice])
    print(game_images[ai_choice])

#Player Turn
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
ai_choice = random.randrange(0,3)



# Check who won
if player_choice >= 3 or player_choice < 0:
    print("You entered an invalid number, you lose")
    
else:
    drawImages()

    if player_choice == ai_choice:
        print("its a draw, try again!")

    elif player_choice == 0 and ai_choice == 2 or player_choice == 1 and ai_choice == 0 or player_choice == 2 and ai_choice == 1:
        print("You win!")

    else:
        print("You lose")