from datetime import *
import os
import smtplib


# smtplib module
my_email = os.environ.get('EMAIL')
password = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com') as connection:  # Use smtp server of whatever mail provider you're using
	connection.starttls()  # Secures our connection and encrypts our emails, should they be intercepted
	connection.login(user=my_email, password=password)
	connection.sendmail(from_addr=my_email,
	                    to_addrs=my_email,
	                    msg="Subject: Hello\n\nThis is the body of my message"
	                    )


# Datetime Module
now = datetime.now()
year = now.year
print(year)
month = now.month  # Gives month as integer starting from 1 == January
print(month)
day_of_week = now.weekday()  # Gives day as integer starting from 0 == Monday
print(day_of_week)

date_of_birth = datetime(year=1989, month=11, day=22, hour=4)  # Requires year, month and day but time values are optional
print(date_of_birth)