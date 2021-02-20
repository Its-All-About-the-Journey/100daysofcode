import tkinter
from tkinter.constants import END

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=400)
#Add padding around entire application window
window.config(padx=20, pady=30)


#Label
label = tkinter.Label(text="I am a label", font=("Calibri", 24, "bold"))
label.grid(column=0, row=0)
#Add padding around specific item
label.config(padx=50, pady=50)
#label.pack(expand=True)

#Changing label text
label["text"] = "New text"
#or
label.config(text="New text")

#Buttons

def button_click():
    #print("I got clicked")
    label["text"] = "Button clicked"

my_button = tkinter.Button(text="Click Me", command=button_click)
my_button.grid(column=1, row=0)



#Input Box
input = tkinter.Entry(width=10)
input.grid(column=0, row=1)

#Collect input and populate text label
label2 = tkinter.Label(text="I am a label", font=("Calibri", 24, "bold"))
label2.grid(column=1, row=1)
label2.config(text="Test")

def button2_click():
    label2["text"] = input.get()

my_button2 = tkinter.Button(text="Collect Input", command=button2_click)
my_button2.grid(column=2, row=1)


def button3_click():
    print("Clicked button 3")

my_button3 = tkinter.Button(text="Button in col 3", command=button3_click)
my_button3.grid(column=2, row=0)


#Entry box
entry = tkinter.Entry(width=30)
entry.insert(END, string="Starting text")
entry.grid(column=0, row=2)


#Text box (multiline)
text = tkinter.Text(height=5, width=30)
#Starts cursor in textbox
text.focus()
#Starting text
text.insert(END, "Example text to start.")
#Get current value at line 1, character 0
print(text.get("1.0", END))
text.grid(column=0, row=3)


#Spinbox (counter)
def spinbox_used():
    #gets current spinbox value
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0,to=20,width=5,command=spinbox_used)
spinbox.grid(column=0, row=4)


#Scale (slider)
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.grid(column=4, row=4)



#Tickbox
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on (built in function)
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=0, row=5)


#Radio Buttons
def radio_used():
    print(radio_state.get())
#Variable to hold which radio button is checked
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0, row=6)
radiobutton2.grid(column=1, row=6)


#List
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
#Variable to hold current list box choice
listbox = tkinter.Listbox(height=4)
fruits = ["Apple","Pear", "Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=0, row=7)



while True:
    window.mainloop()