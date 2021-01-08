alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift):
    codex = []
    if direction == "encode":
        for letter in text:
            newPosition = alphabet.index(letter)+shift
            if newPosition > len(alphabet):
                newPosition = abs(len(alphabet)-newPosition)
            codex += alphabet[newPosition]
            codex = ''.join(codex)
        print(f"The encrypted text is {codex}")        
    elif direction == "decode":
        for letter in text:
            newPosition = alphabet.index(letter)-shift
            if newPosition < 0:
                newPosition = len(alphabet)-abs(newPosition)
            codex += alphabet[newPosition]
            codex = ''.join(codex)
        print(f"The decrypted text is {codex}")
    else:
        print(f'error: {text}, {shift}')

caesar(text=text, shift=shift)
