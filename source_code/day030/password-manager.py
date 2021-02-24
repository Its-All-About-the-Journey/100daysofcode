from json.decoder import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#import string

BLACK = "#010101"
WHITE = "#FFFFFF"
FONT_NAME = "Calibri"
PATH = "source_code/day030/"
SYMBOLS = "!@#$%?+*!@#$%?+*"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
PASS_LENGTH = 20
EMAIL = "test@test.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    #password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(PASS_LENGTH))
    password = ''.join(random.choices(f"{''.join([SYMBOLS,LETTERS,LETTERS.lower(),NUMBERS])}", k=PASS_LENGTH))
    password_input.delete(0, 'end')
    password_input.insert(0,password)

    #This copies the password and clears it when the window is closed
    #window.clipboard_clear()
    #window.clipboard_append(password)

    #This is the "official" password copy-to-clipboard function
    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------- #

def search_accounts():
    website = website_input.get()
    try:
        with open (f"{PATH}data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(website, f"Username: {data[website]['account']}\nPassword: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No data exists yet.")
    except KeyError:
        messagebox.showinfo("Not Found", "Account Not Found.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    account = account_input.get()
    password = password_input.get()
    if website == "":
        messagebox.showerror("Error", "Website field is blank.")
    elif account == "":
        messagebox.showerror("Error", "Account field is blank.")
    elif password == "":
        messagebox.showerror("Error", "Password field is blank.")
    else:
        passlist = {
            website: {
                "account" : account,
                "password" : password
            }
        }
        try:
            with open (f"{PATH}data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open (f"{PATH}data.json", "w") as file:
                json.dump(passlist,file, indent=4)
        else:
            data.update(passlist)
            with open (f"{PATH}data.json", "w") as file:
                json.dump(data,file, indent=4)

        website_input.delete(0, 'end')
        password_input.delete(0, 'end')
        messagebox.showinfo("Success", f"{website} account has been saved.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg=BLACK)
background_image = PhotoImage(file=f"{PATH}logo.png")
window.iconphoto(False, background_image)

#Build canvas with background iamge (HIGHLIGHT THICKNESS = border for canvas)
canvas = Canvas(width=200, height=200,bg=BLACK,highlightthickness=0)
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1,row=0)

#Website Label
website_label = Label(text="Website:", font=(FONT_NAME, 12, "normal"), fg=WHITE, bg=BLACK)
website_label.grid(column=0, row=1, pady=5, sticky=E)

#Website Entry Box
website_input = Entry(width=30)
website_input.focus()
website_input.grid(column=1, row=1, sticky = W, pady=5)

#Search Button
search_button = Button(text="Search", command=search_accounts, highlightthickness=0)
search_button.grid(column=2, row=1, sticky = W+E, pady=5)

#Email/Username Label
account_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "normal"), fg=WHITE, bg=BLACK)
account_label.grid(column=0, row=2, pady=5, sticky=E)

#Account Entry Box
account_input = Entry()
account_input.grid(column=1, row=2, columnspan=2, sticky = W+E, pady=5)
account_input.insert(0, EMAIL)

#Password Label
password_label = Label(text="Password:", font=(FONT_NAME, 12, "normal"), fg=WHITE, bg=BLACK)
password_label.grid(column=0, row=3, pady=5, sticky=E)

#Password Entry Box
password_input = Entry(width=30)
password_input.grid(column=1, row=3, pady=5, sticky = W)

#Generate Password Button
gen_password_button = Button(text="Generate Password", command=gen_password, highlightthickness=0)
gen_password_button.grid(column=2, row=3, pady=5)

#Add Button
add_button = Button(text="Save Password", command=save_password, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2, sticky = W+E, pady=5)

window.mainloop()