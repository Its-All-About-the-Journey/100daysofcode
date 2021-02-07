import tkinter

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=300)

# Creating a label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
# Labels use the pack() method to be applied to the window
my_label.pack()






window.mainloop()