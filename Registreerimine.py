from module1 import *

login_list=[]
pasword_list=[]

while True:
    print("1-registreerimine/n2-autoriseerimine/n")
    valik=int(input("select action:"))
    if valik == 1:
        registreerimine(login_list, pasword_list, "TextFile1.txt")
     
    
        