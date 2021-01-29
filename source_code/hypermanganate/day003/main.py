#!/usr/bin/env python3
# 100 Days of Code : Day 2 Project
# Treasure Island Simulator
# Adam Pawlowski (@hypermanganate)

print('''
*******************************************************************************
                                   ___
                                _-"_-"
                              _-_-"
                           _-_-"
  _______________________-"-"_
  \                          /
   \  HOT SOUP IN HERE !!!  /   mga
.--_\______________________/_--.
 ""--------------------------""
*******************************************************************************
''')
print("Welcome to Treasure Island Total Landscaping.")
print("Your mission is to load up your landscaping truck for a full day's work. There isn't much time, so move quickly, if you want to earn that greenback treasure.\n")
print("It's dark and dreary at 4:30 AM, and without coffee your eyes are barely open. It's your third day, and you're ready to show off your stuff.")

choice = input("You've got to get into the shop, but there are two possible doors. You can't remember which door to take. Type 'left' or 'right' to choose.\n")

print("\nThe door creaks open, but there's no lighting. Fearless, you venture forward...")

if not choice.lower() == 'left':
  print("...and fall into a pit of fertilizer.")
  exit("Game Over.")

print("...and step inside. You hear the crew chatting somewhere in the distance.")
print("You fumble forward in the dark, arms out, slowly making your way.")
print("You feel something cold against your arm as you reach forward!\n")
print("Startled awake, you try and step aside but trip over a garden hose, and knock over a massive tank of some sort.")
print("Squinting and feeling ahead you notice the floor is covered in liquid.\n")
print('"Maybe if I wait", you think, "It\'ll drain off. But, then I\'ll be late!"\n')
choice = input("What do you do? Do you wait and hope it drains in time, or do you go for a swim? Type 'wait' or 'swim' now to choose.\n")

print("\nRemembering your cell phone, you pull it out, and activate the flashlight.")
print("Peering at the water all you can see is your own reflection.")
print("You take a deep breath...\n")

if not choice.lower() == 'wait':
    print("\n...and jump forward, splashing the water like a child in a puddle.")
    print('"Ha!", you think to yourself, "There was nothing to be ..."')
    print("Suddenly, you feel something tugging at your pant leg.")
    print("Slipping, you begin to fall into the water, letting your phone escape your grasp!\n")
    print("Falling to the bottom of the pool, the light cast a story on the wall in front of you - your story! It plays out before your eyes as your clothes are torn away by a tremendous force.")
    print("You turn your head as the froth begins to burn like a thousand cuts, all at once.\n")
    print("Your eyes pause briefly, just long enough to recognize the writing on the tank you'd knocked over, before your vision fades:")
    print("'Caution: Defective Trout! Do not use!'\n")
    print("It was too late the heed the warning now. Looks like you won't even make it through your first day.")
    exit("Game Over.")

print("\n...and notice the shimmering liquid begin to recede.")
print("Patiently, you wait a moment while the path clears for you to proceed.\n")
print("You hear your boss, Tony, off in the distance. You can't make it out, but he sounds impatient.")
print("Hoping to still make a good first impression you round the corner, finding a dimly lit hallway.\n")
print("Ahead you see three doors: red, yellow, and blue.")
print("You see light peering out from under the red and yellow doors, but the blue door is ajar.\n")
print('"Where is that kid, anyway?", the voice breaking your stare. You\'re not sure where it came from, but you\'d better find it fast.\n')

choice = input("Which door do you choose? Type 'red', 'yellow', or 'blue' now.\n")
choice = choice.lower()

if choice == 'red':
  print("\nRushing forward towards the red door, you push it aside brusquely.")
  print("Ahead lies a metal staircase which you begin to climb down, as the door slams shut.")
  print("A warm light guides you further, until you enter a room filled with pipes and valves.")
  print("The light is coming from a ghastly old furnace, fueled by gas, oil, or something you're not quite sure. A massive blue flame is before you.\n")
  print("'This isn't right', you think, and head back up the stairs.")
  print("You tug at the door, but it's jammed!")
  print("You bang on the door, yelling for help, but none comes.")
  print("After a few minutes you return to the gas works.\n")
  print("'Well', you think, 'it's cold out, so maybe if I turn off the heat they'll come and find me!'")
  print("You spin some knobs until the glow of the flame turns yellow, and dies down.")
  print("Minutes later, in the company breakroom, your boss Tony notices the chill.")
  print('"Dang furnace", he remarks, as he reaches for the thermostat and gives it a twist.\n')
  print("Staring at the flickering flame you begin to hear a hiss. Smelling gas, you try everything, reaching up to pull a lever.")
  print("With the damper now closed, both you and the flame are left competing for the oxygen in the room.\n")
  print("You hear a click, and see a fireball heading towards you. You haven't even a moment.")
  print("The terrific heat surrounds you until you feel it no more.\n")
  print("Game Over")
elif choice == 'blue':
  print("\nYou shuffle forward and brush open the blue door.")
  print("Looking inside, you see a number of crates of peat, stacked behind barrels of wood chips.")
  print("There's a light behind the crates, and a sound, almost like a shuffling.\n")
  print("'They\'re leaving without me!', you think.")
  print("Rushing around the crates, you begin to call out, 'Wait!'")
  print("You trip into a writhing mountain of peat.\n")
  print("'Writhing?' you think to yourself, but not fast enough without caffeine.")
  print("The mass of rats swallows you up before you get another chance to yell, adding you to the growing mass of decaying dirt at the rear of the shop.\n")
  print("The beasts have felled you, and had their fill.\n")
  print("Game Over")
elif choice == 'yellow':
  print("\nYou march forward and swing open the yellow door.")
  print("All sound stops, a silent, heavy air filling the room.")
  print("Your eyes adjust to the bright light...\n")
  print('"It\'s him!", shouts Tony, "I knew he\'d show back up! The kid looked like a real worker the moment I saw him."')
  print("Tony holds out his hand while another one of your would-be crewmates hands him $5.")
  print('"Well, kid, coffee\'s on me this morning!", said Tony.\n')
  print('"What are ya waitin\' for?", he says, tossing you a ballcap.')
  print('"Let\'s get to work!"\n')
  print("And with that, you and the crew begin to pack out all the supplies you'll need for a day on the job.")
  print("Having survived that harrowing ordeal, the rest of the day was a breeze.\n")
  print("Before you know it, it's quitting time, and you're on your way home with pockets just a bit heavier than when you started the day.")
  print("Dreaming of the hot-rod bicycle you'd be riding before summer's end, you eagerly settle in for a good night's sleep.\n")
  print("After all, if you made it through day three, how could day four be any worse?\n")
  print("You Win")
else:
  print("A dizzy spell overtakes you. Perhaps it is the fumes from the two-cycle lawn tools, perhaps it is your lack of coffee.")
  print("You lean against the wall to rest and find yourself slipping to the floor.")
  print("'Perhaps, Landscaping wasn't for me', you think. 'Maybe I should have gone into magazine sales.'")
  print("You contemplate your choices as the world goes black.")
  print("Game Over.")

