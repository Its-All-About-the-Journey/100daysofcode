class QuizBrain:
	def __init__(self, question_list):
		self.question_number = 0
		self.question_list = question_list
		self.score = 0

	def still_has_questions(self):
		return self.question_number < len(self.question_list)

	def next_question(self):
		answer = input(f'\nQ.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ')
		correct = self.question_list[self.question_number].answer
		self.check_answer(answer, correct)
		self.question_number += 1

	def check_answer(self, answer, correct):
		if answer.lower() == correct.lower():
			self.score += 1
			print("You got it right!")
			print(f"The correct answer was: {correct}")
			print(f"Your current score is {self.score}/{self.question_number + 1}")
		else:
			print("WRONG ANSWER MO FO!")
			print(f"The correct answer was: {correct}")
			print(f"Your current score is {self.score}/{self.question_number + 1}")
