# 100 Days of Code
# Day 17: Classes
# Question Class
# Adam Pawlowski @hypermanganate

# The video just has this go in order of questions for some reason, which I don't think is particularly fun.

import random


class QuizBrain:

    def __init__(self, questions_list) -> 'QuizBrain':
        super().__init__()

        self.questions_list = questions_list
        self.question_number = 0
        self.total_questions = len(self.questions_list)
        self.current_question = None

    def next_question(self):
        """
        Set the next question, but, return False if we've exhausted the stockpile.
        """

        if self.question_number == self.total_questions:
            # We're out of questions
            return False
        else:
            question = random.choice(self.questions_list)
            self.questions_list.remove(question)
            self.question_number += 1
            self.current_question = question
            return True

    def ask_true_false(self):
        """
        Ask if the question is true or false, and return bool T/F based on the outcome.
        """

        guess = None
        answer = self.current_question.answer

        while guess not in ['true', 'false', 't', 'f']:
            guess = input("(True/False)? ").lower()

        if guess == 't' or guess == 'true':
            guess = True
        else:
            guess = False

        if (answer.lower() == 'true' and guess) or \
           (answer.lower() == 'false' and not guess):
            return True

        return False
