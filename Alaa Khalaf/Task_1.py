import os

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

bids = {}

while True:
    bidder_name = input("Enter your name: ")
    price = int(input("Enter your bid price: "))
    bids[bidder_name] = price

    more_bidders = input("Are there any other players? (yes/no): ").lower()
    clear_screen()
    if more_bidders == "no":
        break
    
highest_bidder = max(bids, key=bids.get)
highest_bid = bids[highest_bidder]

print(f"The winner of the auction is: {highest_bidder} with a bid of {highest_bid}$")
