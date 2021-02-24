# Send Email Functions

from flight_data import FlightData
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications
    # with the deal flight details.
    def __init__(self,
                 from_mail: str,
                 to_mail: str,
                 smart_host_address: str,
                 smart_host_port: str,
                 username: str,
                 password: str,
                 ) -> None:

        self.email_account = from_mail
        self.to_address = to_mail

        self.smart_host_address = smart_host_address
        self.smart_host_port = smart_host_port

        self.username = username
        self.password = password

    def send_mail(
        self,
        flight: FlightData
     ):

        self.connection = smtplib.SMTP(
            host=self.smart_host_address,
            port=self.smart_host_port
        )

        # Enable to debug SMTP transaction
        # connection.set_debuglevel(1)

        self.connection.starttls()

        self.connection.login(
            user=self.username,
            password=self.password
        )

        subject = "Flight Alert!"
        message_body = "A cheap flight deal has been found!\n" + \
            f"A flight from {flight.airport_from} to {flight.airport_to}" + \
            f" has been found for ${flight.price}!\n" + \
            f"Departs on {flight.departure_time}\n" + \
            f"Returrns on {flight.arrival_time}\n" + \
            f"A {flight.nights_in_destination} day trip!"

        message = f"From: {self.email_account}\n" + \
            f"To: {self.to_address}\n" + \
            f"Subject: {subject}\n\n" + \
            message_body

        self.connection.sendmail(
            from_addr=self.email_account,
            to_addrs=self.to_address,
            msg=message.encode("utf8")
            )

        self.connection.close()
