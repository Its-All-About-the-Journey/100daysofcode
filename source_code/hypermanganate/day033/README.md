
# DAY 33

ISS Notifier

# Description

Application will check for the position of the ISS, against your supplied coordinates. 
It will email you if the ISS is potentially visible.

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

requests 2.25.1

# How to run script

Call the script wherever you'd like to leave such a thing running.
The script will check every 60 seconds if the ISS is overhead based on coordinates.

# Sample output

![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day033/app.png)

# Other Exercises
## Kanye Annoyance

Run main.py under ./kanye/. 
The font doesn't really fit but there wasn't much to this as the API has a .text() method.
She did suggest using JSON but, I didn't.
Unforanately, pressing the Kanye button does not get Kanye help.

## Various API practice

The code is inline with the main application, and was re-used for the ISS final.
I did not use split().
I've used it before, but, in this case I felt I'd rather spend more time playing with datetime.
