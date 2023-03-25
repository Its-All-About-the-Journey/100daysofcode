alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = ""
while direction != "encode" and direction != "decode":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = 0
while shift < 1 or shift > 25:
  shift = int(input("Type the shift number (whole number between 1-25):\n"))

def caesar(dir, input_text, shift_amount):
  processed_text = ""
  for char in input_text:
    position = alphabet.index(char)
    if dir == "encode":
      if alphabet.index(char) + shift_amount < 26:
        processed_text += alphabet[position + shift_amount]
      else:
        processed_text += alphabet[position + shift_amount - 26]
    elif dir == "decode":
      if alphabet.index(char) - shift_amount < 26:
        processed_text += alphabet[position - shift_amount]
      else:
        processed_text += alphabet[position - shift_amount + 26]
  print(f"Your {dir}d text is {processed_text}")

caesar(dir=direction, input_text=text, shift_amount=shift)