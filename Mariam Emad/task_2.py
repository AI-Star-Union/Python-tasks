def encrypt_string(input_string):
    encrypted_string = ""
    for char in input_string:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string

def decrypt_string(encrypted_string):
    decrypted_string = ""
    for char in encrypted_string:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
            decrypted_string += decrypted_char
        else:
            decrypted_string += char
    return decrypted_string
