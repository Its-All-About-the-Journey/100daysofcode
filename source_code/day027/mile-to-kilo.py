import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=30)

def calculate_click():
    kilo["text"] = round((float(miles_input.get()) * 1.60934),2)

#Miles Label
miles = tkinter.Label(text="Miles", font=("Calibri", 12, "bold"))
miles.grid(column=2, row=0)

#Is Equal To Label
equals = tkinter.Label(text="is equal to", font=("Calibri", 12, "bold"))
equals.grid(column=0, row=1)

#Number of Kilometers Label
kilo = tkinter.Label(text="0", font=("Calibri", 12, "bold"))
kilo.grid(column=1, row=1)

#Km Label
km = tkinter.Label(text="Km", font=("Calibri", 12, "bold"))
km.grid(column=2, row=1)

#Miles Entry Box
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

#Calculate Button
calculate_button = tkinter.Button(text="Calculate", command=calculate_click)
calculate_button.grid(column=1, row=2)

while True:
    window.mainloop()