import tkinter as tk
from requests import Session
from requests.models import HTTPError

api_tool = Session()
api_endpoint = "https://api.kanye.rest/?format=text"  # Cheater


def get_quote():
    """
    Get text quote and update canvas text.
    """
    quote = api_tool.get(api_endpoint)

    try:
        quote.raise_for_status()
        canvas.itemconfig(quote_text, text=quote.text)

    except HTTPError:
        pass


window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(file="./kanye/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 18, "bold"),
    fill="black"
    )

canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="./kanye/kanye.png")
kanye_button = tk.Button(
    image=kanye_img,
    highlightthickness=0,
    command=get_quote
    )
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()
