def caeser_cipher(text, shift, choice):
    result = ""

    if choice == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start= ord('a')
            
            original_position = ord(char) - start
            new_position = (original_position + shift) % 26
            new_charachter = chr(new_position + start)
            result += new_charachter
        else:
            result += char
    return result


user_text = input("Enter your message:\n")
user_shift = int(input("Enter shift number:\n"))
user_choice = input("Enter your choice('encrypt' or 'decrypt'):\n")

print(f"The final result: {caeser_cipher(user_text, user_shift, user_choice)}")