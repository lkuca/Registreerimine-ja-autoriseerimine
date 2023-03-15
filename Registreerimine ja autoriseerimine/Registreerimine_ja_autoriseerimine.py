from math import*
from random import*
from mymodule import*


log=["User1", "User2"]
parool=["s1mple", "juppi"]

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
