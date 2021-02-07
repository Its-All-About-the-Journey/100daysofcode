import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(cipher_text, shift_amount, cipher_direction):
    new_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in cipher_text:
        if alphabet.index(letter)+shift_amount > 25:
            new_text += alphabet[alphabet.index(letter)+shift_amount-26]
        elif alphabet.index(letter)+shift_amount < 0:
            new_text += alphabet[alphabet.index(letter)+shift_amount+26]
        else:
            new_text += alphabet[alphabet.index(letter)+shift_amount]
        
    print(f"The {cipher_direction}d text is {new_text}")

caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)