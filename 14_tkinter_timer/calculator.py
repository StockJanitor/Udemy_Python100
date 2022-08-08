from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("first gui Program")
window.config(padx=20,pady=20)

# input miles
miles_input = Entry()
miles_input.grid(column=1,row=0)

# text label miles
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

# text label is euqal to
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

# result
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

# text label
kilometer_label = Label(text="km")
kilometer_label.grid(column=2,row=1)

# button
calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column = 1, row = 2)










window.mainloop()