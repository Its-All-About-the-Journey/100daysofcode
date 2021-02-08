
import art

end_program = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_text, shift_amount, cipher_direction):
    new_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in cipher_text:
        if character not in alphabet:
            new_text += character
        elif alphabet.index(character)+shift_amount > 25:
            new_text += alphabet[alphabet.index(character)+shift_amount-26]
        else:
            new_text += alphabet[alphabet.index(character)+shift_amount]
    return new_text

def program():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    print(f"The {direction}d text is {caesar(cipher_text=text, shift_amount=shift, cipher_direction=direction)}")

print(art.logo)

while end_program == False:
    program()
    choice = input("Would you like to continue? Enter Y or N: ")
    if choice.upper() == "N":
        end_program = True