data = {}

people = input("Any other bidders? yes/no: ")

while people.lower() == 'yes':
    name = input("Enter your name: ")
    price = float(input("Enter your price: "))
    data[name] = price
    print("\n" * 50)
    people = input("Any other bidders? yes/no: ")

highest_bid = 0
winner = ""

for name, price in data.items():
    if price > highest_bid:
        highest_bid = price
        winner = name

print("The winner is " + winner + " with a bid of $" + str(highest_bid))

print(data)
