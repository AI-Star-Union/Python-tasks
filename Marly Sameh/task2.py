message = input("Message: ")
shift = int(input("Shift: "))
result = ""

for char in message:
    if char.isalpha():
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        result += char

print("Encoded:", result)