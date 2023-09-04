# ---------------------------- LIBRARIES ------------------------------- #
from tkinter import * 
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARKGREEN = '#4e9525'
YELLOW = "#f7f5dd"
FONTNAME = "Courier"
WORKMIN = 25
SHORTBREAKMIN = 5
LONGBREAKMIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS, TIMER, checkmarkstr
    
    REPS = 0
    window.after_cancel(TIMER)
    checkmarkstr = ''
    label.config(text='Timer', fg=GREEN)
    checkmark.config(text=checkmarkstr)
    canvas.itemconfig(timer, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global REPS, checkmarkstr
    REPS += 1

    worksec = WORKMIN * 60
    shortbreaksec = SHORTBREAKMIN * 60
    longbreaksec = LONGBREAKMIN * 60

    if REPS == 8:
        countdown(longbreaksec)
        label.config(text='Break', fg=RED)
    elif REPS % 2 == 0:
        countdown(shortbreaksec)
        label.config(text='Break', fg=PINK)
    else:
        countdown(worksec)
        label.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global REPS, TIMER, checkmarkstr

    countmin = floor(count / 60)
    if countmin < 10:
        countmin = f'0{countmin}'

    countsec = count % 60
    if countsec < 10:
        countsec = f'0{countsec}'

    canvas.itemconfig(timer, text=f'{countmin}:{countsec}')

    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)

    else:
        if REPS % 2 == 0:
            checkmarkstr += '✔'
            checkmark.config(text=checkmarkstr)
        start()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 134, text='00:00', fill='white', font=(FONTNAME, 25, 'bold'))
canvas.grid(column=1, row=1)

label = Label(text='Timer', font=(FONTNAME, 40, 'bold'), bg=YELLOW, fg=GREEN, highlightthickness=0)
label.grid(column=1, row=0)

checkmarkstr = ''
checkmark = Label(text=checkmarkstr, font=(FONTNAME, 12, 'bold'), bg=YELLOW, fg=GREEN, highlightthickness=0)
checkmark.grid(column=1, row=5)

startbutton = Button(text=' Start ', bg=YELLOW, fg=DARKGREEN, highlightthickness=0, command=start)
startbutton.grid(column=0, row=3)

resetbutton = Button(text='Reset', bg=YELLOW, fg=RED, highlightthickness=0, command=reset)
resetbutton.grid(column=3, row=3)

window.mainloop()