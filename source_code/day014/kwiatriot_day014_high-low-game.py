"""
Day 014 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/14/2021

A Game to choose who has the highest Instagram followers
"""
import sys
import os
import random
import art
from game_data import data


def get_random_person():
    """Get a random person from data"""
    return random.choice(data)


def formatted_data(person):
    """Formats data for printing"""
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    # Print logo
    print(art.logo)
    # Initiate score
    user_score = 0
    # Initiate game Boolean
    play_on = True
    # Choose two random entries from game_data by key:"name"
    person_a = get_random_person()
    person_b = get_random_person()

    # Start game loop
    while play_on:
        person_a = person_b
        person_b = get_random_person()

        while person_a == person_b:
            person_b = get_random_person()

        # Output the random entries using other data, use VS art
        print(f"Compare A: {formatted_data(person_a)}")
        print(art.vs)
        print(f"Against B: {formatted_data(person_b)}")

        # Ask user for choice
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = check_answer(user_choice, person_a["follower_count"], person_b["follower_count"])

        os.system("clear")
        print(art.logo)
        if correct_answer:
            user_score += 1
            print(f"Your right! Current score: {user_score}.")
        else:
            play_on = False
            print(f"Sorry, that's wrong. Final score: {user_score}.")
            sys.exit(0)


game()
