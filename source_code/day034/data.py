import requests

NUM_QUESTIONS = 10

parameters = {
    'amount': NUM_QUESTIONS,
    'type': 'boolean'
}

response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()  # If connection to API endpoint fails, will return the response code as an exception
question_data = response.json()  # Get the response in json/dictionary format
question_data = question_data['results']  # Return the section of the dictionary we want
