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
        self.btn_true = Button(image=btn_true_img, command=self.check_answer_true)
        self.btn_false = Button(image=btn_false_img, command=self.check_answer_false)

        # Grid Layout
        self.lbl_score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.btn_true.grid(row=2, column=0)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def check_answer(self, answer) -> None:
        if self.quiz.check_answer(answer):
            self.update_window_state("green", DISABLED)
            self.update_score()

        else:
            self.update_window_state("red", DISABLED)

        self.window.after(1000, func=self.get_next_question)

    def check_answer_false(self) -> None:
        self.check_answer("false")

    def check_answer_true(self) -> None:
        self.check_answer("true")

    def get_next_question(self) -> None:
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.update_window_state("white")

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def update_score(self) -> None:
        self.lbl_score.config(text=f"Score: {self.quiz.score}")

    def update_window_state(self, color: str, state: str = NORMAL) -> None:
        self.canvas.config(bg=color)
        self.btn_true.config(state=state)
        self.btn_false.config(state=state)

