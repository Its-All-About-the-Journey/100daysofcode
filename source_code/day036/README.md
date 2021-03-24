
# DAY 36

# Description
Stock Price News Alert Project

# Environment
OS: Windows 10

Python version: 3.8

# Dependencies
twilio.rest module

# How to run script
```
This script can be run manually by entering your own alphavantage, newsapi and Twilio SSID's and API keys (must sign up for accounts).
Enter the stock ticker you wish to monitor into the STOCK variable

I've used enviroment variables to store all important credentials. You can store these crendentials however you see fit.
```

# Sample output
Message would arrive via SMS
```
TSLA: 🔺4.82%

Headline 1: Tesla now accepts Bitcoin in the US
Brief: As it promised earlier this year, Tesla now accepts payment in Bitcoin, according to Tesla's website and a tweet from CEO Elon Musk.
Article Link: https://www.engadget.com/tesla-will-soon-let-you-buy-one-of-its-e-vs-with-bitcoin-082916783.html

Headline 2: Elon Musk declares you can now buy a Tesla with Bitcoin in the U.S.
Brief: Tesla made headlines earlier this year when it took out significant holdings in bitcoin, acquiring a roughly $1.5 billion stake at then-prices in early February. At the time, it also noted in an SEC filing disclosing the transaction that it could also eventua…
Article Link: http://techcrunch.com/2021/03/24/elon-musk-declares-you-can-now-buy-a-tesla-with-bitcoin-in-the-u-s/

Headline 3: Tesla stans dunk on Porsche Taycan’s slow software update
Brief: The first electric Porsche Taycans are due for a software update, but it won't be quick. 
Drivers won't be able to push a button on the in-car screen, connect to WiFi, and update the car while in their own garage. Instead, the $100,000+ electric vehicle needs…
Article Link: https://mashable.com/article/porsche-taycan-software-update/
```

