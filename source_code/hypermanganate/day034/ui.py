from quiz_brain import QuizBrain
import tkinter as tk
# from textwrap import wrap

THEME_COLOR = "#375362"


class GameWindow:

    def __init__(self, brain: QuizBrain) -> None:

        self.brain = brain

        self.app_window = tk.Tk()
        self.app_window.title("Quizzler")
        self.app_window["bg"] = THEME_COLOR
        self.app_window["padx"] = 20
        self.app_window["pady"] = 20

        self.question_canvas = tk.Canvas(
            background="white",
            highlightthickness=0,
            width="300",
            height="250"
            )

        self.question_text = \
            self.question_canvas.create_text(
                150,
                125,
                width=280,
                text="Question",
                font=("Arial", 16, "italic")
            )

        self.score_label = \
            tk.Label(
                background=THEME_COLOR,
                text="Score: 0",
                foreground="white"
                )

        self.true_image = tk.PhotoImage(file="./images/true.png")
        self.false_image = tk.PhotoImage(file="./images/false.png")

        self.true_button = tk.Button(
            image=self.true_image,
            highlightthickness=0,
            border=0,
            command=self.true_button_click
            )

        self.false_button = tk.Button(
            image=self.false_image,
            highlightthickness=0,
            border=0,
            command=self.false_button_click
            )

        self.score_label.grid(column=1, row=0)

        self.question_canvas.grid(
            column=0,
            row=1,
            columnspan=2,
            padx=25,
            pady=25
            )

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.is_thinking = False
        self.display_question()

    def display_question(self):
        question = self.brain.next_question()

        self.question_canvas.itemconfig(
            self.question_text,
            # text=f"Q{question_number}: " + '\n'.join(wrap(question_text, 16))
            text=question
            )

    def true_button_click(self):
        if not self.is_thinking:
            self.check_answer(self.brain.check_answer("true"))

    def false_button_click(self):
        if not self.is_thinking:
            self.check_answer(self.brain.check_answer("false"))

    def check_answer(self, results: bool):
        self.is_thinking = True
        if results:
            self.question_canvas.configure(background="Green")
        else:
            self.question_canvas.configure(background="Red")
        self.score_label.config(text=f"Score: {self.brain.score}")
        self.app_window.after(1000, self.reset_question_canvas)

    def reset_question_canvas(self):
        self.question_canvas.configure(background="white")
        if self.brain.still_has_questions():
            self.is_thinking = False
            self.display_question()
        else:
            self.question_canvas.itemconfig(
                self.question_text,
                text="Game Over"
            )
