from requests.models import HTTPError
from question_model import Question
from quiz_brain import QuizBrain
from requests import Session
from ui import GameWindow
from html import unescape
import json
import requests


TRIVIA_ENDPOINT = "https://opentdb.com/api.php?" + \
                  "amount=10&category=9&type=boolean"


def slurp_trivia() -> bool:

    session = Session()

    try:

        response = session.get(TRIVIA_ENDPOINT, timeout=3)

    except requests.ConnectionError:

        print(
            "Failed to connect to OpenTriviaDB"
        )
        return False

    try:

        response.raise_for_status()

    except HTTPError as error:

        print(
            "Failed to get trivia questions from " +
            "OpenTriviaDB API: "
        )
        print(error)
        exit()

    trivia_data = response.json()
    with open('./data.py', "w") as data_file:
        data_file.write("question_data = ")
        data_file.write(json.dumps(trivia_data['results'], indent=4))
        return True


def other_way_to_slurp_trivia():
    session = Session()

    try:

        response = session.get(TRIVIA_ENDPOINT, timeout=3)

    except requests.ConnectionError:

        print(
            "Failed to connect to OpenTriviaDB"
        )
        return False

    try:

        response.raise_for_status()

    except HTTPError as error:

        print(
            "Failed to get trivia questions from " +
            "OpenTriviaDB API: "
        )
        print(error)
        exit()

    trivia_data = response.json()['results']

    return trivia_data

# Main


slurp_trivia()

if 1:
    from data import question_data

# question_data = other_way_to_slurp_trivia()

# if not question_data:
#     exit()


question_bank = []
for question in question_data:
    question_text = unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

game_window = GameWindow(quiz)

game_window.app_window.mainloop()
