import tkinter
from tkinter.constants import END

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=400)


#Label
label = tkinter.Label(text="I am a label", font=("Calibri", 24, "bold"))
label.pack()
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
my_button.pack()



#Input Box
input = tkinter.Entry(width=10)
input.pack()

#Collect input and populate text label
label2 = tkinter.Label(text="I am a label", font=("Calibri", 24, "bold"))
label2.pack()
label2.config(text="")

def button2_click():
    label2["text"] = input.get()

my_button2 = tkinter.Button(text="Collect Input", command=button2_click)
my_button2.pack()



#Entry box
entry = tkinter.Entry(width=30)
entry.insert(END, string="Starting text")
entry.pack()


#Text box (multiline)
text = tkinter.Text(height=5, width=30)
#Starts cursor in textbox
text.focus()
#Starting text
text.insert(END, "Example text to start.")
#Get current value at line 1, character 0
print(text.get("1.0", END))
text.pack()


#Spinbox (counter)
def spinbox_used():
    #gets current spinbox value
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0,to=20,width=5,command=spinbox_used)
spinbox.pack()


#Scale (slider)
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()



#Tickbox
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on (built in function)
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#Radio Buttons
def radio_used():
    print(radio_state.get())
#Variable to hold which radio button is checked
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#List
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
#Variable to hold current list box choice
listbox = tkinter.Listbox(height=4)
fruits = ["Apple","Pear", "Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



while True:
    window.mainloop()