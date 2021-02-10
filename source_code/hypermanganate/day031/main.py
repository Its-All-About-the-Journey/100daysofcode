# 100 Days of Code: Day 31
# Flash Card Tool
# Adam Pawlowski (@hypermanganate)

import tkinter as tk
from textwrap import wrap
from tkinter import messagebox
from random import choice
from os import path

BACKGROUND_COLOR = "#B1DDC6"

if path.exists('./data/words_to_learn.csv'):
    CARD_FILE = './data/words_to_learn.csv'
    if len(open('./data/words_to_learn.csv', "r").readlines()) == 1:
        CARD_FILE = "./data/uc_acronyms.csv"
else:
    CARD_FILE = "./data/uc_acronyms.csv"


def wrong():
    global this_card
    this_card = get_next_card()
    next_card(this_card)


def right():
    global this_card
    card_data.remove(this_card['raw'])
    this_card = get_next_card()
    next_card(this_card)
    with open("./data/words_to_learn.csv", "w") as file:
        file.write(','.join(topics) + "\n")
        for card in card_data:
            file.write(card)


def next_card(card: dict):
    global card_flip_timer

    if card_flip_timer:
        app_window.after_cancel(card_flip_timer)

    flash_card.itemconfig(flash_card_background_id, image=flash_card_back)
    flash_card.itemconfig(
        card_title_text_id,
        text=card['front']['topic']
        )
    flash_card.itemconfig(
        card_word_text_id,
        text='\n'.join(wrap(card['front']['entry'], 13))
        )
    card_flip_timer = app_window.after(
        3000,
        flip_card,
        card
        )


def flip_card(card: dict):
    flash_card.itemconfig(flash_card_background_id, image=flash_card_front)
    flash_card.itemconfig(card_title_text_id, text=card['back']['topic'])
    flash_card.itemconfig(
        card_word_text_id,
        text='\n'.join(wrap(card['back']['entry'], 13))
        )


def get_next_card():
    try:
        next_card_data = choice(card_data)
        return {
            'front': {
                'topic': topics[0],
                'entry': next_card_data.strip().split(',')[0]
            },
            'back': {
                'topic': topics[1],
                'entry': next_card_data.strip().split(',')[1]
            },
            'raw': next_card_data
        }
    except IndexError:
        if messagebox.showerror(
            title="No More Words",
            message="You've learned everything! Game over."
             ) == "ok":
            exit()

# Main


card_data = open(CARD_FILE, "r").readlines()
card_flip_timer = None

topics = card_data.pop(0).strip().split(',')
print(
    f"Loaded {len(card_data)} flash cards " +
    f"on the topics {topics[0]} and {topics[1]}."
    )

app_window = tk.Tk()
app_window.title("The Flasher")
app_window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

flash_card_front = tk.PhotoImage(file='./images/card_front.png')
flash_card_back = tk.PhotoImage(file='./images/card_back.png')

flash_card = tk.Canvas(
    background=BACKGROUND_COLOR,
    highlightthickness=0,
    width="800",
    height="526"
    )
flash_card_background_id = flash_card.create_image(
                                        400,
                                        263,
                                        image=flash_card_front
                                        )

card_title_text_id = flash_card.create_text(
                                    400,
                                    100,
                                    text="Title",
                                    font=("Ariel", 40, "italic")
                                    )
card_word_text_id = flash_card.create_text(
                                    400,
                                    263,
                                    text="Word",
                                    font=("Ariel", 60, "bold")
                                    )

right_button_image = tk.PhotoImage(file='./images/right.png')
wrong_button_image = tk.PhotoImage(file='./images/wrong.png')
right_button = tk.Button(
    image=right_button_image,
    highlightthickness=0,
    border=0,
    command=right
    )
wrong_button = tk.Button(
    image=wrong_button_image,
    highlightthickness=0,
    border=0,
    command=wrong
    )

flash_card.grid(row=0, column=0, columnspan=2)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

this_card = get_next_card()
next_card(this_card)

app_window.mainloop()
