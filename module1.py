def registreerimine(l:list, p:list, Text:str):
    """Funktsioon registreerib kasutaja
    param str l:login
    param str p:pasword
    param str filename:save files
    """
n = int(input("Sisesta kasutajate arv: "))
if n>0:
    with open(Text, 'a') as file:
        for j in range(n):
            login=True
            while login:
                new_login = input("sign up: ")
                if new_login not in l:
                    login = False
                else:
                    print("error")
            new_pasword = input("pasword: ")
            file.write(f"{new_login}:{new_pasword}\n")
            l.append(new_login)
            p.append(new_pasword)
    print("registreeritud! ")
#def autoriseerimine(l:str, p:str)->any:
#    """Funktsioon 
    
#    """
#    users_check=("Sisestage kasutajanimi valideerimiseks: ")
#    if users_check in users:
#        print("Kasutaja leitud")
#    else:
#        print("registreerimiseks vajutage 1")



