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

#Write your code below this line 👇

step1 = input("You're standing at a crossroad, do you go 'left' or 'right'? ").lower()
if step1 == "left":
  step2 = input("\nYou walk down the lane and arrive at a lake with an island in the middle.\nDo you swim to the island or wait for a boat? (type 'swim' or 'wait') ").lower()
  if step2 == "swim":
    print("\nYou're attacked by an alligator and die.\nGame Over")
  elif step2 == "wait":
    step3 = input("\nYou arrive on the island, there is a house with 3 doors.\nWhich door do you enter? red, yellow, or blue: ").lower()
    if step3 == "yellow":
      print("\nCongratulations, you found the gold!\nYou WIN!")
    elif step3 == "red":
      print("\nThe room is full of fire, you are burned to death.\nGame Over")
    elif step3 == "blue":
      print("\nYou have entered the home of the big bad wolf who eats you up.\nGame Over")
    else:
      print("\nYou trip over your shoelaces and fall into the lake where you're eaten by hungry alligators.\nGame Over")
  else:
    print("\nYou get attacked by hungry vultures and are eaten alive.\nGame Over")
else:
  print("\nYou walk into a dark forest full of tigers who attack, ripping you to pieces.\nGame Over")