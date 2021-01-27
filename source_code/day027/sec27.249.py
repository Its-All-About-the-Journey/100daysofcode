import tkinter


def button_clicked() -> None:
    np_label["text"] = input_text.get()


if __name__ == "__main__":
    # Window setup
    window = tkinter.Tk()
    window.title("NP GUI")
    window.minsize(500, 300)

    # Label setup
    np_label = tkinter.Label(text="NetworkPistol", font=("Arial", 24, "bold"))
    np_label.pack(side="left")

    # Change text via attribute
    np_label["text"] = "NP"

    # Change text via method
    np_label.config(text="NP Config")

    # Button
    button = tkinter.Button(text="Click Me", command=button_clicked)
    button.pack()

    # Entry
    input_text = tkinter.Entry(width=10)
    input_text.pack()

    window.mainloop()
