import smtplib
import getpass

print("Lets send a hello email from your outlook email.")
email = input("Enter your outlook email: ")
password = getpass.getpass("Enter password: ")
recipient = input("To: ")

smtp_outlook = "smtp.office365.com"
smtp_gmail = "smtp.gmail.com"
smtp_yahoo = "smtp.mail.yahoo.com"

with smtplib.SMTP(smtp_outlook) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email, 
        msg="Subject:Hello\n\nHello World"
    )
