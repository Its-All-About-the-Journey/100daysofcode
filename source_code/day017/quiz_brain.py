class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list

  def current_question(self, answer):
    