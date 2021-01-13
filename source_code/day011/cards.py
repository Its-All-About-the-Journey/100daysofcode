logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

deck = ['ace', 'ace', 'ace', 'ace', 'two', 'two', 'two', 'two', 'three', 'three', 'three', 'three', 'four', 'four',
        'four', 'four', 'five', 'five', 'five', 'five', 'six', 'six', 'six', 'six', 'seven', 'seven', 'seven', 'seven',
        'eight', 'eight', 'eight', 'eight', 'nine', 'nine', 'nine', 'nine', 'ten', 'ten', 'ten', 'ten', 'jack', 'jack',
        'jack', 'jack', 'queen', 'queen', 'queen', 'queen', 'king', 'king', 'king', 'king']

card_faces = ['''
 ------- 
|A      |
|       |
|       |
|      A|
 ------- ''', '''
 ------- 
|2      |
|       |
|       |
|      2|
 ------- ''', '''
 ------- 
|3      |
|       |
|       |
|      3|
 ------- ''', '''
 ------- 
|4      |
|       |
|       |
|      4|
 ------- ''', '''
 ------- 
|5      |
|       |
|       |
|      5|
 ------- ''', '''
 ------- 
|6      |
|       |
|       |
|      6|
 ------- ''', '''
 ------- 
|7      |
|       |
|       |
|      7|
 ------- ''', '''
 ------- 
|8      |
|       |
|       |
|      8|
 ------- ''', '''
 ------- 
|9      |
|       |
|       |
|      9|
 ------- ''', '''
 ------- 
|10     |
|       |
|       |
|     10|
 ------- ''', ''' 
 ------- 
|J      |
|       |
|       |
|      J|
 ------- ''', '''
 ------- 
|Q      |
|       |
|       |
|      Q|
 ------- ''', '''
 ------- 
|K      |
|       |
|       |
|      K|
 ------- '''
         ]

blank = '''
 ------- 
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
 ------- '''

display = {'ace': card_faces[0], 'two': card_faces[1], 'three': card_faces[2], 'four': card_faces[3],
           'five': card_faces[4], 'six': card_faces[5], 'seven': card_faces[6], 'eight': card_faces[7],
           'nine': card_faces[8], 'ten': card_faces[9], 'jack': card_faces[10], 'queen': card_faces[11],
           'king': card_faces[12]}


# Function to display full card hands as ASCII graphics -> updated code to be independent of the size of the hand
def display_all_cards(hand):
    cards = []
    for i in range(len(hand)):
        cards.append(display[hand[i]].split('\n'))
    for row in zip(*cards):
        print(*row)


# Function to display dealers visible cards as ASCII graphics plus a blank card
def display_visible_cards(hand):
    cards = []
    for i in range(len(hand) - 1):
        cards.append(display[hand[i]].split('\n'))
        hidden = blank.split('\n')
    for row in zip(*cards, hidden):
        print(*row)


