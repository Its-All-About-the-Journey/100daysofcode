from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=450)
window.config(padx=50, pady=50)  # Add padding around the entire window

# Labels
my_label = Label(text="I am a Label", font=("Arial", 24, 'bold'))
# Ways to change properties once the label is created
my_label['text'] = "New Text"
my_label.config(text='New Text')
my_label.grid(row=0, column=0)


# Button Event Listener Function - gets text from input box and puts into label when button clicked
def button_clicked():
	text = input.get()
	my_label.config(text=text, bg='red', padx=20, pady=20)  # Changes text when button is clicked and adds padding


button = Button(text='Click me', command=button_clicked)
button.grid(row=1, column=1)

button2 = Button(text="New Button")
button2.grid(row=0, column=2)

# Entry
input = Entry(width=20, font=('Arial', 10, 'italic'), foreground='grey')
input.insert(END, string="Some starting text...")
input.grid(row=2, column=3)


# Textbox
text = Text(height=5, width=30)
text.focus()  # focuses cursor on textbox
text.insert(END, "Example of a multi-line text entry.")  # Adds some text to start with
print(text.get("1.0", END))  # Gety's current value in textbox starting at line 1 character 0 (1.0) until the END
# text.pack()

# Spinbox - includes function that prints value each time its used
def spinbox_used():
	print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# Scale
def scale_used(value):
	print(value)

scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# Checkbox/Checkbutton
# Function prints 1 if checked and 0 if unchecked
def checkbutton_used():
	print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checkbutton.pack()

# Radiobutton
def radio_used():
	print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# Listbox
def listbox_used(event):
	# Gets the current selection from the list box
	print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Strawberry']
for index, item in enumerate(fruits):
	listbox.insert(index, item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()
