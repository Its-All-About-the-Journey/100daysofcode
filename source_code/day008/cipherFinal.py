from art import logo, codex_box

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift):
    codex = []
    if direction == "encode":
        for letter in text:
            if not letter.isalpha():
                codex += letter
            else:
                newPosition = alphabet.index(letter)+shift
                if newPosition > len(alphabet):
                    if len(alphabet) - newPosition == 0:
                        codex += alphabet[0]
                    else:
                        newPosition = abs(len(alphabet)-newPosition)
                        codex += alphabet[newPosition]
            codex = ''.join(codex)
        codex_box(direction, codex)   
    elif direction == "decode":
        for letter in text:
            if not letter.isalpha():
                codex += letter
            else:
                newPosition = alphabet.index(letter)-shift
                if newPosition < 0:
                    newPosition = len(alphabet)-abs(newPosition)
                    codex += alphabet[newPosition]
                else:
                    codex += alphabet[newPosition]
            codex = ''.join(codex)
        codex_box(direction, codex)
    else:
        print(f'error: {text}, {shift}')

print(logo)

while True:    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    caesar(text=text, shift=shift)
    restart = input("Would you like to restart the cipher program? Type yes or no:\n").lower()
    if restart == "no":
        break
