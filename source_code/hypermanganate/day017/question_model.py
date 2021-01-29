# 100 Days of Code
# Day 17: Classes
# Question Class
# Adam Pawlowski @hypermanganate

class Question:
    """
    Quiz Question
    """

    def __init__(self, question_text: str, question_answer: str) -> 'Question':
        """
        Quiz Question Text (string) (required)
        Quiz Question Answer (string) (required)
        """
        super().__init__()
        self.text = question_text
        self.answer = question_answer
