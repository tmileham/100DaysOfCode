import os

auction = []
auction_running = True

def check_highest_bidder(bidding_record):
    highest_bid = 0
    for bids in bidding_record:
            if bids["bid"] > highest_bid:
                highest_bid = bids["bid"]
                highest_bidder = {
                    "name" : bids["name"],
                    "bid" : bids["bid"]
                }
    print(f"{highest_bidder['name']} won the auction. With a bid of £{highest_bidder['bid']}")


while auction_running:   
    os.system('cls' if os.name == 'nt' else 'clear')
    user_name = input("Please enter your name: ")
    user_bid = int(input("Please enter your bid £"))

    auction_entry={
        "name": user_name,
        "bid": user_bid,
    }
    
    auction.append(auction_entry)
    further_bids = input("Are there any further bidders? (Yes/No)")

    if further_bids.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        check_highest_bidder(auction)

        start_new_auction = input("Do you wish to start a new auction? ")
        if start_new_auction.lower() == "yes":
            highest_bid = 0
            highest_bidder = {}
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            auction_running = False






