
# DAY 27

Miles to Kilometers Project

# Description

Use this application to convert miles to kilometers, or vice versa.

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

tk

# How to run script
```
Call the script

Enter the number and select the type of unit to convert from

Click convert to see the result
```

# Sample output

![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day027/app.png)

# Other Exercises

## * args adder

```
def add(*args):
    print(sum(args))

add(1, 3, 5, 6, 7, 8, 10, 22, 33, 55)
```

## tK example layout

```
import tkinter


def exit_button_clicked():
    print("Exiting...")
    label["text"] = input.get()
    # exit()


# New Window
window = tkinter.Tk()

# Title of Window
window.title = "Whatever"

# Window expands by default, but this is the mininum it should be
window.minsize(width=400, height=400)

# Window border padding example
window["padx"] = 20
window["pady"] = 20

# Text Label Object
label = tkinter.Label(text="Label Example", font=("Arial", 24, "bold"))

# The object needs to be composited for layout
label.grid(column=0, row=0)  # Upper left by default 

# Button Object
button = tkinter.Button(text="Click Here", command=exit_button_clicked)

# Composite this item against master window
button.grid(column=1, row=1)

# Another button
new_button = tkinter.Button(text="Does Nothing")
new_button.grid(column=2, row=0)
```