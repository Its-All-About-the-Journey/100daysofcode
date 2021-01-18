from copy import deepcopy
from html import unescape

class QuizBrain:

    def __init__(self, question_list: list) -> None:
        self.question_index = 0
        self.question_list  = deepcopy(question_list)
        self.num_questions = len(question_list)
        self.score = 0
    
    def check_answer(self, user_answer, correct_answer) -> bool:
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("   That's wrong.\n")
        
        print(f"   The correct answer is: {correct_answer}.")
        print(f"   Your current score is: {self.score}/{self.question_index}\n")

    def next_question(self) -> None:
        question = self.question_list[self.question_index]
        self.question_index += 1

        try:
            user_answer = input(f"Q-{self.question_index}: {unescape(question.text)} (True/False): ")
        except:
            user_answer = None
        
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self) -> bool:
        return self.num_questions > self.question_index