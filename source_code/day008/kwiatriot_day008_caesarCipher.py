"""
Day 008 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/8/2021

This is program to create an encoded message based on the way Caesar created
"""
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(message, shift_amount, cipher_direction):
    end_message = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in message:
        if char in alphabet:
            location = alphabet.index(char)
            new_position = location + shift_amount
            end_message += alphabet[new_position]
        else:
            end_message += char
    print(f"Here's the {cipher_direction}d result: {end_message}")


print(logo)
should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(message=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
