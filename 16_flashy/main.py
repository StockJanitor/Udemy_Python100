BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn={}
from tkinter import *
import pandas as pd
import random

path_data2 = r"C:\Users\chenx\Desktop\Git\Class\Udemy_Python100\16_flashy\data\words_to_learn.csv"
path_data = r"C:\Users\chenx\Desktop\Git\Class\Udemy_Python100\16_flashy\data\french_words.csv"
try:
    data = pd.read_csv(path_data2)
except FileNotFoundError:
    original_data = pd.read_csv(path_data)
    to_learn=original_data.to_dict(orient="records")
else: 
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text = "French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=path_img_card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text = "English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=path_img_card_back)


def is_known():
    global path_data2
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(path_data2,index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800,height=526)

path = r"C:\Users\chenx\Desktop\Git\Class\Udemy_Python100\16_flashy\images\card_front.png"
path_img_card_front=PhotoImage(file=path)
path2=r"C:\Users\chenx\Desktop\Git\Class\Udemy_Python100\16_flashy\images\card_back.png"
path_img_card_back = PhotoImage(file=path2)
card_background = canvas.create_image(400,263,image=path_img_card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"italic"))
canvas.grid(row=0,column=0,columnspan=2)

path_img_wrong = r"C:\Users\chenx\Desktop\Git\Class\Udemy_Python100\16_flashy\images\wrong.png"
cross_image = PhotoImage(file=path_img_wrong)
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

path_img_right = r"C:\Users\chenx\Desktop\Git\Class\Udemy_Python100\16_flashy\images\right.png"
check_image = PhotoImage(file=path_img_right)
known_button = Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)


next_card()



window.mainloop()
