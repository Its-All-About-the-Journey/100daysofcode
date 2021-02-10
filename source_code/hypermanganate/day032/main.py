# 100 Days of Code: Python
# Day 32: SMTP Mail Sending
# Adam Pawlowski (@hypermanganate)

import datetime as dt
import smtplib
import json
import csv
from random import choice, randint

email_account = json.load(open('./email.cfg', 'r'))

TEST = False


def send_mail(
    message_body: str,
    to_address: str = email_account['Live']['address'],
    subject: str = "Motivational Quote"
     ):

    connection = smtplib.SMTP(
        email_account['Yahoo']['smtp_host'],
        port=email_account['Yahoo']['smtp_port']
        )

    # Enable to debug SMTP transaction
    # connection.set_debuglevel(1)

    connection.starttls()

    connection.login(
        user=email_account['Yahoo']['address'],
        password=email_account['Yahoo']['pass']
        )

    message = f"From: {email_account['Yahoo']['address']}\n" + \
              f"To: {to_address}\n" + \
              f"Subject: {subject}\n\n" + \
              message_body

    connection.sendmail(
        from_addr=email_account['Yahoo']['address'],
        to_addrs=to_address,
        msg=message
        )

    connection.close()

# m


quotes = open('./quotes.txt', 'r').readlines()

if TEST:
    mail_date = dt.datetime(year=2021, month=2, day=8)
else:
    mail_date = dt.datetime.now()

if not mail_date.weekday():
    quote = choice(quotes).strip()
    print("It's Monday")
    print(quote)
    send_mail(quote)
else:
    print("Today's not Monday, but, still stay motivated!")


# #################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

birthdays = open('./birthdays.csv', 'r')
birthdays_csv = csv.DictReader(birthdays)

for birthday in birthdays_csv:
    if dt.date.today().month == int(birthday['month']) and \
       dt.date.today().day == int(birthday['day']):

        print(f"Happy Birthday today to {birthday['name']} !")

        email_to_read = f"./letter_templates/letter_{randint(1,3)}.txt"
        print(f"Sending {email_to_read}")
        email_body = open(email_to_read, 'r').read().replace(
            '[NAME]', birthday['name']
            ).replace("Angela", "Adam")
        send_mail(message_body=email_body,
                  to_address=birthday['email'],
                  subject="Happy Birthday!"
                  )
