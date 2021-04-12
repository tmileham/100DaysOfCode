################# Our Blackjack House Rules
## The deck is unlimited in size
## There are no jokers
## The Jack/Queen/King all count as 10.
## The ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as thery are drawn

import random, os


player_cards = []
player_total = 0

ai_cards = []
ai_total = 0

game_over = False
player_turn = True
ai_turn = True

def deal(target):
    """Deals a card to target list by randomly selecting from cards list. Also tallies the totals within the same call"""

    global player_total
    global ai_total
    
    target.append(random.choice(cards))
    if (len(player_cards) > 0):
        player_total = sum(player_cards)
    if (len(ai_cards)> 0):
        ai_total = sum(ai_cards)

def check_total(target):
    score = sum(target)
    # print(f"The current total is {score}")
    return score

def win_check(target):
    """ Checks if provided list is equal to 21 """
    if sum(target) == 21:
        return True
    else:
        return False

def check_if_bust(target):
    """ Checks provided list if sum > 21 """
    global player_total
    global ai_total
    if sum(target) > 21:
        if 11 in target:
            print("Exceeded 21 with an ace. replacing an ace with a value of 11 with 1")
            replace_ace_11 = target.index(11)
            target[replace_ace_11] = 1
            if target == player_cards:
                player_total = sum(target)
            elif target == ai_cards:
                ai_total == sum(target)
            print(f"The new total is {sum(target)}")
   
            return False
        return True
    else:
        return False

def hit_or_stand():
    global game_over
    global player_turn

    action = input("\n\tDo you wish to 'Hit' or 'Stick' :")

    if action.lower() == "hit" or action.lower() == "h":
        deal(player_cards)
        print(f"\nPlayers cards: {player_cards}")
        print(f"Player total: {player_total}")

    else:
        print(f"\nPlayer total: {player_total}")
        player_turn = False


def init_game():
    #Clears the console
    os.system('cls' if os.name == 'nt' else 'clear')

    """ Starts the game, 2 cards are dealt to both Player/AI """
    # Player
    deal(player_cards)
    deal(player_cards)

    print(f"\nPlayers cards: {player_cards}")

    # AI
    deal(ai_cards)
    deal(ai_cards)

    print(f"Dealers cards: {ai_cards[:1]} - (One card is hidden)\n")

init_game()



# Game Loop
while not game_over:
    while player_turn == True:
        check_total(player_cards)

        if win_check(player_cards):
            print("You got 21.")
            player_turn = False
            break

        if check_if_bust(player_cards):
            print("GAMEOVER - You went bust")
            game_over = True
            player_turn = False
        
        if game_over == False and player_turn == True:
            hit_or_stand()

    while ai_turn == True and game_over == False:
        if ai_total < 17:
            print(ai_cards)
            print(f"\nThe dealers current total is {ai_total}")
            deal(ai_cards)
        if ai_total > 17:
            print(ai_cards)
            print(f"The dealers current total is {ai_total}")
            ai_turn = False
        if check_if_bust(ai_cards):
            print("Dealer went bust. You win!")
            game_over = True
    
    if game_over == False:
        if player_total > ai_total:
            print("\nYOU WIN!!")
            print(f"Your cards were {player_cards} with a total of {player_total}")
            print(f"The dealers cards were {ai_cards} with a total of {ai_total}")
            break
        elif player_total == ai_total:
            print("\nIt was a draw!!")
            print(f"Your cards were {player_cards} with a total of {player_total}")
            print(f"The dealers cards were {ai_cards} with a total of {ai_total}")
            break
        else:
            print("\nYou lose! :(")
            print(f"Your cards were {player_cards} with a total of {player_total}")
            print(f"The dealers cards were {ai_cards} with a total of {ai_total}")
            break
