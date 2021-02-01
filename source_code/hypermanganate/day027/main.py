# 100 Days of Code: Python
# Miles to Kilometers Converter
# Adam Pawlowski (@hypermanganate)

import tkinter
units = "miles"


def compute_value():
    input_value = float(input_data.get())
    output_value = input_value
    if units == "miles":
        # Convert to KM
        output_value = input_value * 1.609
    else:
        # Convert to Miles
        output_value = input_value / 1.609

    result_label['text'] = f"Result: {output_value}"


def exit_button_clicked():
    exit()


def change_unit():
    global units
    units = from_unit.get()
    print(f"Units now {units}")


# New Window
window = tkinter.Tk()

# Title of Window
window.title("Unit Turner-Arounder")

# Window expands by default, but this is the mininum it should be
window.minsize(width=400, height=200)

# Window border padding example
window["padx"] = 20
window["pady"] = 20

# Main Label Object
form_label = tkinter.Label(text="Units Converter", font=("Arial", 24, "bold"))

# Instructions Label
instructions_label = tkinter.Label(text="Enter a starting value, choose the" +
                                        " unit type to convert from.\nUnits" +
                                        " will be converted to the other " +
                                        "type\nwhen you press convert.")

# Input Label
input_label = tkinter.Label(text="Convert", font=("bold"))

# Bridge Label
bridge_label = tkinter.Label(text="to", font=("bold"))

# Results Label
result_label = tkinter.Label(text="Results: ")

# Exit Button Object
exit_button = tkinter.Button(text="Exit", command=exit_button_clicked)

# Go Button Object
go_button = tkinter.Button(text="Go", command=compute_value)

# Starting Unit Text Input
input_data = tkinter.StringVar(value="10")
from_value_input = tkinter.Entry(textvariable=input_data)

# Unit Choice Selector
from_unit = tkinter.StringVar(value="miles")

miles_choice = tkinter.Radiobutton(command=change_unit,
                                   indicatoron=False,
                                   text="Miles",
                                   variable=from_unit,
                                   value="miles"
                                   )
kilometers_choice = tkinter.Radiobutton(command=change_unit,
                                        indicatoron=False,
                                        text="Kilometers",
                                        variable=from_unit,
                                        value="kilometers"
                                        )

# Composite the window
form_label.grid(column=0, row=0, columnspan=4)
instructions_label.grid(column=0, row=1, columnspan=4)

input_label.grid(column=0, row=2, rowspan=2)
from_value_input.grid(column=1, row=2, rowspan=2)
bridge_label.grid(column=2, row=2, rowspan=2)

miles_choice.grid(column=3, row=2)
kilometers_choice.grid(column=3, row=3)

result_label.grid(column=1, row=4, sticky="w")

go_button.grid(column=0, row=5, columnspan=3)
exit_button.grid(column=1, row=5, columnspan=3)

input_label.focus()

# At the end of program, to listen for events
window.mainloop()
