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


# Function to display full card hands as ASCII graphics
def display_all_cards(hand):
    if len(hand) == 2:
        card1 = display[hand[0]].split('\n')
        card2 = display[hand[1]].split('\n')
        for row in zip(card1, card2):
            if row != " ":
                print(row[0], row[1])
    elif len(hand) == 3:
        card1 = display[hand[0]].split('\n')
        card2 = display[hand[1]].split('\n')
        card3 = display[hand[2]].split('\n')
        for row in zip(card1, card2, card3):
            print(row[0], row[1], row[2])
    elif len(hand) == 4:
        card1 = display[hand[0]].split('\n')
        card2 = display[hand[1]].split('\n')
        card3 = display[hand[2]].split('\n')
        card4 = display[hand[3]].split('\n')
        for row in zip(card1, card2, card3, card4):
            print(row[0], row[1], row[2], row[3])
    elif len(hand) == 5:
        card1 = display[hand[0]].split('\n')
        card2 = display[hand[1]].split('\n')
        card3 = display[hand[2]].split('\n')
        card4 = display[hand[3]].split('\n')
        card5 = display[hand[4]].split('\n')
        for row in zip(card1, card2, card3, card4, card5):
            print(row[0], row[1], row[2], row[3], row[4])


# Function to display dealers visible cards as ASCII graphics
def display_visible_cards(hand):
    if len(hand) == 2:
        card1 = display[hand[0]].split('\n')
        card2 = blank.split('\n')
        for row in zip(card1, card2):
            print(row[0], row[1])
    elif len(hand) == 3:
        card1 = display[hand[0]].split('\n')
        card2 = display[hand[1]].split('\n')
        card3 = blank.split('\n')
        for row in zip(card1, card2, card3):
            print(row[0], row[1], row[2])
    elif len(hand) == 4:
        card1 = display[hand[0]].split('\n')
        card2 = display[hand[1]].split('\n')
        card3 = display[hand[2]].split('\n')
        card4 = blank.split('\n')
        for row in zip(card1, card2, card3, card4):
            print(row[0], row[1], row[2], row[3])
    elif len(hand) == 5:
        card1 = display[hand[0]].split('\n')
        card2 = display[hand[1]].split('\n')
        card3 = display[hand[2]].split('\n')
        card4 = display[hand[3]].split('\n')
        card5 = blank.split('\n')
        for row in zip(card1, card2, card3, card4, card5):
            print(row[0], row[1], row[2], row[3], row[4])


