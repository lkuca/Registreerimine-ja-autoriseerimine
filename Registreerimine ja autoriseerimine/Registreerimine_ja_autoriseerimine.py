from math import*
from random import*
from mymodule import*
from tkinter import *
log=["User1", "User2"]
parool=["s1mple", "juppi"]
aken=Tk()
aken.geometry("400x500")
btn1=Button(text="registreerimine",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn2=Button(text="autoriseerimine",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn3=Button(text="muuta",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn4=Button(text="Unustasidparooli",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn5=Button(text="Logivälja",font="Arial 24",relief=GROOVE)#SUNKEN, RAISED
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()


aken.mainloop()
while True:
    print("Valige:")
    print("1. Registreerima")
    print("2. Logi sisse")
    print("3. Muudata login voi salasõna")
    print("4. Unustasid salasone")
    print("5. Logi välja")
    
    valik = input("Sisesta number (1-5): ")
    if valik == '1':
        registerimine()
    elif valik == '2':
        autoreserimine()
    elif valik == '3':
        muuta()
    elif valik == '4':
        Unustasidparooli()
    elif valik == '5':
        Logivälja()
        exit()
