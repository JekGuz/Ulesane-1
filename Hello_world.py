from random import *  #* - все функции, второй вариант, если обращаемся к определенной функции, randint as rd 
from math import * # матаматические функции, в данный момент Пи

#Ülesanne 1
# print("Tere maailm!")
# nimi=input("Palun kirjuta oma nimi ").capitalize() #lower() - все маленькие, upper() - все большие, capitalize() - первая будет всегда большая другие маленькие
# print("Tere tulemast! Tervitan sind " + nimi + "!")
# print("Tere tulemast! Tervitan sind" , nimi + "!") #"," действует как " " а затем идет слова "+" обьядиняет тобишь Слова если до не было пробела будет написано слитно
# vanus=int(input("Kui vana sa oled? "))
# print("Tere Tulemast! Tervitan sind" , nimi , "Sa oled", vanus , "aastat vana.")
# print(f"\tTere Tulemast! Tervitan sind  {nimi} Sa oled {vanus} aastat vana.")

#Ülesanne 2
# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käeb_koolis = True
# print(type(vanus))
# print(type(eesnimi))
# print(type(pikkus))

#Ülesanne 3  import имя_модуля или from имя_модуля import *
# kokku=randint(1,1000)
# print(f"Kokku on {kokku} kommi")
# kommi=int(input("Mittu kommi sa tahad? "))
# kokku = kokku - kommi
# print(f"Jääk on {kokku} kommi")

#Ülesanne 4  L=2*P*R d=L/P
print("Läbimõõdu leidmine ")
#l - ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")