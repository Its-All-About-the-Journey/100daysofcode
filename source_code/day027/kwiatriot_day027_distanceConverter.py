from tkinter import *


def button_clicked():
    print("Button clicked")
    miles_to_calc = float(miles_entry.get())
    km_final = miles_to_calc * 1.609
    km_value.config(text=km_final)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=25, pady=50)

# Creating the labels
miles = Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)

equal_to = Label(text="is equal to", font=("Arial", 12))
equal_to.grid(column=0, row=1)

km_value = Label(text="0", font=("Arial", 12))
km_value.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

# Button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)

# Entry field
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)


window.mainloop()
