# Grant Armstrong
# 1/9/2020
# Caesar Cipher Day 8 Project
# 100DaysOfCode



from art import logo

print(logo)

# This cipher converts between the unicode point representations of characters
# to encode and decode the text
def caesar(text, shift, direction):
    # Adjust the shift if it's super large
    if shift > 26:
        shift = shift % 26
    text = list(text)
    text_list = []
    for char in text:
        # If the character is a space or punctuation, add it as is to the text
        if 32 <= ord(char) <= 64:
            text_list.append(char)
        # What to do if the user wants to encrypt
        elif direction.lower() in ['encode', 'encrypt']:
            # Check to make sure the shift doesn't overlap from Z back to A (do the following if it doesn't)
            if ord(char) + shift <= 122:
                text_list.append(chr(ord(char) + shift))
            # What to do if the shift overlaps from Z back to A
            elif ord(char) + shift > 122:
                adjusted_unicode = 96 + (ord(char) + shift - 122)
                text_list.append(chr(adjusted_unicode))
        # Decrypted -> works the exact opposite as encrypting
        elif direction.lower() in ['decode', 'decrypt']:
            if ord(char) - shift >= 97:
                text_list.append(chr(ord(char) - shift))
            elif ord(char) - shift < 97:
                adjusted_unicode = 123 - (97 - (ord(char) - shift))
                text_list.append(chr(adjusted_unicode))
    code_text = ''.join(text_list)
    print(f'The {direction}d text is: {code_text}')


def run_caesar():
    # Outer while loop reruns program until user enters "no"
    run_again = True
    while run_again:

        # Inner while loops validate user inputs and re-requests input if invalid
        while True:
            direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction_input in ['encode', 'encrypt', 'decode', 'decrypt']:
                break
            else:
                print(f'"{direction_input}" is an invalid selection. Please try again...')
                continue

        text_input = input("Type your message:\n").lower()

        # Ensures valid shift value is entered, catching exceptions
        while True:
            try:
                shift_input = int(input("Type the shift number:\n"))
                break
            except ValueError:
                print("Invalid format. Must be an integer.")
                continue

        # Runs the function with all user inputs
        caesar(text_input, shift_input, direction_input)

        # Asks user if they would like to run again
        again = input("Would you like to run the program again (yes/no)?")
        if again.lower() in ['no', 'n']:
            run_again = False
            print('\n', 'Goodbye User!')
        elif again.lower() in ['yes', 'y']:
            run_again = True


run_caesar()


