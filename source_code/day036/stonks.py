import twilio
import os
import datetime
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
alpha_api_key = os.environ['ALPHAVANTAGE_API_KEY']
newsapi_api_key = os.environ['NEWSAPI_KEY']


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_stocks():

    alphavantage_url = 'https://www.alphavantage.co/query'

    alphavantage_parameters = {
        'function' : 'TIME_SERIES_DAILY',
        'symbol' : STOCK,
        'outputsize' : 'compact',
        'apikey' : alpha_api_key
    }

    stock_info = requests.get(url=alphavantage_url, params=alphavantage_parameters)
    yesterday = list(stock_info.json()['Time Series (Daily)'].keys())[1]
    day_before = list(stock_info.json()['Time Series (Daily)'].keys())[2]

    close_yesterday = float(stock_info.json()['Time Series (Daily)'][yesterday]['4. close'])
    close_day_before = float(stock_info.json()['Time Series (Daily)'][day_before]['4. close'])
    change = ((close_yesterday - close_day_before) / close_day_before) * 100.0
    
    if abs(change) > 5:
        get_news(change)
        

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news(change):
    newsapi_url = 'https://newsapi.org/v2/everything'

    newsapi_parameters = {
        'qInTitle' : COMPANY_NAME,
        'pageSize' : 3,
        'sortBy' : 'publishedAt',
        'apiKey' : newsapi_api_key
    }

    news = requests.get(url=newsapi_url, params=newsapi_parameters)
    text_news(change,news)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def text_news(change,news):
    
    for article in news.json()['articles']:
        headline = article['title']
        description = article['description']
        client = Client(twilio_account_sid, twilio_auth_token)
        up_or_down = '🔺' if change > 0 else '🔻'
        message = f"{STOCK}: {up_or_down}{round(change,3)}\nHeadline: {headline}\nBrief: {description}"

        message = client.messages \
                        .create(
                            body=message,
                            from_='+19522434466',
                            to='+19522398656'
                        )
        print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

check_stocks()