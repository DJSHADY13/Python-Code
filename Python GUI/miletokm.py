from tkinter import *

from graphql import is_equal_type

window = Tk()
window.title("MY first gui program")
window.config(padx=20, pady=20)
# my_label = tkinter.Label(text="I am a label", font=("Arial",30))
# my_label.grid(column=0, row=0)

# my_label["text"] = "New text"

# def button_clicked():
#     my_label.config(text="I was clicked")

# button = tkinter.Button(text="click me", command=button_clicked)
# button.grid(column=1, row=1)

# new_button = tkinter.Button(text="New Button")
# new_button.grid(column=2, row=0)

# input = tkinter.Entry(width=10)
# input.grid(column=3,row=4)
# print(input.get())

def cal_km():
    miles = int(inputt.get())
    kilometers = int(miles * 1.6)
    my_label.config(text=kilometers)

inputt = Entry(width=7)
inputt.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

my_label = Label(text="0")
my_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="click me", command=cal_km)
button.grid(column=1, row=2)

window.mainloop()