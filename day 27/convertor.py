from tkinter import *

def button_clicked():
    f2 = float(f1.get())
    k = f2 * 1.609
    km_output.config(text=f"{k}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

f1 = Entry(width=10)
f1.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_label = Label(text="is equal to")
is_label.grid(column=0, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)



window.mainloop()