data = {}
flag = True
max_value = 0
winner = ""
while True:
    name = input("Enter your name: ")
    value = int(input("Enter your bid amount: "))
    data[name] = value
    if value > max_value:
        winner = name
        max_value = value
    
    
    ans = input("Is there another player? (yes/no): ").lower()
    print ('\n'*100)
    if ans == "no":
        break


print(f"The winner is {winner} with a bid of {max_value}.")
