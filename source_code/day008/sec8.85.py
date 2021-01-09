alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def ceaser(msg: str, shift_amount: int, direction: str) -> None:
  result = ""
  for letter in msg:
    position = alphabet.index(letter)

    if(direction == 'encode'):
        new_position = position + shift_amount
    else:
        new_position = position - shift_amount
    
    result += alphabet[new_position]
  print(f"The encoded text is {result}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceaser(msg=text, shift_amount=shift, direction=direction)