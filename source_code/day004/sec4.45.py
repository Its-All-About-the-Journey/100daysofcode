import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

graphics = [rock, paper, scissors]

# Messages
tie  = 'It is a tie.'
lost = 'Bot has beaten you to the death!'
won  = 'You won!'

# Result combination 
rock_map = [tie, lost, won]
paper_map = [won, tie, lost]
scissor_map = [lost, won, tie]

# Result Map
result_map = [rock_map, paper_map, scissor_map]

# Bots random RPS selection
bot_chose = random.randint(0,2)

# Get players move
print('What is your move: Rock(0) Paper(1) or Scissors(2)?')
player_chose = int(input('Enter number: '))

# Results
print('='*80)
print(f'You\n{graphics[player_chose]}')
print(f'Bot\n{graphics[bot_chose]}')
print('='*80)
print( result_map[player_chose][bot_chose] )
print('='*80)
