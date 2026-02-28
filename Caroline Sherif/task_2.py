message=input("Enter your message: ")
shifting_key=int(input("Enter your shifting_key: "))
operation=input("Enter your operation: ").lower().strip()
result=""
for letter in message:
    if letter.isalpha():
      if letter.isupper():
         original_letter = ord("A")
      else:
         original_letter =ord("a")
      if operation == "encode":
         shift_amount=shifting_key
      else:
         shift_amount=-shifting_key
      new_position=(ord(letter)-original_letter+shift_amount)%26
      new_letter=chr(new_position+original_letter)
      result+=new_letter
    else:
        result+=letter
print("Result:", result)



