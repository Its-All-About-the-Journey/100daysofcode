from email import message
import smtplib
import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2021:
    print("Wear a mask")
print(type(now))

date_of_birth = dt.datetime(year=1986,month=5,day=7)
print(date_of_birth)



'''
email = "emailviapython@gmail.com"
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email,password="2TestPassPythonEmail")


    connection.sendmail(
        from_addr=email, 
        to_addrs="tekkn0beatz@gmail.com", 
        msg="Subject:Hello\n\nThis is the body of my email."
        )
'''