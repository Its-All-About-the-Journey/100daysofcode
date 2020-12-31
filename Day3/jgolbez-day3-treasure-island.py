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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
direction = input("You\'re at a fork in the road. Go LEFT or RIGHT?\n")
if direction.upper() == "LEFT":
  print('''There is a watery shore here. In the distance you see an island.''')
  sinkorswim = input("Will you SWIM across the water or WAIT for a boat?\n")
  if sinkorswim.upper() == "WAIT":
    print('''A shadowy boat glides across the water piloted by a dark figure. It holds out a bony hand and you place a coin within. The figure beckons you to board and you arrive safely on the island shore''')
    door = input("There are three doors. Will you open the RED, YELLOW or BLUE door?\n")
    if door.upper() == "YELLOW":
      print("You have found fabulous treasure. You win!")
    elif door.upper() == "RED".upper():
      print("A river of lava surges out, burning you to a crisp! GAME OVER")
    else:
      print("A river of acid surges out, washing away your skin and leaving only bones. GAME OVER")
  else:
    print("You are eaten by sharks. GAME OVER")
else:
  print("You are eaten by a grue. GAME OVER")