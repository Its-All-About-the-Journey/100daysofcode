from tkinter import *


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
update_window = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    canvas.after_cancel(update_window)
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    status.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    reps = 0
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    start_button.config(state="disabled")
    global reps
    if reps in [0, 2, 4, 6]:
        status.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)
    elif reps in [1, 3, 5]:
        # Collect current checkmarks and add a checkmark
        checkmarks.config(text=f"{''.join([checkmarks.cget('text'), '✓'])}")
        status.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif reps == 7:
        status.config(text="Break", fg=RED)
        # Collect current checkmarks and add a checkmark
        checkmarks.config(text=f"{''.join([checkmarks.cget('text'), '✓'])}")
        countdown(LONG_BREAK_MIN * 60)
        timer_reset()        
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global update_window
    seconds = int(count % 60)
    minutes = int(count / 60)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if count > 0:
        update_window = window.after(1000, countdown, count - 1)
    if count == 0:
        #Bring window to front (then disable the forced window-on-top)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        timer_start()
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=30,pady=20,bg=YELLOW)

background_image = PhotoImage(file="source_code/day028/tomato.png")

#Build canvas with background iamge (HIGHLIGHT THICKNESS = border for canvas)

canvas = Canvas(width=203, height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100, 112, image=background_image)
timer_text = canvas.create_text(100, 135, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, "30", "bold"))
canvas.grid(column=1,row=1)

#Status Label
status = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
status.grid(column=1, row=0)

#Checkmarks Label
checkmarks = Label(text="", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

#Start Button
start_button = Button(text="Start", command=timer_start, highlightthickness=0)
start_button.grid(column=0, row=2, pady=30)

#Reset Button
reset_button = Button(text="Reset", command=timer_reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()