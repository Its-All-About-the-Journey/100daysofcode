from tkinter import *
from tkinter import messagebox
import os
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def find_password():
	# Check to make sure user entered a value to search for...
	if website_entry.get():
		try:
			with open('password_manager.json', 'r') as json_file:
				# Read in existing password data
				existing_data = json.load(json_file)
				# Read in user entry
				website = website_entry.get().lower()

				# Attempt to get dictionary by that name and display results
				website_dict = existing_data[website]
				email = website_dict['email']
				password = website_dict['password']

				# Display messagebox with info
				messagebox.showinfo(title=f"Credentials for {website}", message=f"Website: {website}\nEmail/Username: "
				                                                                f"{email}\nPassword: {password}")

		except FileNotFoundError:
			messagebox.showerror(title="No Data File Found",
			                     message="Unable to find an existing password manager data file.")
		except KeyError as key:
			messagebox.showerror(title="No Data Found",
			                     message=f"No details for the website {key} have been found.")
	else:
		messagebox.showerror(title="No Search Value Entered",
		                     message="Please enter a value to search for...")

def gen_pass():
	# Select a random number of letters, numbers and symbols
	nr_letters = random.randint(8, 10)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)

	# Generate a list containing randomly selected letters, numbers and symbols
	password = [random.choice(letters) for i in range(nr_letters)]
	[password.append(random.choice(symbols)) for i in range(nr_symbols)]
	[password.append(random.choice(numbers)) for i in range(nr_numbers)]

	# Shuffle the list and join the list into a single string
	random.shuffle(password)
	password = ''.join(password)

	# Add the password to the entry box
	password_entry.delete(0, END)
	password_entry.insert(0, password)

	# Automatically copies the generated password into users clipboard
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
	# Get the users entries
	website = website_entry.get().lower()
	email_user = email_user_entry.get()
	password = password_entry.get()

	# Create user data dictionary
	user_data = {
		website: {
			"email": email_user,
			"password": password,
		}
	}

	# Check to make sure none of the entries are blank -> show error if one is
	if not website or not email_user or not password:
		messagebox.showerror(title="Invalid Entry", message="You have left one or more fields blank.")
	# Otherwise, proceed with read/write
	else:
		try:
			with open('password_manager.json', 'r') as json_file:
				# Read in existing data
				existing_data = json.load(json_file)
				# Update existing data with new data
				existing_data.update(user_data)
			with open('password_manager.json', 'w') as json_file:
				# Save updated data back to file
				json.dump(existing_data, json_file, indent=4)
		except FileNotFoundError:
			with open('password_manager.json', 'w') as json_file:
				json.dump(user_data, json_file, indent=4)
		except json.decoder.JSONDecodeError:
			with open('password_manager.json', 'w') as json_file:
				json.dump(user_data, json_file, indent=4)


		# Finally, delete the entries and refocus cursor
		website_entry.delete(0, END)
		password_entry.delete(0, END)
		website_entry.focus()

# ---------------------------- UI SETUP ------------------------------ #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file='logo.png')
canvas.create_image(130, 100, image=lock)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", width=13, anchor='e')
website_label.grid(row=1, column=0)
email_user_label = Label(text="Email/Username:", width=13, anchor='e')
email_user_label.grid(row=2, column=0)
password_label = Label(text="Password:", width=13, anchor='e')
password_label.grid(row=3, column=0)

# Entry Boxes
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_user_entry = Entry(width=59)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, "DefaultEmail@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass = Button(text="Generate Password", width=21, command=gen_pass)
generate_pass.grid(row=3, column=2)
add = Button(text="Add", width=50, command=add_password)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", width=21, command=find_password)
search.grid(row=1, column = 2)

window.mainloop()
