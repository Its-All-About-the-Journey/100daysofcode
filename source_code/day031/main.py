from tkinter import *
import random
from numpy import flip
import pandas

BACKGROUND_COLOR = "#B1DDC6"
PATH="source_code/day031/"
FONT_NAME = "Arial"

def load_words():
    try:
        return pandas.read_csv(f"{PATH}data/words_to_learn.csv").to_dict(orient="records")
    except FileNotFoundError:
        return pandas.read_csv(f"{PATH}data/french_words.csv").to_dict(orient="records")

WORD_LIST = load_words()

card_choice = {}
update_window = None

def remove_card():
    window.after_cancel(update_window)
    global WORD_LIST
    WORD_LIST.remove(card_choice)
    pandas.DataFrame.from_dict(WORD_LIST).to_csv(f"{PATH}data/words_to_learn.csv", index=False)
    next_word()

def next_word():
    global card_choice
    global update_window
    canvas.itemconfig(card_image, image=question_background)
    canvas.itemconfig(title_text, text="French", fill="black")
    card_choice = random.choice(WORD_LIST)
    canvas.itemconfig(word_text, text=card_choice["French"], fill="black")
    update_window = window.after(3000, flip_to_answer)

def flip_to_answer():
    canvas.itemconfig(card_image, image=answer_background)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card_choice["English"], fill="white")

window = Tk()
window.title("Flashcard Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

question_background = PhotoImage(file=f"{PATH}images/card_front.png")
answer_background = PhotoImage(file=f"{PATH}images/card_back.png")
right_image = PhotoImage(file=f"{PATH}images/right.png")
wrong_image = PhotoImage(file=f"{PATH}images/wrong.png")

#Build canvas with background iamge (HIGHLIGHT THICKNESS = border for canvas)
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_image = canvas.create_image(0, 0, image=question_background, anchor="nw")
title_text = canvas.create_text(400, 175, text="Title", fill="black", font=(FONT_NAME, "40", "italic"))
word_text = canvas.create_text(400, 300, text="Word", fill="black", font=(FONT_NAME, "60", "bold"))
canvas.grid(column=0,row=0,columnspan=2)

#Wrong Button
wrong_button = Button(window, image=wrong_image, command=next_word, highlightthickness=0)
wrong_button.grid(column=0, row=1)

#Right Button
right_button = Button(window, image=right_image, command=remove_card, highlightthickness=0)
right_button.grid(column=1, row=1)

while True:
    next_word()
    window.mainloop()
    