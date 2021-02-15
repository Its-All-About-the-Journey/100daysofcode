from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=115)
window.config(padx=30, pady=20)

# Entry
input = Entry(width=10, font=('Arial', 12, 'normal'))
input.grid(row=0, column=1)

# Labels
miles = Label(text="Miles", font=("Arial", 12, 'normal'))
miles.grid(row=0, column=2)
equal = Label(text="is equal to", font=("Arial", 12, 'normal'))
equal.grid(row=1, column=0)
kilometers_output = Label(text=" ", font=("Arial", 12, 'normal'))
kilometers_output.grid(row=1, column=1)
km_label = Label(text="Km", font=("Arial", 12, 'normal'))
km_label.grid(row=1, column=2)

# Button
def button_clicked():
	kilometers = round(int(input.get()) * 1.609344, 2)
	kilometers_output.config(text=str(kilometers), foreground='green')

button = Button(text='Calculate', command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()