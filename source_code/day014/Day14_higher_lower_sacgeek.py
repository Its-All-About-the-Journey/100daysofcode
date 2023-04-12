from art import logo
from art import vs
from game_data import data
from random import randint
import time
import os
import platform

def clear():
  sysos = platform.platform()
  if sysos[0] == "Windows":
      os.system('cls')
  else:
    os.system('clear')

#Step 1: Generate 2 random numbers
#Step 2: Use random numbers to select two indexes from game_data
def distinct_item(item = None):
  """Function will find a random and distinct item from data if given an item to compare to, with no imput will return a random item from data."""
  if item == None:
    myitem = data[randint(0,len(data)-1)]
    return myitem
  else:
    myitem2 = data[randint(0,len(data)-1)]
    while item["follower_count"] ==  myitem2["follower_count"]:
      myitem2 = data[randint(0,len(data)-1)]
    return myitem2


#Step 3: Determine which item has the highest value and store/return it's index

#Step 5: Check if user is correct
def check_response(response):
  """Submit a letter resonse of 'A' or 'B' (not case sensitive) and return will be True if response is correct or False if not."""
  if response.lower == "a":
    if dataitem1["follower_count"] > dataitem2["follower_count"]:
      return True
    else:
      return False
  else:
    if dataitem1["follower_count"] < dataitem2["follower_count"]:
      return True
    else:
      return False

#Step 4: Display random item 1 vs random item 2 and ask user which one has more followers  
def get_response():
  response = input("Who has more followers? Type 'A' or 'B': ")
  while response.lower() != "a" and response.lower() != "b":
    print(response.lower())
    print("Bad value, try again", end='\r')
    time.sleep(1)
    print("                    ", end='\r')
    print("\x1b[1A", end='\r')
    response = input("Who has more followers? Type 'A' or 'B': ")
  return response
    
#Step 6: If user is correct loop, set random1 to the stored/returned value from step 3 and generate another random index for item 2 and ask the user again, "higher or lower?"  - If user is wrong end game
dataitem1 = distinct_item()
correct = True
score = 0
while correct == True:
  dataitem2 = distinct_item(dataitem1)
  clear()
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}")
  print(f"Compare A: {dataitem1['name']}, a {dataitem1['description']}, from {dataitem1['country']}.\n{vs}\nAgainst B: {dataitem2['name']}, a {dataitem2['description']}, from {dataitem2['country']}.")
  response = get_response()
  correct = check_response(response)
  if correct == True:
    dataitem1 = dataitem2
    score += 1
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")