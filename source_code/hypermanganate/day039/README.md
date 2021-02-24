
# DAY 39

Flight Price Checker

# Description

Checks for a lower price flight than one you have in a Google sheet.
Emails you when one is found for one of the target cities.

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

requests 2
core

# How to run script
Complete the app.cfg 

Call the script.

```
{
    "app": {
        "api": {
            },
            "sheety": {
                "api_key": "YOUR_API_KEY",
                "endpoint": "https://api.sheety.co/YOUR_URLS/flightDeals/prices"
            },
            "kiwi": {
                "api_key": "YOUR_API_KEY",
                "endpoint": "https://tequila-api.kiwi.com"
            }
        },
        "mail": {
            "Yahoo": {
                "user": "username",
                "pass": "password",
                "smtp_host": "smtp.mail.yahoo.com",
                "smtp_port": "587",
                "address": "address@yahoo.com"
            },
            "Live": {
                "address": "address@live.com"
            }
        }
    }
}

```

# Sample output

![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day039/app.png)

