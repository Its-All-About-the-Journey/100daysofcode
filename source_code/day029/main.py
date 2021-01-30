from random import choice, randint, shuffle

import pyperclip
from tkinter import *
from tkinter import messagebox

import constants as CONST


# Variable to point to the callback window schedule
clipboard_schedule = None 


def add_pass() -> None:
    site = txt_site.get()
    username = txt_username.get()
    password = txt_password.get()

    # TODO: Update if already exists

    acceptable_data = is_data_valid()

    message = (
        f"These are the details entered:\n\n"
        f"  Site: {site}\n"
        f"  Username: {username}\n"
        f"  Password: {password}"
    )

    if acceptable_data:
        # Confirm if user wants to save password
        acceptable_data = msg_box("askokcancel", "Add password?", message)

    else:
        # Data is not acceptable
        # TODO: Show information of what caused error.
        msg_box("showerror", "ERROR on data", message)

    if acceptable_data:
        # TODO: Encrypt password
        write_data(f"{site},{username},{password}\n")
        copy_clipboard(password)
        reset_text_boxes()


def clear_clipboard() -> None:
    pyperclip.copy("")


def copy_clipboard(data: str) -> None:
    global clipboard_schedule

    # Copy password to clipboard
    # TODO: NOT WORKING ON UBUNTU, APPEARS TO REQUIRE SOME DEPENDENCY xclip or xsel
    pyperclip.copy(data)

    #Schedule callback to reset clipboard after 1 min
    clipboard_schedule = window.after(CONST.CLEAR_CLIPBOARD_TIME, clear_clipboard)


def delete_clipboard() -> None:
    # If the after
    if clipboard_schedule:
        window.after_cancel(clipboard_schedule)
    
    # Clear clipboard so no password lives in clipboard
    clear_clipboard()
    

def generate_pass() -> None:
    # TODO: Generate passwords based on rules
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(CONST.LETTERS)  for _ in range(nr_letters)]
    password_list += [choice(CONST.SYMBOLS) for _ in range(nr_symbols)]
    password_list += [choice(CONST.NUMBERS) for _ in range(nr_numbers)]

    shuffle(password_list)

    txt_password.delete(0, END)
    txt_password.insert(0, "".join(password_list))


def is_data_valid() -> bool:
    # TODO: Validate password length, and site syntax via regex.
    # validate fields are not empty
    return len(txt_site.get()) and len(txt_username.get()) and len(txt_password.get())


def msg_box(method: str, title: str, message: str) -> bool:
    func = getattr(messagebox, method)

    return func(title=title, message=message)


def reset_text_boxes():
    txt_site.delete(0, END)
    txt_password.delete(0, END)
    txt_site.focus()


def write_data(data: str) -> None:
    # TODO: Write serialized data.  JSON or YAML
    # Append to file
    with open(CONST.PASS_FILENAME, "a") as file_out:
        file_out.write(data)

if __name__ == '__main__':

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

    btn_generate_pass = Button(text="Generate", command=generate_pass, highlightthickness=0)
    btn_add_pass = Button(text="Save", command=add_pass, highlightthickness=0)

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

    # Clean up clipboard
    delete_clipboard()
