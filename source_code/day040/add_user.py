from users import User

print("Welcome to Grant's Flight Club.\nWe find the best flight deals and email you.")

# Loop through and validate users first and last name entries
while True:
	fn = input("What is your first name?\n").capitalize()
	ln = input("What is your last name?\n").capitalize()
	# If either name is empty, ask for names again
	if not fn or not ln:
		print("Must enter valid first and last names...")
		continue
	else:
		break

# Loop through and validate email entries
while True:
	email = input("What is your email address?\n").lower()
	email2 = input("Please confirm your email address:\n").lower()
	# If emails don't match or are empty, ask for them again
	if email != email2 or not email:
		print("Emails did not match or were empty. Please re-enter a valid email...")
		continue
	# Otherwise, add user to spreadsheet
	else:
		email_flag = False
		user = User(fn, ln, email)
		user.add_user()
		break
