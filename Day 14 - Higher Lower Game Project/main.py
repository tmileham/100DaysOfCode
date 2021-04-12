from logo import art, vs
from random import shuffle
from data import userdata
import os

# Clear + Print Logo
def clear_printlogo():
    """clears screen and prints the higher lower ascii art"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art)

def compare_followers(item_a,item_b):
    """Returns a or b based on item with higher number of followers"""
    if item_a["ig_followers"] > item_b["ig_followers"]:
        return "a"
    else:
        return "b"

def format_data(item):
    """Returns the data formatted to be output to console"""
    return f"{ item['name']}, {item['description']}, from {item['country']}"    


def game():
    clear_printlogo()
    shuffle(userdata)
    current_score = 0
    is_game_over = False


    while not is_game_over:
        # Select data # Display data (hiding the follower count) # Display second (data hiding the follower count)
        item_a = userdata[current_score]
        item_b = userdata[current_score+1]
        
        print(f"Compare A: {format_data(item_a)}")
        print(f"{vs}")
        print(f"Compare B: {format_data(item_b)}")

        # User to guess who has more IG followers
        guess = input("\nWho has more instagram followers? Type 'A' or 'B': ").lower()
        
        # Check answer
        answer = compare_followers(item_a,item_b)

        if guess == answer:
            current_score += 1
            clear_printlogo()
            print(f"You're right!, Current score: {current_score}.\n")
            
        else:
            clear_printlogo()
            print(f"Sorry, that's wrong. Final score: {current_score}")
            print(f"\nYou selected {guess.upper()}")
            print(f"A: {item_a['name']} has {item_a['ig_followers']} followers")
            print(f"B: {item_b['name']} has {item_b['ig_followers']} followers")
            is_game_over = True

game()