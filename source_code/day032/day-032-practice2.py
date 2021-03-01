from email import message
import smtplib
import datetime as dt
import random

email = "emailviapython@gmail.com"
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open(file="source_code/day032/quotes.txt") as file:
        quote_list = file.readlines()
        chosen_quote = random.choice(quote_list)
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email,password="2TestPassPythonEmail")

        connection.sendmail(
            from_addr=email, 
            to_addrs="tekkn0beatz@gmail.com", 
            msg=f"Subject:{now.strftime('%A')} Inspiration\n\n{chosen_quote}"
            )