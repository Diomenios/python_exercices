#!/usr/local/bin/python3.6
#! -*-coding:Utf-8 -*

annee = input("saisissez une année : ")

anneeInt = int(annee)


if anneeInt % 4 != 0 :
    print(annee + " n'est pas bissextile")
elif anneeInt % 100 == 0 :
    if anneeInt % 400 == 0 :
        print(annee + " est bissextile")
    else :
        print(annee + " n'est pas bissextile")
else :
    print(annee + " est bissextile")
