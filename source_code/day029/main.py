from random import choice, randint, shuffle

import pyperclip
from tkinter import *
from tkinter import messagebox

BG_COLOR = "#0f3057"
FG_COLOR = "#3282b8"
FONT = "arial"
FONT_CFG = (FONT, 12, "bold")
IMAGE_FILENAME = "logo.png"
PASS_FILENAME = "hushhushpass.txt"
PASSWORD_LEN = 25


def add_pass() -> None:
    site = txt_site.get()
    username = txt_username.get()
    password = txt_password.get()

    # TODO: Validate password length, and site syntax via regex.
    # validate fields are not empty
    is_valid = len(site) and len(username) and len(password)

    # TODO: Update if already exists

    if is_valid:
        # Confirm if user wants to add password
        is_ok = messagebox.askokcancel(
                    title="Add password?",
                    message=f"These are the details entered:\n"
                            f"Site: {site}\n"
                            f"Username: {username}\n"
                            f"Password: {password}\n"
                )

    else:
        # TODO: Show information of what caused error.
        messagebox.showerror(
            title="Incomplete",
            message=f"These are the details entered:\n"
                    f"Site: {site}\n"
                    f"Username: {username}\n"
                    f"Password: {password}\n"
        )
        is_ok = False

    # TODO: Encrypt password
    # TODO: Write serialized data.  JSON or YAML

    if is_ok and is_valid:
        # Append to file
        with open(PASS_FILENAME, "a") as file_out:
            file_out.write(
                f"{site},"
                f"{username},"
                f"{password}\n"
            )

        # Copy password to clipboard
        # TODO: NOT WORKING ON UBUNTU, APPEARS TO REQUIRE SOME DEPENDENCY xclip or xsel
        # pyperclip.copy(txt_password.get())
        # Schedule callback to reset clipboard after 1 min
        # window.after(1000 * 60, clear_clipboard)

        reset_entries()


def clear_clipboard() -> None:
    pyperclip.copy("")

def generate_pass() -> None:
    # TODO: Generate passwords based on rules
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # TODO: Add random letter case

    password_list = [choice(letters)  for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    txt_password.delete(0, END)
    txt_password.insert(0, "".join(password_list))


def reset_entries():
    txt_site.delete(0, END)
    txt_password.delete(0, END)
    txt_site.focus()


if __name__ == '__main__':

    window = Tk()
    window.title("Hush Hush")
    window.config(padx=20, pady=20, bg=BG_COLOR)

    # Setup background image
    image = PhotoImage(file=IMAGE_FILENAME)
    image_width = image.width()
    image_height = image.height()
    canvas = Canvas(width=image_width, height=image_height, bg=BG_COLOR, highlightthickness=0)
    canvas.create_image(image_width / 2, image_height / 2, image=image)
    canvas.pack()

    # Setup Fields, label and entry
    lbl_site = Label(text="Website", bg=BG_COLOR, fg=FG_COLOR, font=FONT_CFG)
    txt_site = Entry(width=35)
    txt_site.focus()

    lbl_username = Label(text="Username", bg=BG_COLOR, fg=FG_COLOR, font=FONT_CFG)
    txt_username = Entry(width=35)
    txt_username.insert(0, "username@gmail.com")

    lbl_password = Label(text="Password", bg=BG_COLOR, fg=FG_COLOR, font=FONT_CFG)
    txt_password = Entry(width=35)

    btn_generate_pass = Button(text="Generate", command=generate_pass, highlightthickness=0)
    btn_add_pass = Button(text="Add", command=add_pass, highlightthickness=0)

    # Setup Grid layout with spanning columns
    canvas.grid(row=0, column=0, columnspan=3)

    lbl_site.grid(row=1, column=0, padx=5, pady=5)
    txt_site.grid(row=1, column=1, columnspan=2)

    lbl_username.grid(row=2, column=0, padx=5, pady=5)
    txt_username.grid(row=2, column=1, columnspan=2)

    lbl_password.grid(row=3, column=0, padx=5, pady=5)
    txt_password.grid(row=3, column=1, columnspan=2)

    btn_generate_pass.grid(row=4, column=1, pady=15)
    btn_add_pass.grid(row=4, column=2)

    window.mainloop()
