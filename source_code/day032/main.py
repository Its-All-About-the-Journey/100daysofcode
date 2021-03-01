##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv - DONE

# 2. Check if today matches a birthday in the birthdays.csv - DONE

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


from email import message
import smtplib
import datetime as dt
import random
import pandas

PATH = "source_code/day032/"
email = "emailviapython@gmail.com"
now = dt.datetime.now()
birthdays = pandas.read_csv(f"{PATH}birthdays.csv")

for index,row in birthdays.iterrows():
    if row.month == now.month and row.day == now.day:
        with open(file=f"{PATH}letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            letter_template = letter.read()
            new_letter = letter_template.replace("[NAME]", row["name"])
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email,password="2TestPassPythonEmail")

                connection.sendmail(
                    from_addr=email, 
                    to_addrs=row.email, 
                    msg=f"Subject:Happy Birthday!\n\n{new_letter}"
                    )
