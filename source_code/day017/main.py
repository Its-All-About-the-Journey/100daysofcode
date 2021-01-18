from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


if __name__ == "__main__":
    # Load questions
    question_bank  = [ Question(question["question"], question["correct_answer"]) for question in question_data]

    # Create a QuizBrain instance
    quiz_brain = QuizBrain(question_bank)

    while( quiz_brain.still_has_questions() ):
        quiz_brain.next_question()

    print("=" * 80)
    print("You've completed the quiz")
    print(f"Your final score was: {quiz_brain.score}/{quiz_brain.num_questions}")
    print("=" * 80)