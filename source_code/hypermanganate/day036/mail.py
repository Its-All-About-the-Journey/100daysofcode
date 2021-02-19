# Send Email Functions

import smtplib
import json

email_account = json.load(open('./email.cfg', 'r'))


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
        msg=message.encode("utf8")
        )

    connection.close()
