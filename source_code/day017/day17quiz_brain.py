class QuizBrain:
    
    def __init__(self, question_list):
        """takes a list of questions as input. questions are dicts with text and answer keys."""
        
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        
    def next_question(self):
        """will print the next question, collect a response, print the answer, then advance the question number"""
        
        # grab the next question
        question = self.question_list[self.question_number]
        
        # ask it and collect a response
        response = input(f"Q.{self.question_number + 1}: {question.text} (True/False): ")
        
        # score the response
        self.score_response(response, question.answer)
        
        # advance question number in prep for next question
        self.question_number += 1
        
        # done with this question
        print()
        
    def has_next(self):
        return self.question_number < len(self.question_list)
    
    def score_response(self, response, answer):
        if response.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Score: {self.score}/{self.question_number + 1}")