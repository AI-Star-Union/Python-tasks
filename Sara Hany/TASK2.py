# Task 2

print("Welcome to Ceaser Cipher!")
print("1.Decode  2.Encode")
choice = int(input("Enter your choice: "))
text = input("Enter your text: ")
shift = int(input("Enter the shifting number: "))

def Ceaser(text,shift,choice):
    new = ""
    for char in text:
        if choice == 1:
            if char.isalpha():
                if char.isupper():
                    pos=ord(char) - ord('A')
                    new_pos = (pos - shift) % 26
                    new += chr(new_pos + ord('A'))
                else :
                    pos = ord(char) - ord('a')
                    new_pos = (pos - shift) % 26
                    new += chr(new_pos + ord('a'))
            else:
                 new += char

        if choice == 2 :
            if char.isalpha():
                if char.isupper():
                    pos=ord(char) - ord('A')
                    new_pos = (pos + shift) % 26
                    new += chr(new_pos + ord('A'))
                else :
                    pos = ord(char) - ord('a')
                    new_pos = (pos + shift) % 26
                    new += chr(new_pos + ord('a'))
            else:
                 new += char
    return new

final_text= Ceaser(text,shift,choice)
print(f"Here's your final result : {final_text}")


