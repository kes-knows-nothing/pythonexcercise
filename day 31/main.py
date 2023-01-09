from tkinter import *
import pandas
from random import random, choice, sample
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#-------------------------------------------------------------------------#

def is_known():

    to_learn.remove(current_card)
    pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()

#-------------------------------------------------------------------------#


def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(bg_img, image=card_back_img)

#-------------------------------------------------------------------------#
def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(bg_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

#-------------------------------------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 35, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)

circle_image = PhotoImage(file="images/right.png")
known_button = Button(image=circle_image, command=is_known)
known_button.grid(row=1, column=1)


next_card()


window.mainloop()