from day17data import question_data
from day17question_model import Question
from day17quiz_brain import QuizBrain

quiz_brain = QuizBrain([Question(**question) for question in question_data])


while quiz_brain.has_next():
    quiz_brain.next_question()
    
print("You completed the quiz!")
print(f"Your final score is {quiz_brain.score} out of {len(quiz_brain.question_list)}.")


