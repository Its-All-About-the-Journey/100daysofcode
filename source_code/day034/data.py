from tkinter.constants import NUMERIC
import requests

number_of_questions = 10
difficulty = 'medium'
type = 'boolean'
category = 18

parameters = {
    'amount' : number_of_questions,
    'difficulty' : difficulty,
    'type' : type,
    'category' : category
}

response = requests.get(url=f"https://opentdb.com/api.php", params=parameters)

response.raise_for_status
question_data = response.json()['results']