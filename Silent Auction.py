data = {}
Max = 0
winner = ""
while True:
    name = input("Enter your name: ")
    while True:
        try:
            num = int(input("Enter your bid amount:$$ "))
            break
        except ValueError:
            print("Please enter a valid number!")
    data[name] = num
    if num > Max:
        Max = num
        winner = name
    ans = input("Is there another player? (yes/no): ").lower()
    print("\n" * 100)
    if ans == "no":
        break
print(f"The winner is {winner} with a bid of {Max}.")
