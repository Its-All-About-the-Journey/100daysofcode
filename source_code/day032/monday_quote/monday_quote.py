from datetime import *
import os
import random
import smtplib

my_email = os.environ.get('EMAIL')
my_email_pass = os.environ.get('EMAIL_PASS')

# Get the day today
today = datetime.now().weekday()

# If today is Monday, email a random quote to myself
if today == 0:
	os.environ.get
	# Open the text file and pull out a random quote
	with open('quotes.txt', 'r') as file:
		quotes = file.readlines()
	random_quote = random.choice(quotes)
	print(random_quote)

	with smtplib.SMTP('smtp.gmail.com') as connection:  # Use smtp server of whatever mail provider you're using
		connection.starttls()  # Secures our connection and encrypts our emails, should they be intercepted
		connection.login(user=my_email, password=my_email_pass)
		connection.sendmail(from_addr=my_email,
		                    to_addrs='test@email.com',
		                    msg=f"Subject:Quote of the Day!\n\n{random_quote}"
		                    )
