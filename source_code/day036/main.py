import os
from twilio.rest import Client
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

# Alphavantage api key and endpoints
ALPHA_API_KEY = os.environ.get('ALPHA_API_KEY')
ALPHA_ENDPOINT = 'https://www.alphavantage.co/query'

# newsapi key and endpoint
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

# Account SSID and token for Twilio
TWILIO_SSID = os.environ.get('TWILIO_ACCOUNT_SSID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# My private phone number I used to sign up for Twilio
MY_NUM = os.environ.get('MY_PHONE_NUMBER')

# Set parameters for call to Alpha Stocks API
alpha_parameters = {
	'function': 'TIME_SERIES_DAILY',
	'symbol': STOCK,
	'outputsize': 'compact',
	'datatype': 'json',
	'apikey': ALPHA_API_KEY
}

# Make call to API and get relevant portion of the returned data
alpha_response = requests.get(url=ALPHA_ENDPOINT, params=alpha_parameters)
alpha_response.raise_for_status()
daily_stock_prices = alpha_response.json()["Time Series (Daily)"] # see sample_daily_stock_prices.json for format

# Get most recent two date keys from resulting data (have to take into account weekends and same day
# before 4:00pm EST are excluded from data)
date_keys = [day for day in daily_stock_prices][0:2]
print("Last 2 Date Keys: ", date_keys)

# Use the date keys from the 2 most recent days get the closing values
closing_price_1 = float(daily_stock_prices[date_keys[0]]["4. close"])
print("Closing Price 1: ", closing_price_1)
closing_price_2 = float(daily_stock_prices[date_keys[1]]["4. close"])
print("Closing Price 2: ", closing_price_2)

# Calculate the percent difference and check if it's >= 5%
# If gain or loss > 5%, get the first 3 news pieces for the COMPANY_NAME.
percent_difference = round(((closing_price_2 - closing_price_1)/closing_price_2) * 100, 2)
print("Percent Difference:  ", percent_difference)
if abs(percent_difference) >= 5:

	# Set parameters for call to news API
	news_parameters = {
		'apiKey': NEWS_API_KEY,
		'qInTitle': COMPANY_NAME,
		'from': date_keys[1],
		'sortBy': 'popularity',
		'pageSize': '3'
	}

	# Make call to news API and get relevant section of response
	news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
	news_response.raise_for_status()
	top_3_articles = news_response.json()['articles']

	# Compose message containing % change, news headlines + brief descriptions
	up_or_down = f'🔺{percent_difference}%' if percent_difference > 0 else f'🔻{percent_difference}%'
	sms_message = f'{STOCK}: {up_or_down}\n'
	for index, article in enumerate(top_3_articles):
		headline = article['title']
		brief = article['description']
		url = article['url']
		sms_message += f'\nHeadline {index + 1}: {headline}\nBrief: {brief}\nArticle Link: {url}\n'

	# Use twilio API to send composed message as an SMS text to my phone
	client = Client(TWILIO_SSID, TWILIO_AUTH_TOKEN)
	message = client.messages.create(
		body=sms_message,
		from_='+12623203179',
		to=MY_NUM
	)

# If the change wasn't >= 5% print to console
else:
	print("Didn't get News because change not >= 5%")
