from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

question_bank = [Question(d['question'], d['correct_answer']) for d in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()
else:
	print("\nYou've completed the quiz.")
	print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")