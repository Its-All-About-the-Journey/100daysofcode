#!/user/bin/env python3
# 100 Days of Code
# Day 17: Classes
# Adam Pawlowski (@hypermanganate)

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Build Question Database List


def build_question_database(data):
    questions = []

    for question in question_data:
        questions.append(Question(question['text'], question['answer']))

    return questions


question_bank = build_question_database(question_data)
game_brain = QuizBrain(question_bank)
player_score = 0

game_proceeds = game_brain.next_question()

while game_proceeds:
    print(f"""\nQuestion #{game_brain.question_number}: """ +
          f"""{game_brain.current_question.text}""", end=' ')
    if game_brain.ask_true_false():
        print("That's right!")
        player_score += 1
    else:
        print("That's wrong!")
    print(f"""The correct answer was: {game_brain.current_question.answer}.""")
    print(f"""Your current score is {player_score}/""" +
          f"""{game_brain.question_number}""")
    game_proceeds = game_brain.next_question()

print(f"""Game over! Your score was: {player_score}/""" +
      f"""{game_brain.question_number}""")
