from tkinter import *


def miles_to_km() -> None:
    # Convert miles to km
    lbl_km_value["text"] = float(txt_box.get()) * 1.609


if __name__ == '__main__':
    window = Tk()
    window.minsize(300, 200)
    window.title("Miles to Kilometer Converter")
    window.config(padx=50, pady=50)

    txt_box = Entry(width=10)
    txt_box.grid(row=0, column=1)

    lbl_miles = Label(text="Miles")
    lbl_miles.grid(row=0, column=2)

    lbl_equal = Label(text="is equal to")
    lbl_equal.grid(row=1, column=0)

    lbl_km_value = Label()
    lbl_km_value.grid(row=1, column=1)

    lbl_km = Label(text="Km")
    lbl_km.grid(row=1, column=2)

    btn_calculate = Button(text="Calculate", command=miles_to_km)
    btn_calculate.grid(row=2, column=1)

    window.mainloop()
