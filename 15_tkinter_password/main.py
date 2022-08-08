from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['!','@','#']

def gen_pass():
    password_letters = [choice(ALPHABET) for _ in range(randint(6,8))]
    password_numbers = [str(randint(0,9)) for _ in range(randint(1,3))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(1,3))]
    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    user=username_input.get()
    password = password_input.get()
    is_ok=messagebox.askokcancel(title="Check",message=f"{website}\n{user}\n{password}")
    
    if is_ok:
        path = r"C:\Users\Gumo\Desktop\Git\Class\Udemy\14_tkinter_timer\data.txt"
        with open(path,"a") as data_file:
            data_file.write(f"{website} | {user} | {password}\n")
            website_input.delete(0,END)
            password_input.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pass Manager")
window.config(padx=50,pady=50)


############### LOGO ###############
canvas = Canvas(width=200,height=200)
path = r"C:\Users\Gumo\Desktop\Git\Class\Udemy\15_tkinter_password\logo.png"
lock_image = PhotoImage(file=path)
#insert image
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

############### Website ###############
#Part 1 Label
website_text = Label(text="Website:")
website_text.grid(column=0,row=1)

#Part 2 Entry
website_input = Entry(width=40)
website_input.grid(column=1,row=1)
website_input.focus()
############### Email/Username ###############
#Part 1 Label
username_text = Label(text="Email/Username:")
username_text.grid(column=0,row=2)

#Part 2 Entry
username_input = Entry(width=40)
username_input.grid(column=1,row=2)
username_input.insert(0,"@gmail.com")
############### Email/Username ###############
#Part 1 Label
password_text = Label(text="Password:")
password_text.grid(column=0,row=3)

#Part 2 Entry
password_input = Entry(width=40)
password_input.grid(column=1,row=3)

# Generate button
generate_button = Button(text="Gnerate Password",command=gen_pass)
generate_button.grid(column=2,row=3)

# Add button
add_button = Button(text="Add",width=30,command=save)
add_button.grid(column=1, row=4)




window.mainloop()