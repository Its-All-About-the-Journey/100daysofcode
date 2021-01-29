#!/usr/bin/env python3
# 100 Days of Code : Day 8 Project
# Caesar Cipher
# Adam Pawlowski (@hypermanganate)

from art import logo

# Setup

# Logo was updated in art.py to remove the consecutive triple quotes which causes the art to render wrong. It's wrong in the video too.
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_input():

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % len(alphabet)
  if not shift:
    shift = len(alphabet) - 1

  return direction, text, shift

# Functions

def crypt(text, shift, type="decode"):

  overflow = len(alphabet)

  if type == "encode":
    overflow = 0 - overflow
  else:
    shift = 0 - shift

  message = []
  for letter in text:
    if not letter in alphabet:
      message = f"""The message contains {letter} which is not able to be encoded. Use letters A - Z only."""
      return message
    new_index = alphabet.index(letter) + shift
    if new_index >= len(alphabet) or new_index < 0:
      new_index += overflow
    message.append(alphabet[new_index])

  message = f"""The {type}d text is {''.join(message)}"""

  return message

# Main

while True:

  direction, text, shift = get_input()

  if direction == "encode":
    message = crypt(text, shift, "encode")
  elif direction == "decode":
    message = crypt(text,shift)
  else:
    print("Invalid selection, try again.")

  print(message)
  if (input("Give 'er another go? Type 'yes' to try again. :") != "yes"):
    break
