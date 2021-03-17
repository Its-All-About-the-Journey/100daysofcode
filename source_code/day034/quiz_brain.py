import html

class QuizBrain:

    def __init__(self, q_bank: list):
        self.question_number = 0
        self.score = 0
        self.question_bank = q_bank
        self.current_question = None

    # Added a Python Type Hint that the return value should be a Boolean
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_bank)

    # Function gets next questions from list, removes HTML escape characters and returns it
    # Added a Python Type Hint that the return value should be a String
    def next_question(self) -> str:
        self.current_question = self.question_bank[self.question_number]
        self.question_number += 1
        unescaped_question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {unescaped_question_text}"

    # Function checks user answer and returns the results (Correct/Incorrect), the users score and question number
    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        # If the users answer matches the correct answer, add 1 to score and return True as outcome
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            outcome = True
        # Otherwise, do not add to score and return False as the outcome
        else:
            outcome = False

        # Return the outcome, user score and current question number
        return outcome
