from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# --------------------------- Functions ------------------------------
# Displays random word on flash card canvas after every button press
def display_random_word():
	global current_card, timer
	# If button is pressed multiple times, cancel the previous timer before proceeding
	window.after_cancel(timer)
	current_card = random.choice(word_dict)
	french_word = current_card['French']
	canvas.itemconfig(canvas_image, image=front)
	canvas.itemconfig(card_title, text='French', fill='black')
	canvas.itemconfig(card_word, text=french_word, fill='black')
	timer = window.after(3000, flip_card)

# Flips flash card to back and displays english translation
def flip_card():
	global current_card
	english_word = current_card['English']
	canvas.itemconfig(canvas_image, image=back)
	canvas.itemconfig(card_title, text='English', fill='white')
	canvas.itemconfig(card_word, text=english_word, fill='white')

# If user presses green check, function removes the word from the 'words_to_learn,csv' file
def remove_word():
	global current_card
	word_dict.remove(current_card)
	new_data = pandas.DataFrame(word_dict)
	new_data.to_csv('data/words_to_learn.csv', index=False)


# ------------------------ Data Retrieval ----------------------------
# If program is being run for the first time, use the french_words.csv for the base data
# Otherwise, use words_to_learn.csv
if os.path.exists('data/words_to_learn.csv'):
	data = pandas.read_csv('data/words_to_learn.csv')
else:
	data = pandas.read_csv('data/french_words.csv')
	data.to_csv('data/words_to_learn.csv', index=False)
# Convert data to dictionary to be used in app
word_dict = data.to_dict(orient='records')

# ------------------------------ UI ----------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file='images/card_front.png')
back = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front)
card_title = canvas.create_text(400, 150, text="", fill='black', font=('Arial', 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill='black', font=('Arial', 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, relief='flat',
                      command=display_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
# Use lambda to call multiple functions on each button press
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, relief='flat',
                      command=lambda: [display_random_word(), remove_word()])
right_button.grid(row=1, column=1)

# Initiate the flip timer for the first card
timer = window.after(3000, flip_card)
# Initial call of function to populate card
display_random_word()

window.mainloop()
