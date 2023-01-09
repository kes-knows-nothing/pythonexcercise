from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I Am a Label")

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button


def button_clicked():
    my_label.config(text=input.get())
    print("I got clicked")

button = Button(text="Click Me", command=button_clicked)

#Entry

input = Entry(width=10)

#New Button

















window.mainloop()