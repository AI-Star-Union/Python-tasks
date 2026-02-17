max = 0
winner = ""

auction = {}

while True:
    name = input("Enter your name: ")
    bid = float(input("Enter your bid: "))
    auction[name] = bid
    
    if bid > max:
        max = bid
        winner = name

        another = input("Is there another bidder? (yes or no)").lower()

        print("\n" * 100)   
        if another == "no":
            break
        
print(f"the winner is {winner} with bids {bid} $")