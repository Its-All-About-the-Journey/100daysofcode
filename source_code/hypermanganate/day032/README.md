
# DAY 32

Email Dispatch

# Description

Send emails triggered by certain date values such as Birthdays or Garfield Days

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

Core

# How to run script

Enter birthday data into brithdays.csv following the format described.
Year isn't really important, as it's rude to inform someone past a certain age of their year probably.

Customize the birthday letter templates in letter_templates.
Currently, adding more isn't supported.

Run the script. 
If it's a Monday, receive motivational quotes.
If it's a birthday, email is dispatched.

*NOTE* The format of email.cfg is JSON:
{
    'Account': {
        'user': username,
        'pass': password,
        'smtp_host': smtp smart host,
        'smtp_port': smtp port,
        'address': email address
     }

}

*NOTE* App doesn't use username to auth but rather address whatever :dealwithit:

# Sample output

![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day032/app.png)