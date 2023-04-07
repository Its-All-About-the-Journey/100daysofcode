from art import logo
import random

def pick_card():
  return cards[random.randint(0,12)]
def calc_score(cards):
  """Pass a list object with only integer values and function will return a sum of the values"""
  score = 0
  for card in cards:
    score += card
  return score
def check_win():
  if user_score == 21:
    print("\nBlackjack! You Win! 😎")
    return True
  elif computer_score == 21:
    print(f"\nComputer has backjack. {computer_cards}\n\nYou loose. 😱")
    return True
  if user_score > 21:
    print("\nYou went over, You loose. 😭")
    return True
  
#Vars:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
computer_score = 0

print(logo)

#Initial Draw:
for _ in range(2):
  user_cards.append(pick_card())
  computer_cards.append(pick_card())
##############
#Computer Starting Score:
computer_score = calc_score(computer_cards)
#Game loop:
finished = False
while finished == False:
  user_score = calc_score(user_cards)
  if user_score > 21 and 11 in user_cards and (user_score - 10) <= 21:
    user_cards[user_cards.index(11)] = 1
    user_score = calc_score(user_cards)

  print(f"   Your cards: {user_cards}, current score: {user_score}")
  print(f"   Computer's first card: {computer_cards[0]}")
  if check_win() == True:
    break

  if input("Draw another card (y/n)?: ") == "n":
    finished = True
    while computer_score < 17:
      computer_cards.append(pick_card())
      computer_score = calc_score(computer_cards)
    
    if computer_score > 21 or user_score > computer_score:
      print(f"Your cards: {user_cards}, and score: {user_score}\nComputer cards: {computer_cards}, and score: {computer_score}\n\nYou Win! 😃")
    elif computer_score > user_score:
      print(f"Your cards: {user_cards}, and score: {user_score}\nComputer cards: {computer_cards}, and score: {computer_score}\n\nYou Loose. 😤")
    else:
      print(f"Your cards: {user_cards}, and score: {user_score}\nComputer cards: {computer_cards}, and score: {computer_score}\n\nIt's a draw!. 🙃")
  else:
    user_cards.append(pick_card())
