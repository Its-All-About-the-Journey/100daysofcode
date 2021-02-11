class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        self.check_answer(input(f"Q.{self.question_number}: {current_question.text} (True/False?): "), current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The answer was {correct_answer.lower()}. Your current score is {self.score}/{self.question_number}.\n\n")

    def still_has_questions(self):
        return len(self.questions_list) != self.question_number