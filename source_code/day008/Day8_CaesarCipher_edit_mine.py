characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=' '_', '+', '[', ']', '{', '}', '\\', '|', ':', ';', '\'', '"', '\,', '<', '.', '>', '/', '?']
import art
print(art.logo)

def caesar(dir, input_text, shift_amount):
  processed_text = ""
  for char in input_text:
    if char in characters:
        position = characters.index(char)
        if dir == "encode":
          if characters.index(char) + shift_amount < 67:
            processed_text += characters[position + shift_amount]
          else:
            processed_text += characters[position + shift_amount - 67]
        elif dir == "decode":
          if characters.index(char) - shift_amount < 67:
            processed_text += characters[position - shift_amount]
          else:
            processed_text += characters[position - shift_amount + 67]
    else:
        processed_text += char
  print(f"Your {dir}d text is: {processed_text}")
again = "yes"
while again == "yes":
    direction = ""
    while direction != "encode" and direction != "decode":
      direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = 0
    while shift < 1 or shift > 66:
      shift = int(input("Type the shift number (whole number between 1-66):\n"))
    
    caesar(dir=direction, input_text=text, shift_amount=shift)
    again = input("Type 'yes' to go again or anything else to end. ")
print("Goodbye")