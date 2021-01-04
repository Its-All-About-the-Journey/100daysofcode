# Final - treasure island game
# ---------------------------------------------------------
print('''
            88                                          
            ""                         ,d               
                                       88               
8b,dPPYba,  88 8b,dPPYba, ,adPPYYba, MM88MMM ,adPPYba, ,adPPYba,  
88P'    "8a 88 88P'   "Y8 ""     `Y8   88   a8P_____88 I8[    ""  
88       d8 88 88         ,adPPPPP88   88   8PP"""""""  `"Y8ba,  
88b,   ,a8" 88 88         88,    ,88   88,  "8b,   ,aa aa    ]8I  
88`YbbdP"'  88 88         `"8bbdP"Y8   "Y888 `"Ybbd8"' `"YbbdP"'  
88                                                      
88                                                    
''')
print("\nwelcome to the game of pirates.\n")
print("where we don't use capital letters and your mission is to find the treasure.")

def play():

  # question 1
  direction = input("\nwhich way first, matey: left or right? ")
  if direction.lower() != "left":
    print("\noh no. you're not going to like this. you caught the scurves...and died. oh, yeah, what a twist.")
    return

  # question 2
  action = input("\nhigh tide in the bay, strumpet, shall we: wait or swim? ")
  if action != "wait":
    print("\nyou wench, you can't swim. say hello to davey jones for me...oh and you died.")
    return

  # question 3
  door = input("\nwhich door will it be ya bilge rat: red, blue or yellow? ")
  if door != "yellow":
    print("\naaaaaaaaaaaaaand you survived. no, actually, you died.")
    return

  print("\na left turn ye did, then waited before ye picked the yellow door. smart, smart, very smart. the treasure be yours me hearty...yo ho.")

play()