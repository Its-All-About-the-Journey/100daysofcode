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
FONT = "Courier"
WORK_SECONDS = 1500  # 25 minutes
SHORT_BREAK_SECONDS = 300  # 5 minutes
LONG_BREAK_SECONDS = 1200  # 20 minutes
reps = 0
check_count = 0
timer = None
started_flag = True

# Bring window to front
def focus_window():
	window.lift()
	window.attributes('-topmost', True)
	window.after_idle(window.attributes, '-topmost', False)
	window.focus_force()

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

# Function to get total seconds from mm:ss time string
def countdown_from_current_time():
	# Use the canvas itemcget(objectID, 'text) method to get the canvas text
	# In this case, we use the timer_text variable
	time_string = canvas.itemcget(timer_text, 'text')
	m, s = time_string.split(':')
	current_seconds = int(m) * 60 + int(s)
	count_down(current_seconds)

# ---------------------------- TIMER RESET ------------------------------- # 
# Function resets all global variables and GUI texts to their original values and stops the timer loop
def reset_timer():
	global reps, check_count, started_flag
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text='00:00')
	timer_label.config(text="Timer", font=(FONT, 40, "bold"), fg=GREEN, bg=YELLOW)
	checks_label.config(text="", font=(FONT, 22, "bold"))
	start_button.config(text='Start')
	started_flag = True
	check_count = 0
	reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps, check_count, started_flag
	time_string = canvas.itemcget(timer_text, 'text')

	# When 'Start' button is pressed, do the following...
	if start_button['text'] == 'Start' or time_string == '00:00':
		start_button.config(text='Stop')
		reps += 1  # Add a rep everytime the cycle starts
		check_count += 1  # Add a check everytime the cycle starts
		# print(reps)
		# What to do on work reps
		if reps in [1, 3, 5, 7]:

			# Bring the window to the front and focus window
			focus_window()

			# Configure canvas text, initiate work period countdown
			timer_label.config(text="Work", font=(FONT, 40, "bold"), fg=GREEN, bg=YELLOW)

			# If starting new timer or new phase, initiate count_down() with constants
			if started_flag:
				count_down(WORK_SECONDS)
			# If resuming timer from stopped state, initiate count_down() with current time left
			elif not started_flag:
				countdown_from_current_time()
				started_flag = True

		# What to do on small break reps
		elif reps in [2, 4, 6]:
			# Bring the window to the front and focus window
			focus_window()

			# Configure canvas text, increase checks, begin short break countdown
			timer_label.config(text="Break", font=(FONT, 40, "bold"), fg=PINK, bg=YELLOW)
			# Set number of checkmarks - divide total check count (1 per round) by 2
			checks_label.config(text="☑" * int((check_count/2)))

			# If starting new timer or new phase, initiate count_down() with constants
			if started_flag:
				count_down(SHORT_BREAK_SECONDS)
			# If resuming timer from stopped state, initiate count_down() with current time left
			elif not started_flag:
				countdown_from_current_time()
				started_flag = True

		# What to do on final large break
		elif reps == 8:
			# Bring the window to the front and focus window
			focus_window()

			# Configure canvas text, increase checks, begin long break countdown
			checks_label.config(text="⭐", font=(FONT, 40, "bold"), bg=YELLOW, fg=DARK_GREEN)
			timer_label.config(text="Break", font=(FONT, 40, "bold"), fg=RED, bg=YELLOW)

			# If starting new timer or new phase, initiate count_down() with constants
			if started_flag:
				count_down(LONG_BREAK_SECONDS)
			# If resuming timer from stopped state, initiate count_down() with current time left
			elif not started_flag:
				countdown_from_current_time()
				started_flag = True

	# When 'Stop' Button is pressed, do the following...
	elif start_button['text'] == 'Stop' and time_string != '00:00':
		start_button.config(text='Start')  # Change button text to 'Start'
		window.after_cancel(timer)  # Pause the timer
		reps -= 1  # Remove a rep if user stops timer, as it will be re-added on start again
		check_count -= 1  # Remove a check if user stops timer, as it will be re-added on start again
		started_flag = False  # Change flag

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
                      font=(FONT, 16, "bold"), width=7, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', bg=GREEN, bd=1, activebackground=YELLOW, relief='flat', fg='white',
                      font=(FONT, 16, "bold"), width=7, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
