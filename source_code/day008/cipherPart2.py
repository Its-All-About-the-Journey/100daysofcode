alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    codex = []
    for letter in text:
        newPosition = alphabet.index(letter)+shift
        if newPosition > len(alphabet):
            newPosition = abs(len(alphabet)-newPosition)
        codex += alphabet[newPosition]
    #print(f"The encoded text is {codex}.")
    return ''.join(codex)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
    codex = []
    for letter in plain_text:
        newPosition = alphabet.index(letter)-shift
        if newPosition < 0:
            newPosition = len(alphabet)-abs(newPosition)
        codex += alphabet[newPosition]
    return ''.join(codex)

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    codex = encrypt(plain_text=text, shift_amount=shift)
    print(f"The encoded message is {codex}")
else:
    codex = decrypt(plain_text=text, shift_amount=shift)
    print(f"The decoded text is {codex}")
