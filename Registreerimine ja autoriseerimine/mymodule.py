from random import*
import string
logins=[]
passwords=[]
def salasõna(k: int)->bool:
    """
    Määrme salasõna..
    :parem int k:Järjend salasõna numbridest
    :rtype: bool
    """
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

# kasutaja registreerimise funktsioon
def registerimine():
    nicname = input("Sisesta oma nicname: ")
    if nicname in logins:
        print("See nicname on juba votud.")
        return
    salasona_valik = input("Kas sa tahad juhuslik salasõna? (Y/N): ")
    if salasona_valik.lower() == 'y':
        password = salasõna(8)
        print(f"Sinu salasona: {password}")
    else:
        while True:
            password = input("Sisesta oma salasõna: ")
            if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
    logins.append(nicname)
    passwords.append(password)
    print("Registreerimine õnnetus!")

# kasutaja autoriseerimise funktsioon
def autoreserimine():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See logini pole registreeritud.")
        return
    password = input("Sisesta oma salasõna: ")
    if password != passwords[logins.index(login)]:
        print("Vale salasõna.")
        return
    print("Login õnnetus!")

# nime või parooli muutmise funktsioon
def muuta():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See nimi ei ole registreeritud.")
        return
    valik = input("Kas soovite muuta oma nime või parooli? (login/password): ")
    if valik.lower() == 'login':
        new_login = input("Sisesta uue login: ")
        if new_login in logins:
            print("See login on juba võtud.")
            return
        logins[logins.index(login)] = new_login
        print("Login muudatus õnnetus.")
    elif valik.lower() == 'password':
        while True:
            new_password = input("Sisesta uue salasõne: ")
            if any(char.isdigit() for char in new_password) and any(char.islower() for char in new_password) and any(char.isupper() for char in new_password) and any(char in string.punctuation for char in new_password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
        passwords[logins.index(login)] = new_password
        print("Salasõne muudatus õnnetus.")
    else:
        print("Viga.")

# unustatud parooli taastamise funktsioon
def Unustasidparooli():
    login = input("sissestage oma login: ")
    if login not in logins:
        print("te ei ole registreeritud.")
        return
    new_password = salasõna(8)
    passwords[logins.index(login)] = new_password
    print(f"Sinu uus parool on: {new_password}")


# funktsioon kasutaja väljumist
def Logivälja():
    print("Sa logisid välja.")
    
