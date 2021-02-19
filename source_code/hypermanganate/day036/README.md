# DAY 36

Stock News Alert

# Description

Application will obtain market closing prices for a given ticker symbol.
If there's enough of a change, the application will search for news that correlates.
An alert is dispatched via email if the change is above the delta percentage configured.

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

# How to run script
Setup app.cfg.

Presently, application looks at first stock.
Get API gets from alphavantage.co and newsapi.org and add them in .

```
{
    "stocks": [
        {
                "symbol": "AAPL",
                "company_name": "Apple, Inc."
        }
    ],
    "app": {
        "stock_delta": "0.05",
        "api_keys": {
            "alphavantage.co": "YOUR_API_KEY",
            "newsapi.org": "YOUR_OTHER_API_KEY"
        }
    }
}
```
email.cfg is a similar JSON file.
Account names are examples for services used.

Yahoo requires authentication with address, and not username.
```
{
    "Yahoo": {
        "user": "username",
        "pass": "password",
        "smtp_host": "smtp.mail.yahoo.com",
        "smtp_port": "587",
        "address": "address@yahoo.com"
    },
    "Live": {
        "user": "username",
        "pass": "password",
        "smtp_host": "server",
        "smtp_port": "port",
        "address": "address@live.com"
    }
}
```


# Sample output
![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day034/app.png)

```
Checking stock price of AAPL (Apple, Inc.) between close 2021-02-17 and close 2021-02-18
Yesterday's close was 130.84.
Today's close was 129.71.
This is a -0.8711741577364762% change.
That's not enough movement to be interested in.
```

In the above I had it send the email anyway.
