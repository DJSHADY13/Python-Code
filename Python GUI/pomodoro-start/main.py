import math
from tkinter import *

from invoke import Responder
from matplotlib.pyplot import text
from sympy import check_assumptions
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
CHECK_SYMBOL = "✓"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=RED)
        count_down(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec == 0:
        count_sec = "00"
    if int(count_sec) < 10 and int(count_sec) > 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)  
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += CHECK_SYMBOL
        check_marks.config(text=mark)
         
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Timer font
timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
timer_label.grid(column=1, row=0)
#Timer image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Python GUI/pomodoro-start/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(104 , 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)
#Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0,command= reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,25))

check_marks.grid(column=1, row=3)

window.mainloop()