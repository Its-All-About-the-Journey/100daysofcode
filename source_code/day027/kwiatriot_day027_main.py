import tkinter


def button_clicked():
    print("Button clicked")
    new_text = text_entry.get()
    # The config method modifies the attribute
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=300)

# Creating a label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
# Labels use the pack() method to be applied to the window
my_label.grid(column=0, row=0)
# can also use the place method, which takes an x and y value
# my_label.place(x=100, y=100)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New button
button1 = tkinter.Button(text="Another click")
button1.grid(column=2, row=0)

# Entry field
text_entry = tkinter.Entry(width=10)
text_entry.grid(column=3, row=2)


window.mainloop()
