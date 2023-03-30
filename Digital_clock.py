from tkinter import *
from time import *
def show():
    time_value=strftime("%H : %M : %S  %p")
    time_label.config(text=time_value)
    
    day_value=strftime("%A")
    day_label.config(text=day_value)

    date_value=strftime("%B  %d  %Y")
    date_label.config(text=date_value)
    
    win.after(1000,show)
win=Tk()
win.config(bg="black")

label1=Label(win, font=("Cooper Black",30), text="Digital Clock",fg='pink',bg='black')
label1.pack()

time_label=Label(win,font=('Cooper Black',50), fg='cyan',bg='black')
time_label.pack()

day_label=Label(win,font=("Papyrus",30),fg="pink",bg='black')
day_label.pack()

date_label=Label(win,font=("Papyrus",30),fg='pink',bg='black')
date_label.pack()

show()

win.mainloop()
