alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ""
while direction != "encode" and direction != "decode":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = 0
while shift < 1 or shift > 25:
  shift = int(input("Type the shift number (whole number between 1-25):\n"))

#Function for encrypting the users message:
def encrypt(lowertext, shiftamount):
  crypt = ""
  for char in lowertext:
    position = alphabet.index(char)
    if alphabet.index(char) + shiftamount < 26:
      crypt += alphabet[position + shiftamount]
    else:
      crypt += alphabet[position + shiftamount - 26]
  return crypt
#Function for decrypting the users message:
def decrypt(lowertext, shiftamount):
  cryptext = ""
  for char in lowertext:
    position = alphabet.index(char)
    if alphabet.index(char) - shiftamount < 26:
      cryptext += alphabet[position - shiftamount]
    else:
      cryptext += alphabet[position - shiftamount + 26]
  return cryptext
#If statement to decide which function to call and print the corresponding message:
if direction == "encode":
  print(f"The encoded text is {encrypt(text, shift)}")
elif direction == "decode":
  print(f"The decoded text is {decrypt(text, shift)}")
