import pandas
from random import choice

from tkinter import *
from tkinter import messagebox

AFTER_CALLBACK_MSEC = 3000

BACKGROUND_COLOR = "#B1DDC6"

CSV_FILE = "./data/french_words.csv"

FONT_LANGUAGE_LABEL_ATTRIBUTES = ("Arial", 40, "italic")
FONT_WORD_LABEL_ATTRIBUTES = ("Arial", 60, "bold")

IMAGE_BTN_CORRECT_FILE = "./images/right.png"
IMAGE_BTN_WRONG_FILE = "./images/wrong.png"
IMAGE_BTN_HEIGHT = 100
IMAGE_BTN_WIDTH = 100

IMAGE_CARD_BACK_FILE = "./images/card_back.png"
IMAGE_CARD_FRONT_FILE = "./images/card_front.png"
IMAGE_CARD_HEIGHT = 526
IMAGE_CARD_WIDTH = 800

LBL_BACK_LANGUAGE = "English"
LBL_FRONT_LANGUAGE = "French"
LBL_BG_COLOR ="#ffffff"

WINDOW_IMAGE_PADDING = 50
WINDOW_TITLE = "French to English"

# global variable
after_callback = None
flash_card = None
flash_cards = None
flash_correct_cards = list()
flash_wrong_cards = list()


def answered_correct() -> None:
    flash_card["LastGuessCorrect"] = True
    flash_correct_cards.append(flash_card)
    show_next_flash_card()


def answered_wrong() -> None:
    flash_card["LastGuessCorrect"] = False
    flash_wrong_cards.append(flash_card)
    show_next_flash_card()


def button_state(normal: bool) -> None:
    state = NORMAL if normal else DISABLED
    btn_correct.config(state=state)
    btn_wrong.config(state=state)    


def cancel_after_callback() -> None:
    if after_callback:
        window.after(after_callback)


def csv_dump(filename: str) -> None:
    # Combine the flash_cards, flash_correct_cards, flash_wrong_cards, flash_card
    # then write to file
    cards = list()

    for obj in [flash_cards, flash_wrong_cards, flash_correct_cards]:
        if len(obj):
            cards.extend(obj)
    
    if len(flash_card):
        cards.append(flash_card)
    
    csv_data = pandas.DataFrame(cards)
    csv_data.to_csv(CSV_FILE, index=False)
    

def csv_load(filename: str) -> dict:
    global flash_cards

    pandas_in = pandas.read_csv(filename)
    flash_cards = pandas_in.to_dict(orient="records")

    # If data has history, separate cards into new, wrong, correct list
    if "LastGuessCorrect" in pandas_in.columns:
        new_cards = list()

        for card in flash_cards:
            if card["LastGuessCorrect"] == True:
                flash_correct_cards.append(card)

            elif card["LastGuessCorrect"] == False:
                flash_wrong_cards.append(card)

            else:
                new_cards.append(card)
        
        flash_cards = new_cards


def show_answer() -> None:
    global canvas_image

    canvas.itemconfig(canvas_image, image=canvas_back_image)
    canvas.itemconfig(lbl_language, text=LBL_BACK_LANGUAGE, fill="white")
    canvas.itemconfig(lbl_word, text=flash_card["English"], fill="white")
    button_state(True)    
    

def show_next_flash_card() -> None:
    global canvas_image, flash_card, flash_cards, flash_correct_cards, flash_wrong_cards

    # If we run out
    # - flash_cards points to flash_wrong_cards
    # - flash_wrong_cards points to empty list
    if (not len(flash_cards)) and len(flash_wrong_cards):
        flash_cards = flash_wrong_cards
        flash_wrong_cards = list()
    
    elif not len(flash_cards):
        # All cards are correct, pop message, start over
        if messagebox.askokcancel("You have completed all cards.", "Click 'ok' to start over or 'cancel' to quit"):
            flash_cards = flash_correct_cards
            flash_correct_cards = list()
        
        else:
            exit()

    flash_card = choice(flash_cards)  
    flash_cards.remove(flash_card)

    canvas.itemconfig(canvas_image, image=canvas_front_image)
    canvas.itemconfig(lbl_language, text=LBL_FRONT_LANGUAGE, fill="black")
    canvas.itemconfig(lbl_word, text=flash_card["French"], fill="black")
    button_state(False)

    window.after(AFTER_CALLBACK_MSEC, show_answer)


if __name__ == "__main__":

    # Setup Window
    window = Tk()
    window.title(WINDOW_TITLE)
    window.config(bg=BACKGROUND_COLOR, padx=WINDOW_IMAGE_PADDING, pady=WINDOW_IMAGE_PADDING)

    # Setup images
    btn_correct_image = PhotoImage(file=IMAGE_BTN_CORRECT_FILE)
    btn_wrong_image = PhotoImage(file=IMAGE_BTN_WRONG_FILE)
    canvas_front_image = PhotoImage(file=IMAGE_CARD_FRONT_FILE)
    canvas_back_image = PhotoImage(file=IMAGE_CARD_BACK_FILE)

    # Setup Canvas
    canvas = Canvas(bg=BACKGROUND_COLOR, width=IMAGE_CARD_WIDTH, height=IMAGE_CARD_HEIGHT, highlightthickness=0)
    canvas_image = canvas.create_image(IMAGE_CARD_WIDTH/2, IMAGE_CARD_HEIGHT/2, image=canvas_front_image)
    lbl_language = canvas.create_text(400, 150, text="Language", font=FONT_LANGUAGE_LABEL_ATTRIBUTES)
    lbl_word = canvas.create_text(400, 263, text="word", font=FONT_WORD_LABEL_ATTRIBUTES)

    # Setup buttons - wrong and correct
    btn_correct = Button(command=answered_correct, image=btn_correct_image, highlightthickness=0)
    btn_wrong = Button(command=answered_wrong, image=btn_wrong_image, highlightthickness=0)
    
    # Setup 2X3 grid
    canvas.grid(row=0, column=0, columnspan=2)
    btn_wrong.grid(row=1, column=0)
    btn_correct.grid(row=1, column=1)

    # Load flash cards from csv file
    csv_load(CSV_FILE)

    # Display first flash card
    show_next_flash_card()

    # Keep window up until user closes it
    window.mainloop()

    # Cancel any after callback
    cancel_after_callback()

    # Dump card progress
    csv_dump(CSV_FILE)