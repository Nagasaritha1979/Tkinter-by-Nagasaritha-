from tkinter import *

win=Tk()
btn1=Button(win,text="Quotes")
btn1.pack()


labelframe1=LabelFrame(win, text="Quotes", labelanchor=SW, labelwidget=btn1)
labelframe1.pack(fill=BOTH, expand=True)


quote1=Label(labelframe1,text="An apple a day keeps the doctor away.")
quote1.pack()

quote2=Label(labelframe1,text="Do not count your chickens before they hatch.")
quote2.pack()

quote3=Label(labelframe1,text="A stich in time saves nine.")
quote3.pack()


labelframe2=LabelFrame(win, text="Motivational Quotes")
labelframe2.pack(fill=BOTH,expand=True)

motive1=Label(labelframe2, text= "Nothing is impossible.")
motive1.pack()

motive2=Label(labelframe2, text= "Failure is the stepping stone for success.")
motive2.pack()

motive3=Label(labelframe2, text= "Dream big.")
motive3.pack()

win.mainloop()

