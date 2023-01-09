from tkinter import *
import pandas
from random import random, choice, sample
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# 4-2 에러 방지
try:
    data = pandas.read_csv("data/word_to_learn")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = pandas.DataFrame.to_dict(original_data, orient="records")
else:
    to_learn = pandas.to_dict(orient="records")

# 4-1 체크된 것 제거
def is_known():

    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/word_to_learn.csv", index=False)
    next_card()

# 3-1 카드 뒤집기 함수

def flip_card():

    # 영어로 변환
    global current_card, timer
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # UI 변환
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(bg_img, image=card_back_img)

# 2-2 다음 카드 넘어가는 함수

def next_card():

    global current_card, timer
    window.after_cancel(timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(bg_img, image=card_front_img)
    timer = window.after(3000, flip_card)

# 1. UI 설정

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 35, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)
next_card()

window.mainloop()

# 2. 체크 클릭 시 다음 카드로 변경 구현
# 3. 카드 뒤집기 구현
# 4. 내가 v 누른 것을 제외 한 단어 리스트 만들기