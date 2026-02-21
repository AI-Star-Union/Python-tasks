def encrypt_caesar(text): 
    encrypted = [] 
    for char in text: 
        if char.isalpha():   
            new_char = chr((ord(char.lower()) - ord('a') + 2) % 26 + ord('a')) 
            encrypted.append(new_char) 
        elif char != ' ':  
            encrypted.append(char) 
    return ''.join(encrypted) 

def decrypt_caesar(text): 
    decrypted = [] 
    for char in text: 
        if char.isalpha(): 
            new_char = chr((ord(char.lower()) - ord('a') - 2) % 26 + ord('a')) 
            decrypted.append(new_char) 
        elif char != ' ': 
            decrypted.append(char) 
    return ''.join(decrypted)

x = input ('enter the text :')
y = encrypt_caesar(x)
z = decrypt_caesar(y)
print (y,z)