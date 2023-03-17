from math import*
from random import*
from mymodule import*
from tkinter import *
log=["User1", "User2"]
parool=["s1mple", "juppi"]
aken1=Tk()
aken1.geometry("400x500")
btn1=Button(text="registreerimine",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn2=Button(text="autoriseerimine",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn3=Button(text="muuta",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn4=Button(text="Unustasidparooli",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn5=Button(text="Logivälja",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn1.bind("<Button-1>",registerimine)
btn2.bind("<Button-1>",autoreserimine)
btn3.bind("<Button-1>",muuta)
btn4.bind("<Button-1>",Unustasidparooli)
btn5.bind("<Button-1>",Logivälja)
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()


aken1.mainloop()
