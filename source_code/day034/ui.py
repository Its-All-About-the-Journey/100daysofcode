from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

	# We pass the QuizBrain object we created in main.py into the initialization of our Quiz Interface -> used later
	# We also declare that the object we pass in must be of type QuizBrain (called Python Typing)
	def __init__(self, quiz_brain: QuizBrain):
		self.quiz = quiz_brain

		# Configure the initial window layout
		self.window = Tk()
		self.window.title('Quizzler')
		self.window.config(bg=THEME_COLOR, padx=20, pady=20)

		# Configure the score label
		self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, padx=20, font=("Arial", 10, "bold"))
		self.score_label.grid(row=0, column=1)

		# Configure canvas layout and text
		self.canvas = Canvas(width=300, height=250, bg='white')
		self.question_text = self.canvas.create_text(150, 125, width=280, text='',
		                                             font=("Arial", 20, "italic"), fill="black")
		self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

		# Configure buttons and their images
		self.true_img = PhotoImage(file='images/true.png')
		self.true_button = Button(image=self.true_img, highlightthickness=0, relief='flat',
		                          command=lambda: self.answer('True'))
		self.true_button.grid(row=2, column=0)
		self.false_img = PhotoImage(file='images/false.png')
		self.false_button = Button(image=self.false_img, highlightthickness=0, relief='flat',
		                           command=lambda: self.answer('False'))
		self.false_button.grid(row=2, column=1)

		# Call function to populate initial question
		self.get_next_question()

		self.window.mainloop()

	# Function retrieves the next question using the QuizBrain object next_question() method
	def get_next_question(self) -> None:
		# Turns canvas back to white from green/red, after player guess
		self.canvas.config(bg='white')
		# If there are questions remaining, get one and update canvas text
		if self.quiz.still_has_questions():
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.question_text, text=q_text)
		# Otherwise, if no questions remain, disable buttons and display final score
		else:
			self.true_button.config(state='disabled')
			self.false_button.config(state='disabled')
			self.canvas.itemconfig(self.question_text, text=f'Quiz Complete!\nFinal Score: '
			                                                f'{self.quiz.score}/{self.quiz.question_number}')

	# Called if user clicks True/False buttons -> pass in user answer, either 'True' or 'False'
	def answer(self, user_answer):
		# Get the outcome (Right/Wrong) based on the player answer - update the score
		outcome = self.quiz.check_answer(user_answer)
		self.score_label.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
		# If the user answered correctly, change the background to green
		if outcome:
			self.canvas.config(bg='green')
		# If wrong, change background of canvas to red
		else:
			self.canvas.config(bg='red')
		# After 0.75s delay, get and display the next question
		self.window.after(750, self.get_next_question)
