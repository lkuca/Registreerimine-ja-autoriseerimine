from random import *
import string
"""
m��arme salas�na
"""
saladuss�na=""
def salas�na(k: int)->bool:
    for i in range(k):
        t=choice(string.ascii_letters)
        num=choice([1,2,3,4,5,6,7,8,9,10])
        symbol=choice(["*","-",".","!","_"])
        t_num=[t,str(num),symbol]
        saladuss�na+=choice(t_num)
    return saladuss�na
def register():
    reg=input("sissestage oma nimi/nicname: ")


