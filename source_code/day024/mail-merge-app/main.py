#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
INPUT_PATH = "source_code/day024/mail-merge-app/Input/"
OUTPUT_PATH = "source_code/day024/mail-merge-app/Output/ReadyToSend/"

with open(f"{INPUT_PATH}Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open(f"{INPUT_PATH}Letters/starting_letter.txt", "r") as letter:
    letter_template = letter.read()
    for name in names:
        name = name.strip("\n")
        new_letter = letter_template.replace("[name]", name)
        with open(f"{OUTPUT_PATH}letter_for_{name}.txt", "w") as new_file:
            new_file.writelines(new_letter)