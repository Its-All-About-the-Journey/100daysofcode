from datetime import *
import os
import pandas as pd
import random
import smtplib

MY_EMAIL = os.environ.get('EMAIL')
MY_EMAIL_PASS = os.environ.get('EMAIL_PASS')

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.


# Create a data frame from csv
df = pd.read_csv('birthdays.csv')

# Create a datetime object representing todays month and day
now = datetime.now()
todays_month = now.month
todays_day = now.day

# Construct filter for todays day and month and apply to the df
filter_date = (df['month'] == todays_month) & (df['day'] == todays_day)
filtered_df = df[filter_date]

# If there is a match, get the name(s) and email address(es) of the person(s)
if len(filtered_df) != 0:
	names = filtered_df['name'].values
	emails = filtered_df['email'].values
# If there are no matches, exit the application
else:
	print(f"No matching birthdays for {todays_month}/{todays_day}")
	exit()

# Create a dictionary of the names and corresponding emails
info = {name: email for name, email in zip(names, emails)}

# Loop through each of the name/email pairs, construct the letter and email the person
for target_name, target_email in info.items():

	# Pick random letter, open it and insert name
	random_letter = random.choice(['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt',
	                               'letter_templates/letter_3.txt'])
	with open(random_letter) as letter:
		formatted_letter = ''
		for line in letter.readlines():
			line = line.replace('[NAME]', target_name)
			formatted_letter += line

		# Email the letter to the recipient
		with smtplib.SMTP('smtp.gmail.com') as connection:  # Use smtp server of whatever mail provider you're using
			connection.starttls()  # Secures our connection and encrypts our emails, should they be intercepted
			connection.login(user=MY_EMAIL, password=MY_EMAIL_PASS)
			connection.sendmail(from_addr=MY_EMAIL,
			                    to_addrs=target_email,
			                    msg=f"Subject:Happy Birthday {target_name}!\n\n{formatted_letter}"
			                    )
