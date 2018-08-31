#!/usr/local/bin/python3.6
#! -*-coding:Utf-8 -*

import os
from random import randrange
from math import ceil

print("bienvenu dans notre casino \n")

miseDuJoueur = int(input("veuillez introduire votre mise de départ : \n"))

while miseDuJoueur <= 0 :
    miseDuJoueur =  int(input("veuillez introduire une mise plus grand que 0 : \n"))
while miseDuJoueur > 0 :
    choixDuJoueur = int(input("veuillez choisir une case où miser entre 1 et 50 : q\n"))
    if choixDuJoueur < 1 | choixDuJoueur > 50 :
        print("mauvaise mise veuillez réessayer")
        pass
    else :
        mise = int(input("veuillez choisir la somme que vous voulez miser : \n"))
        if mise > miseDuJoueur :
            print("erreur vous n'avez pas assez d'argent")
            pass
        else :
            number = randrange(1, 50)
            if number == choixDuJoueur :
                print("la roulette donne le chiffre " + str(number) + "\n")
                print("votre chiffre est " + str(choixDuJoueur) + "\n")
                miseDuJoueur = miseDuJoueur + 3*mise
                print("félicitation vous avez gagné ! votre mise est maintenant de : " + str(miseDuJoueur) + "\n" )
            else :
                if number%2 == choixDuJoueur%2 :
                    print("la roulette donne le chiffre " + str(number) + "\n")
                    print("votre chiffre est " + str(choixDuJoueur) + "\n")
                    miseDuJoueur = miseDuJoueur + ceil(mise/2)
                    print("félicitation vous avez gagné par couleur ! votre mise est maintenant de : " + str(miseDuJoueur) + "\n" )
                else :
                    print("la roulette donne le chiffre " + str(number) + "\n")
                    print("votre chiffre est " + str(choixDuJoueur) + "\n")
                    miseDuJoueur = miseDuJoueur - mise
                    print("Vous avez perdu ! votre mise est maintenant de : " + str(miseDuJoueur) + "\n" )
