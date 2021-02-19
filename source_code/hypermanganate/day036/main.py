# 100 Days of Code: Python
# Day 36: Stock News Alert
# Adam Pawlowski (@hypermanganate)

from requests import Session
from requests.exceptions import HTTPError
from mail import send_mail
import json
import datetime

APP_CONFIG = json.load(open("./app.cfg", "r"))

STOCK = APP_CONFIG['stocks'][0]["symbol"]
COMPANY_NAME = APP_CONFIG['stocks'][0]["company_name"]
STOCK_DELTA = APP_CONFIG['app']['stock_delta']

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TODAY = datetime.datetime.today().strftime("%Y-%m-%d")
YESTERDAY = (datetime.datetime.today() -
             datetime.timedelta(days=1)).strftime("%Y-%m-%d")

print(
    f"Checking stock price of {STOCK} ({COMPANY_NAME}) between " +
    f"close {YESTERDAY} and close {TODAY}"
)

api_session = Session()

# STEP 1: Use STOCK ENDPOINT
# When STOCK price increase/decreases by 5% between yesterday and the
# day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday.
# Find the positive difference between the two prices. \
# e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": APP_CONFIG["app"]["api_keys"]["alphavantage.co"]
}

stock_details = api_session.get(STOCK_ENDPOINT, params=params)

try:

    stock_details.raise_for_status()

except HTTPError as error:

    print(
        "Error while retrieving stock details:\n" +
        error.response
    )

else:

    close_yesterday = float(
        stock_details.json()['Time Series (Daily)'][YESTERDAY]['4. close']
        )

    close_today = float(
        stock_details.json()['Time Series (Daily)'][TODAY]['4. close']
        )

    change = (100 - (close_yesterday * 100 / close_today))

    print(f"Yesterday's close was {close_yesterday}.")
    print(f"Today's close was {close_today}.")
    print(f"This is a {change}% change.")
    if abs(change) >= 5.0:
        print("This is an interesting amount!")
        get_stock_news = True
    else:
        print("That's not enough movement to be interested in.")
        get_stock_news = False

# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the
# first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator

if not get_stock_news:
    exit()

params = {
    # "q": COMPANY_NAME,  # This actually produced poor content
    "q": STOCK,
    "from": YESTERDAY,
    "to": TODAY,
    "sortBy": "popularity",
    "pageSize": 3,
    "apiKey": APP_CONFIG["app"]["api_keys"]["newsapi.org"]
}

# if get_stock_news:

news_articles = api_session.get(NEWS_ENDPOINT, params=params)

try:

    news_articles.raise_for_status()

except HTTPError as error:

    print(
        "Failed to fetch news:\n" +
        error.response
    )

else:

    if news_articles.json()['status'] != "ok":
        print("News Service Error")
        exit()

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and
#  description to your phone number.
# HINT 1: Consider using a List Comprehension.

# Optional: Format the SMS message like this:

if change < 0:
    subject = f"{STOCK}: 🔻{round(abs(change))}"
else:
    subject = f"{STOCK}: 🔺{round(abs(change))}"

body = ""
for article in news_articles.json()['articles']:
    body += f"{article['source']['name']}: {article['title']}\n" + \
        article['content'] + "\n" + article['url'] + "\n"

send_mail(message_body=body, subject=subject)

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings
....
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds
and prominent investors are required to file by the SEC The 13F filings
....
"""
