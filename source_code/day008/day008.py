'''
Grant Armstrong
1/9/2020
Caesar Cipher Day 8 Project
'''


from art import logo

print(logo)
run_again = True

# This cipher converts between the unicode point representations of characters
# to encode and decode the text
def caesar(text, shift, direction):
    if shift > 26:
        shift = shift % 26
    text = list(text)
    text_list = []
    for char in text:
        if 32 <= ord(char) <= 64:
            text_list.append(char)
        elif direction.lower() in ['encode', 'encrypt']:
            if ord(char) + shift <= 122:
                text_list.append(chr(ord(char) + shift))
            elif ord(char) + shift > 122:
                adjusted_unicode = 96 + (ord(char) + shift - 122)
                text_list.append(chr(adjusted_unicode))
        elif direction.lower() in ['decode', 'decrypt']:
            if ord(char) - shift >= 97:
                text_list.append(chr(ord(char) - shift))
            elif ord(char) - shift < 97:
                adjusted_unicode = 123 - (97 - (ord(char) - shift))
                text_list.append(chr(adjusted_unicode))
    code_text = ''.join(text_list)
    print(f'The {direction}d text is: {code_text}')


def run_caesar():

    while True:
        direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction_input in ['encode', 'encrypt', 'decode', 'decrypt']:
            break
        else:
            print(f'"{direction_input}" is an invalid selection. Please try again...')
            continue

    text_input = input("Type your message:\n").lower()

    while True:
        try:
            shift_input = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Invalid format. Must be an integer.")
            continue

    caesar(text_input, shift_input, direction_input)


while run_again:
    run_caesar()
    again = input("Would you like to run the program again (yes/no)?")
    if again.lower() in ['no', 'n']:
        run_again = False
        print('\n', 'Goodbye User!')
    elif again.lower() in ['yes', 'y']:
        run_again = True
