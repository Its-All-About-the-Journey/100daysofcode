
# DAY 40

Flight Price Club

# Description

Checks for a lower price flight than one you have in a Google sheet.
Emails club members based on mail addresses in a Google sheet.

*This is an incomplete project*

I could not tolerate this any more, and nearly finished it when the final step was
just add a Google Flight URL which ... isn't even related to the flight data we bothered processing.
Big thumbs down on the unnecessary complexity to prove we know how to use an API.

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
                "flight_endpoint": "https://api.sheety.co/YOUR_URLS/flightDeals/prices",
                "users_endpoint": "https://api.sheet.co/YOUR_URLS/flightDeals/users"
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

![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day040/app.png)

