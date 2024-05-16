from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 1500
SHORT_BREAK_SEC = 300
LONG_BREAK_SEC = 1200
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    main_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        main_label.config(text="Break", fg=RED)
        countdown(LONG_BREAK_SEC)
    elif reps % 2 == 0:
        main_label.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_SEC)
    else:
        main_label.config(text="Work", fg=GREEN)
        countdown(WORK_SEC)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global timer

    m = count // 60
    s = count - (m * 60)
    time = f"{m:0>2d}:{s:0>2d}"
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps == 3:
            check_marks.config(text="✓")
        elif reps == 5:
            check_marks.config(text="✓✓")
        elif reps == 7:
            check_marks.config(text="✓✓✓")
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

main_label = Label(text="Timer", font=("Arial", 35, "bold"), fg=GREEN, bg=YELLOW)
main_label.grid(column=2, row=1)

start_bot = Button(text="Start", command=start_timer)
start_bot.grid(column=1, row=3)

reset_bot = Button(text="Reset", command=reset_timer)
reset_bot.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
check_marks.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Python-100-days-of-code/day 28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


window.mainloop()
