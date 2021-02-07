import random
import pyperclip
import tkinter as tk
from tkinter import messagebox

APP_BACKGROUND = "white"
FILE_NAME = "app_data.txt"

# ---------------------------- PASSWORD GENERATOR --------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = \
        [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = \
        [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = \
        [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input_var.set(password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def store_data_button():
    store_data()


def store_data():

    data = [website_input_var.get(),
            email_input_var.get(),
            password_input_var.get()]

    if '' in data:
        messagebox.showerror(
                            title="Data Error",
                            message="Data fields are missing."
                            )
        return

    go_ahead = messagebox.askokcancel(
        title=website_input_var.get(),
        message=f"Save username or email {email_input_var.get()} with " +
                f"password {password_input_var.get()} for this website?"
                )

    if go_ahead:

        with open("app_data.txt", mode="a") as file:
            file.write(f"{' | '.join(data)}\n")
            website_input_var.set('')
            password_input_var.set('')


# ---------------------------- UI SETUP ------------------------------- #

# Window


app_window = tk.Tk()
app_window.minsize(width=240, height=240)
app_window.configure(padx=20, pady=20, bg=APP_BACKGROUND)
app_window.title("Password Manager")

# Logo Image

image_canvas = tk.Canvas(
    width=200,
    height=200,
    bg=APP_BACKGROUND,
    highlightthickness=0
    )

logo_image_file = tk.PhotoImage(
    file="./logo.png"
    )
logo_image = image_canvas.create_image(
    100,
    100,
    image=logo_image_file
    )

# Labels

website_label = tk.Label(bg=APP_BACKGROUND, text="Website:")
email_label = tk.Label(bg=APP_BACKGROUND, text="Email/Username:")
password_label = tk.Label(bg=APP_BACKGROUND, text="Password:")

# Input Fields

website_input_var = tk.StringVar()
website_input = tk.Entry(textvariable=website_input_var, width=39)

email_input_var = tk.StringVar()
email_input = tk.Entry(textvariable=email_input_var, width=39)

password_input_var = tk.StringVar()
password_input = tk.Entry(textvariable=password_input_var, width=21)

# Butttons

generate_button = tk.Button(
    text="Generate Password",
    command=lambda: generate_password()
    )

add_button = tk.Button(
    text="Add",
    command=lambda: store_data(),
    width=36
    )

# Composition

image_canvas.grid(row=1, column=0, columnspan=3)

website_label.grid(row=2, column=0)
website_input.grid(row=2, column=1, columnspan=2)

email_label.grid(row=3, column=0, ipadx=2, pady=4)
email_input.grid(row=3, column=1, columnspan=2, pady=4)

password_label.grid(row=4, column=0)
password_input.grid(row=4, column=1)
generate_button.grid(row=4, column=2)

add_button.grid(row=5, column=1, columnspan=2, pady=4)

# Event Loop

app_window.mainloop()
