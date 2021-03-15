from tkinter import *
import requests


def get_quote():
    quote = requests.get(url='https://api.kanye.rest/').json()['quote']
    print(len(quote))
    if len(quote) >= 150:
        canvas.itemconfig(quote_text, font=("Arial", 18, "bold"), text=quote)
    elif len(quote) >= 100:
        canvas.itemconfig(quote_text, font=("Arial", 20, "bold"), text=quote)
    elif len(quote) >= 70:
        canvas.itemconfig(quote_text, font=("Arial", 22, "bold"), text=quote)
    else:
        canvas.itemconfig(quote_text, font=("Arial", 30, "bold"), text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()
