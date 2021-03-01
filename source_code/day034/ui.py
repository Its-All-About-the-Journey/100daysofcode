THEME_COLOR = "#375362"
PATH="source_code/day034/"
FONT_NAME = "Arial"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.true_image = PhotoImage(file=f"{PATH}images/true.png")
        self.false_image = PhotoImage(file=f"{PATH}images/false.png")
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg='white', bg=THEME_COLOR, font=(FONT_NAME, "12", "bold"))
        self.score_label.grid(column=1,row=0)

        #Build canvas (HIGHLIGHT THICKNESS = border for canvas)
        self.canvas = Canvas(width=300, height=250,bg='white',highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question text", fill="black", font=(FONT_NAME, "16", "italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.true_button = Button(self.window, image=self.true_image, command=self.true_pressed, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(self.window, image=self.false_image, command=self.false_pressed, highlightthickness=0, padx=40, pady=40)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.true_button.config(state='normal')
            self.false_button.config(state='normal')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')
        self.correct() if self.quiz.check_answer("True") else self.incorrect()
    
    def false_pressed(self):
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')
        self.correct() if self.quiz.check_answer("False") else self.incorrect()

    def correct(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg='green')
        self.window.after(2000, self.get_next_question)

    def incorrect(self):
        self.canvas.config(bg='red')
        self.window.after(2000, self.get_next_question)