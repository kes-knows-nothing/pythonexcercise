from tkinter import *
from turtle import Screen, Turtle
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def button_reset():
    window.after_cancel(timer)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="", bg=YELLOW, fg=GREEN)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        canvas.itemconfig(timer_text, text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.itemconfig(timer_text, text="Break", fg=PINK)
    else:
        count_down(work_sec)
        canvas.itemconfig(timer_text, text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        if reps % 2 == 0:
            mark += "✓"
            check_mark.config(text=mark, bg=YELLOW, fg=GREEN)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30,'bold'))
timer.grid(column=1, row=0)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(113, 112, image=tomato_img)
timer_text = canvas.create_text(113, 132, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

b_start = Button(text="Start", command=start_timer)
b_start.grid(column=0, row=2)

b_reset = Button(text="Reset", command=button_reset)
b_reset.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()