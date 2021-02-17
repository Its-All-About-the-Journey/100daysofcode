# Grant Armstrong
# 100daysofcode - Day 28 Pomodoro Work/Break Timer
# 02/17/2021


from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = "#379b46"
YELLOW = "#f7f5dd"
BRIGHT_YELLOW = '#FBFF02'
FONT = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_count = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
# Function resets all global variables and GUI texts to their original values and stops the timer loop
def reset_timer():
	global reps, check_count
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text='00:00')
	timer_label.config(text="Timer", font=(FONT, 40, "bold"), fg=GREEN, bg=YELLOW)
	checks_label.config(text="")
	check_count = 0
	reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps, check_count
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	# Use the canvas itemcget(objectID, 'text) method to get the canvas text
	# In this case, we use the timer_text variable
	current_time = canvas.itemcget(timer_text, 'text')
	# Only start the timer and increase reps if it hasn't been started already
	# This line of code will prevent bugs if the user presses start multiple times
	if current_time == '00:00':
		reps += 1
		# What to do on work reps
		if reps in [1, 3, 5, 7]:
			timer_label.config(text="Work", font=(FONT, 40, "bold"), fg=GREEN, bg=YELLOW)
			count_down(work_sec)
		# What to do on small break reps
		elif reps in [2, 4, 6]:
			timer_label.config(text="Break", font=(FONT, 40, "bold"), fg=PINK, bg=YELLOW)
			check_count += 1
			checks_label.config(text="☑" * check_count)
			count_down(short_break_sec)
		# What to do on final large break
		elif reps == 8:
			check_count += 1
			checks_label.config(text="⭐", font=(FONT, 40, "bold"), bg=YELLOW, fg=DARK_GREEN)
			timer_label.config(text="Break", font=(FONT, 40, "bold"), fg=RED, bg=YELLOW)
			count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
	global timer
	seconds = count
	# Use time module to change total seconds into proper format
	struct_time = time.gmtime(seconds)  # Create time.struct_time object from seconds
	time_string = time.strftime("%M:%S", struct_time)  # returns a time string based on the format provided
	canvas.itemconfig(timer_text, text=time_string) # Set the canvas text equal to the time string
	if count > 0:
		# Set global timer variable so that it can be cancelled from reset_timer()
		timer = window.after(1000, count_down, count - 1)  # Recursively call count_down() subtracting a second
	else:
		# At each segway, where seconds have reached 0, recall start_timer()
		start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

checks_label = Label(font=(FONT, 22, "bold"), bg=YELLOW, fg=DARK_GREEN)
checks_label.grid(row=3, column=1)

canvas = Canvas(width=200, heigh=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', bg=GREEN, bd=1, activebackground=YELLOW, relief='flat', fg='white',
                      font=(FONT, 16, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', bg=GREEN, bd=1, activebackground=YELLOW, relief='flat', fg='white',
                      font=(FONT, 16, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
