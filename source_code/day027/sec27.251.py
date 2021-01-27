from tkinter import *


if __name__ == "__main__":

    window = Tk()
    window.minsize(500,300)
    window.title("Off the Grid!")
    window.config(padx=20, pady=20)

    # Label on grid(0, 0)
    label = Label(text="Grid: 0,0", font=("Arial", 24, "bold"))
    label.grid(row=0, column=0)

    # Button on grid(1, 1)
    button = Button(text="Grid: 1, 1")
    button.grid(row=1, column=1)

    # Button on grid(0, 2)
    button = Button(text="Grid: 0, 2")
    button.grid(row=0, column=2)

    # Entry on grid(2, 3)
    entry = Entry(text="Grid: 2, 3)")
    entry.grid(row=2, column=3)

    window.mainloop()
