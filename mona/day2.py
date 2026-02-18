def caesar_cipher(text, shift, choice):
    result = ""
    
    if choice == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            
            pos= ord(char) - start
            new_pos = (pos + shift) % 26
            new_char = chr(start + new_pos)
            result += new_char
        else:
            result += char
    
    return result


text = input("Enter your message: ")
shift = int(input("Enter shift number: "))
choice = input("Type 'encrypt' or 'decrypt': ")

final_result = caesar_cipher(text, shift, choice)
print("Result:", final_result)