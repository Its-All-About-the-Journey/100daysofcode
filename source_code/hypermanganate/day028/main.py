# 100 Days of Code: Python
# Day 28
# Tomato Timer
# Adam Pawlowski (@hypermanganate)


from PIL import ImageTk, Image
import tkinter

# const

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_HEIGHT = 200
TOMATO_WIDTH = 225


class Timer:

    # Periods odd = 25 minutes
    # Periods even not period % 8 = 5 minutes else 20 minutes

    def __init__(
        self, window: tkinter,
        canvas: tkinter.Canvas,
        label: tkinter.Label,
        image_index: int,
        image: Image,
        goal_text: tkinter.StringVar
         ) -> None:

        self.window = window
        self.canvas = canvas
        self.label = label
        self.image = image
        self.original_iamge = image
        self.image_index = image_index
        self.tomato_scale = 1.0
        self.goal_text = goal_text

        self.running = False
        self.period = 0

    def set_progress(self, progress_amount: int):
        new_goal = "☕" * progress_amount
        self.goal_text.set(new_goal)

    def set_period_details(self):
        print(f"It is period {self.period}")
        if self.period % 2:
            self.period_timer = WORK_MIN * 60
        else:
            self.set_progress(int(self.period/2))
            if self.period % 8:
                self.period_timer = SHORT_BREAK_MIN * 60
            else:
                self.period_timer = LONG_BREAK_MIN * 60

        self.scale_factor = .40 / self.period_timer

        self.update_timer_label(self.period_timer)
        self.tomato_scale = 0.6
        self.rescale_tomato(self.tomato_scale)
        self.window.after(1000, self.tick)

    def start(self):
        if not self.running:
            self.running = True
            self.period += 1
            self.set_period_details()

    def reset(self):
        self.running = False
        self.period = 0
        self.tomato_scale = 1.0
        self.update_timer_label(0)
        self.rescale_tomato(self.tomato_scale)
        self.set_progress(0)

    def update_timer_label(self, time: int):
        timer_minutes = time // 60
        timer_seconds = time % 60

        self.canvas.itemconfig(
            self.label,
            text='{:02d}:{:02d}'.format(
                        timer_minutes, timer_seconds
                        )
        )

    def tick(self):

        if self.period_timer > 0:
            if self.running:
                self.period_timer -= 1
                self.update_timer_label(
                    self.period_timer
                    )
                self.tomato_scale += self.scale_factor
                self.rescale_tomato(self.tomato_scale)
                self.window.after(1000, self.tick)
        else:
            if self.period == 8:
                self.reset()
            else:
                self.period += 1
                self.set_period_details()

    def rescale_tomato(self, scale_percent: float):

        new_x = round(TOMATO_HEIGHT * scale_percent)
        new_y = round(TOMATO_WIDTH * scale_percent)

        resized = ImageTk.PhotoImage(self.original_iamge.resize(
                (new_x, new_y),
                resample=Image.NEAREST
                )
        )

        self.canvas.itemconfig(self.image_index, image=resized)
        self.image = resized


def start_timer_button():
    my_timer.start()


def reset_timer_button():
    my_timer.reset()


#
# Window Setup
#


# New Window
window = tkinter.Tk()

# Title of Window
window.title("Tomato Timer")

# Window expands by default, but this is the mininum it should be
window.minsize(width=200, height=225)

# Window border and background
window["padx"] = 50
window["pady"] = 50
window["bg"] = YELLOW

# Canvas Object
canvas = tkinter.Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)

# Tomato Background
tomato_image = Image.open("./tomato.png")
tomato_photoimage = ImageTk.PhotoImage(file="tomato.png")
c_tomato_image = canvas.create_image(100, 112, image=tomato_photoimage)

# Main Label Object
form_label = tkinter.Label(text="Work Intensity Timer",
                           font=(FONT_NAME, 36, "bold"),
                           fg=GREEN,
                           bg=YELLOW
                           )

# Timer Label
c_timer_label = canvas.create_text(100, 130,
                                   text="00:00",
                                   fill=PINK,
                                   font=(FONT_NAME, 35, "bold")
                                   )

# Goal Label
goal_text = tkinter.StringVar(value="")
goal_label = tkinter.Label(text="",
                           font=(FONT_NAME, 36, "bold"),
                           bg=YELLOW,
                           fg=RED,
                           textvariable=goal_text
                           )

# Reset Button Object
reset_button = tkinter.Button(text="Reset", command=reset_timer_button)

# Start Button Object
start_button = tkinter.Button(text="Start", command=start_timer_button)

# Timer Class Object
my_timer = Timer(window, canvas, c_timer_label,
                 c_tomato_image, tomato_image, goal_text
                 )

# Composite the window

form_label.grid(column=1, row=0)

start_button.grid(column=0, row=2, sticky="nw")
goal_label.grid(column=1, row=3)
reset_button.grid(column=2, row=2)

canvas.grid(column=1, row=1)

# Set User Focus
start_button.focus()

# At the end of program, to listen for events
window.mainloop()
