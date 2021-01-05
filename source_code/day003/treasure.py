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

correctDirection = "left"
correctSwim = "wait"
correctDoor = "yellow"
incorrectDoorRed = "red"
incorrectDoorBlue = "blue"

direction = str.lower(input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n"))
if direction != correctDirection:
    print("You have turned right and fallen into a hole. Gameover\n")
else:
    print("You have turned left and after some distance you come upon a lake\n")
    swimChoice = str.lower(input("You can go no further. Do you swim across the lake or wait for a boat?\n"))
    if swimChoice != correctSwim:
        print("You are attacked by a man eating trout and succomb to your wounds. Gameover\n")
    else:
        print("You have reached the island in the center of the lake. \nYou come upon a castle with three doors: Red, Blue and Yellow.\n")
        doorChoice = str.lower(input("Which door do you open? Choose \"red\", \"blue\" or \"yellow\":\n"))
        if doorChoice == correctDoor:
            print("You open the door and find the hidden treasure. Congratulations!")
        elif doorChoice == incorrectDoorBlue:
            print("\nYou open the blue door and are attacked by viscious hyenas. You are eaten. Gameover\n")
        elif doorChoice == incorrectDoorRed:
            print("\nYou open the red door and are sucked into a fire. There is no escape. Gameover\n")
        else:
            print("\nYou did not choose a door. A skeletal hand emerges from the ground and drags you into a shallow grave. Gameover\n")
print("\nThank you for playing!")
