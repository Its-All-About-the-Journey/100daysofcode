print('''
       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("left or right?\nAnswer: ")
direction_lc = direction.lower()
if direction_lc == "left":
  action_2 = input("You move onto the next level.\nSwim or wait?\nAnswer:").lower()
  if action_2 == "wait":
    action_3 = input("You move onto the next level.\nWhich door? Red,Blue,Yellow.\nAnswer:").lower()
    if action_3 == "yellow":
      print("\n\n\nYou Win this time!!\n\n\n")
  else:
    print("Sorry u ded")
else:
  print("Sorry u ded")