from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(to_encrypt, to_shift):
    new_letter = []
    for letter in to_encrypt:
        position = alphabet.index(letter)
        new_word = position + to_shift
        new_letter += alphabet[new_word]
    word = ""
    for char in new_letter:
        word += char

    print(f"The encoded message is {word}")

def decrypt(to_decrypt, to_shift):
    new_letter = []
    for letter in to_decrypt:
        position = alphabet.index(letter)
        new_word = position - to_shift
        new_letter += alphabet[new_word]
    word = ""
    for char in new_letter:
        word += char

    print(f"The decoded message is {word}")

print(logo)
end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if "encode" in direction:
        encrypt(text, shift)
    elif "decode" in direction:
        decrypt(text, shift)

    restart = input("Whould you like to do it again ? [Yes/no]").lower()
    if restart == 'no':
        end = True
        print("See ya!")
