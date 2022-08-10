'''
1XX : HOLD ON
2XX : HERE YOU GO
3XX : GO AWAY
4XX : YOU SCREWED UP
    401 no authorization
    
5XX : I SCREWRED UP

httpstatuses.com
'''

import requests
from tkinter import *

def get_quote():
    url="https://api.kanye.rest"
    response = requests.get(url=url)
    data = response.json()
    canvas.itemconfig(quote_text,text=data['quote'])



window = Tk()
window.title("Kaye Says...")
window.config(padx=50,pady=50)

canvas = Canvas(width=300, height=414)

# background image
path_background = r"C:\Users\Gumo\Desktop\Git\Class\Udemy_Python\18_API\background.png"
background_img=PhotoImage(file=path_background)
canvas.create_image(150,207,image=background_img)

# quote
quote_text = canvas.create_text(150,207, text="Kanye Quote Goes HERE", width=250, font=("Ariel"))
canvas.grid(row=0,column=0)

#kanye image
path_kanye = r"C:\Users\Gumo\Desktop\Git\Class\Udemy_Python\18_API\kanye.png"
kanye_img = PhotoImage(file=path_kanye)
kanye_button = Button(image=kanye_img,highlightthickness=0,command=get_quote)
kanye_button.grid(row=1,column=0)


window.mainloop()