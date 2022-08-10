from itertools import count
from tkinter import *
from tkinter import messagebox
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35))
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps,timer
    try:
        window.after_cancel(timer)
    except:
        pass
    reps +=1

    work_sec= WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED,font=(FONT_NAME,35))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Fast Break", fg=PINK,font=(FONT_NAME,35))
        count_down(break_sec)
    else:
        timer_label.config(text="Work Work", fg=GREEN,font=(FONT_NAME,35))
        count_down(work_sec)
    
    marks = ""
    # session = math.floor(reps/2)
    for _ in range(reps//2):
        marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # min
    count_min = count // 60
    # sec
    count_sec = count % 60

    if count_min <10:
        count_min=f"0{count_min}"
    if count_sec<10:
        count_sec = f"0{count_sec}"

    # config canvas text
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        # count down part
        global timer
        timer = window.after(1000,count_down,count-1)

    if count == 0:
        messagebox.showinfo(title="InfoBox",message="Session has ended.")
    # else:
    #     start_timer()
        # global marks
        # session = math.floor(reps/2)
        # for _ in range(session):
        #     marks += "✔"
        # check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)




#timer label
timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35))
timer_label.grid(column=1,row=0)

#canvas and size
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)


# get current working directory
path = os.getcwd() +"\\14_tkinter_timer\\tomato.png"
#import image
#surface path
# path=r"C:\Users\chenx\Desktop\Git\Class\Udemy_Python100\14_tkinter_timer\tomato.png"

#desktop path
# path = r"C:\Users\Gumo\Desktop\Git\Class\Udemy_Python\14_tkinter_timer\tomato.png"
tomato_img = PhotoImage(file=path)
#insert image
canvas.create_image(100,112,image=tomato_img)

#timer text
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=timer_reset)
reset_button.grid(column=2,row=2)

check_marks =Label(text="",fg=GREEN,highlightthickness=0,bg=YELLOW)
check_marks.grid(column=1,row=3)

start_button.focus_force()


window.mainloop()