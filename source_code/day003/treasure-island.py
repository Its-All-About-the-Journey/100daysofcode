print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice == "right":
    print("You fall in a hole almost immediately.\nGame Over.")
    exit()
elif choice == "left":
    choice = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat, or "swim" to swim across.\n').lower()
    if choice == "swim":
        print("You are attacked by a trout and drown.\nGame Over.")
        exit()
    elif choice == "wait":
        choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n').lower()
        if choice == "red":
            print("You open the door and are consumed by fire.\nGame Over.")
            exit()
        elif choice == "blue":
            print("You open the door and are eaten by the beasts inside.\nGame Over.")
            exit()
        elif choice == "yellow":
            print("You found the treasure! Congratulations!")
            exit()
        else:
            print("You chose poorly...\nGame Over.")
            exit()
    else:
        print("You chose poorly...\nGame Over.")
        exit()
else:
    print("You chose poorly...\nGame Over.")
    exit()