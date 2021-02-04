from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.lbl_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)

        # Button Images
        btn_true_img = PhotoImage(file="./images/true.png")
        btn_false_img= PhotoImage(file="./images/false.png")

        # Buttons
        self.btn_true = Button(image=btn_true_img)
        self.btn_false = Button(image=btn_false_img)

        # Grid Layout
        self.lbl_score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.btn_true.grid(row=2, column=0)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)


if __name__ == "__main__":
    quiz_ui = QuizInterface()
