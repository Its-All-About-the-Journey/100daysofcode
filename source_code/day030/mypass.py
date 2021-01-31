import json
from random import choice, randint, shuffle
import re

try: 
    import pyperclip
    PYPERCLIP_INSTALLED = True

except ImportError:
    PYPERCLIP_INSTALLED = False

try:
    from tkinter import *
    from tkinter import messagebox

except ImportError:
    print("Python 3 Tkinter package is not present on your system.")
    exit()

import constants as CONST


# Variable to point to the callback window schedule
clipboard_schedule = None 
database = dict()


def clipboard_clear() -> None:
    if not PYPERCLIP_INSTALLED:
        return None
    
    pyperclip.copy("")


def clipboard_copy(data: str) -> None:
    global clipboard_schedule

    if not PYPERCLIP_INSTALLED:
        return None
    
    # Copy password to clipboard
    pyperclip.copy(data)

    #Schedule callback to reset clipboard after 1 min
    clipboard_schedule = window.after(CONST.CLEAR_CLIPBOARD_TIME, clipboard_clear)


def clipboard_delete() -> None:
    
    if not PYPERCLIP_INSTALLED:
        return None

    if clipboard_schedule:
        window.after_cancel(clipboard_schedule)
    
    # Clear clipboard so no password lives in clipboard
    clipboard_clear()


def credentials_str(credentials: list) -> str:
    text = ""

    for credential in credentials:
        text += f"{credential['username']}\n--> {credential['password']}\n\n"
    
    return text


def database_dump() -> None:
    with open(CONST.DATABASE_FILENAME, "w") as db_out:
        json.dump(database, db_out, indent=4)


def database_load() -> None:
    try:
        with open(CONST.DATABASE_FILENAME) as db_in:
            database.update(json.load(db_in))
    except FileNotFoundError:
        # First time running. Ignore exception
        pass

    except json.decoder.JSONDecodeError:
        # Database is malformed
        msg_box("showerror", "DATABASE ERROR", "Database is corrupted.")


def database_update(site: str, credentials: dict) -> None:
    if site in database:
        # TODO: If credentials exist, update new password
        database[site].append(credentials)
   
    else:
        database[site] = list()
        database[site].append(credentials)        

    # Keep database file synced with loaded data
    database_dump()


def find_pass(site: str) -> list:
    if site in database:
        return database[site]
    
    else:
        return None


def generate_pass() -> None:
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    nr_letters = CONST.PASSWORD_MIN_LEN - nr_symbols - nr_numbers

    password_list = [choice(CONST.LETTERS)  for _ in range(nr_letters)]
    password_list += [choice(CONST.SYMBOLS) for _ in range(nr_symbols)]
    password_list += [choice(CONST.NUMBERS) for _ in range(nr_numbers)]

    shuffle(password_list)

    txt_password.delete(0, END)
    txt_password.insert(0, "".join(password_list))


def is_data_valid(site: str, username: str, password: str) -> tuple:
    # validate fields are not empty
    return is_site_valid(txt_site.get()), bool(len(txt_username.get())), is_password_valid(txt_password.get())


def is_password_valid(password: str) -> bool:
    # Passwords requires at least one letter, number, and symbol
    # Password length must be greater than or equal to PASSWORD_MIN_LEN
    letters = sum([password.count(char) for char in CONST.LETTERS])
    numbers = sum([password.count(char) for char in CONST.NUMBERS])
    symbols = sum([password.count(char) for char in CONST.SYMBOLS])

    return letters and numbers and symbols and (letters + numbers + symbols >= CONST.PASSWORD_MIN_LEN)


def is_site_valid(site: str) -> bool:
    # TODO: Validate site syntax via regex.
    return bool(len(site))


def msg_box(method: str, title: str, message: str) -> bool:
    func = getattr(messagebox, method)

    return func(title=title, message=message)


def reset_text_boxes() -> None:
    txt_site.delete(0, END)
    txt_password.delete(0, END)
    txt_site.focus()


def save_pass() -> None:
    site = txt_site.get()
    username = txt_username.get()
    password = txt_password.get()

    valid_site, valid_username, valid_password = is_data_valid(site, username, password)

    if valid_password and valid_username and valid_password:
        # TODO: Encrypt password
        
        # Update data dictionary
        database_update(site, {"username": username, "password": password})
        clipboard_copy(password)
        reset_text_boxes()

    else:
        # Data is not acceptable
        valid_prefix = "   "
        invalid_prefix = "* "

        message = (
            f"These are the details entered:\n\n"
            f"{valid_prefix if valid_site else invalid_prefix}Site: {site}\n"
            f"{valid_prefix if valid_username else invalid_prefix}Username: {username}\n"
            f"{valid_prefix if valid_password else invalid_prefix}Password: {password}\n\n"
        )

        message += "Note: * --> invalid data"
        msg_box("showerror", "Invalid data", message)


def search_pass() -> None:

    site = txt_site.get()

    if not is_site_valid(site):
        msg_box("showerror", "Invalid website format", f"Invalid format:\n\n--> '{site}'")
        
        return None
    
    credentials = find_pass(site)
    
    if credentials:
        # TODO: Allow user to copy password to clipboard
        msg_box("showinfo", f"{site} credentials on file", credentials_str(credentials))
    
    else:
        msg_box("showinfo", f"{site} search results", f"No credentials were found for website:\n\n--> {site}")


if __name__ == '__main__':
    # Setup window
    window = Tk()
    window.title("Hush Hush 🤫")
    window.config(padx=20, pady=20, bg=CONST.BG_COLOR)

    # Setup background image
    image = PhotoImage(file=CONST.IMAGE_FILENAME)
    image_width = image.width()
    image_height = image.height()
    canvas = Canvas(width=image_width, height=image_height, bg=CONST.BG_COLOR, highlightthickness=0)
    canvas.create_image(image_width / 2, image_height / 2, image=image)
    canvas.pack()

    # Setup Fields, label and entry
    lbl_site = Label(text="Website", bg=CONST.BG_COLOR, fg=CONST.FG_COLOR, font=CONST.FONT_CFG)
    txt_site = Entry(width=35)
    txt_site.focus()

    lbl_username = Label(text="Username", bg=CONST.BG_COLOR, fg=CONST.FG_COLOR, font=CONST.FONT_CFG)
    txt_username = Entry(width=35)
    txt_username.insert(0, "username@gmail.com")

    lbl_password = Label(text="Password", bg=CONST.BG_COLOR, fg=CONST.FG_COLOR, font=CONST.FONT_CFG)
    txt_password = Entry(width=35)

    btn_search_pass = Button(text="Search", command=search_pass, width=7, highlightthickness=0)
    btn_generate_pass = Button(text="Generate", command=generate_pass, width=7, highlightthickness=0)
    btn_save_pass = Button(text="Save", command=save_pass, width=7, highlightthickness=0)

    # Setup Grid layout with spanning columns
    canvas.grid(row=0, column=0, columnspan=3)

    lbl_site.grid(row=1, column=0, padx=5, pady=10)
    txt_site.grid(row=1, column=1)
    btn_search_pass.grid(row=1, column=2)

    lbl_username.grid(row=2, column=0, padx=5, pady=10)
    txt_username.grid(row=2, column=1)


    lbl_password.grid(row=3, column=0, padx=5, pady=10)
    txt_password.grid(row=3, column=1)
    btn_generate_pass.grid(row=3, column=2, padx=5)

    btn_save_pass.grid(row=4, column=2)

    # Load database
    database_load()

    window.mainloop()

    # Clean up clipboard
    clipboard_delete()
