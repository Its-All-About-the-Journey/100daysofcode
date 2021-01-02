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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
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
print("You see a labyrinth in the middle of the islande...\n")
direction = input(
    "You decide to enter, which direction do you want to go, Left[L] or Right[R]?\n>>")
direction = direction.lower()
if direction == 'l':
    print("There is a lot of water due to heavy rain. You will have two solution:")
    action = input("Do you want to swim or do you want to wait until the weater is gone? Swim[S], Wait[W]\n>>")
    action = action.lower()
    if action == 'w':
        print(""" After waiting a couple hours, the water is finally gone.
        You now continue to walk through the labyrinth, and you find three doors a Blue, a Yellow and a Red one.
        """)
        door = input("Which door do you want to go through? Red[R],BLUE[B], or YELLOW[Y]\n>>")
        door = door.lower()
        if door == 'y':
            print("You made it! This is the room with the treasure...\nYou Win!")
        elif door == 'r':
            print("Wrong one! There is a fire... You burned...\n Game Over!")
        elif door == 'b':
            print("Wrong one! This is the hell... You've been eaten by beasts...\nGame Over!")
        else:
            print("Sorry... Game Over.")
    else:
        print("You are attacked by trout...\n Game Over!")
else:
    print("You fall into a hole...\nGame Over!")
