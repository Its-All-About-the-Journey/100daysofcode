# 100 Days of Code: Python
# Mail Merge Example
# Adam Pawlowski (@hypermanganate)

# Boy the training wheels came off for this one, just go google it I guess.
# This doesn't have any output so I added some just for fun.

print("Beginning mail merge example program.")

# You can't .close() after reading, as it becomes a string object.
# Hopefully it will be okay.
starting_letter = open("./Input/Letters/starting_letter.txt", "r").read()

print(f"Loaded template:\n-----\n{starting_letter}\n-----\n")

# The idea here would be to be familiar with readlines
# instead of reading it all as a string.
names = open("./Input/Names/invited_names.txt", "r").read().split("\n")

print(f"Got {len(names)} names to merge.")

# You could replace the name in letter[0] and print the rest I guess.
for name in names:
    with open(file=f"./Output/ReadyToSend/{name}.txt", mode="w") as out_file:
        out_file.write(starting_letter.replace("[name]", name))

print ("Mail merge complete.")
