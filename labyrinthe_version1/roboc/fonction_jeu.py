# -*-coding:Utf-8 -*

import os
import sys

from carte import Carte
from labyrinthe import Labyrinthe


""" Ce module contient toutes les fonctions nécessaires au bon déroulement d'une
    partie.  Entre autre la boucle principale du jeu"""

def play(carte):
    print("Vous avez lancé la carte : {}".format(carte.nom))
    print("Les commandes sont : 'Q' quitter la partie,'N' vers le haut, 'E' vers \
     la droite, 'S' vers le bas, 'O' vers la gauche.  Si vous faites suivre votre \
     commande par un chiffre, elle sera répétée autant de fois que votre chiffre.")
    endGame = False
    while not endGame:
        carte.labyrinthe.affiche_labyrinthe()
        retour = input("")
        if len(retour) == 1:
            print("option one :")
            if retour.lower() == 'q':
                #save and quit
            else:
                carte = move_switch(retour, carte)
        elif len(retour) == 2:
            print("option two:")
            if retour[0].lower() == 'q':
                #save and quit
            else:
                try:
                    carte = move_switch(retour[0], carte, retour[1])
                except TypeError:
                    print("erreur votre deuxième élément doit être un chiffre.")
        else:
            print("erreur, votre entrée est incorrecte")
            print("Les commandes sont : 'Q' quitter la partie,'N' vers le haut, 'E' vers \
             la droite, 'S' vers le bas, 'O' vers la gauche.  Si vous faites suivre votre \
             commande par un chiffre, elle sera répétée autant de fois que votre chiffre.")
        carte.labyrinthe.affiche_labyrinthe()

#todo ecrire les differentes methodes de move dans labyrinthe.py
def move_switch(lettres, carte, count = 1):
    if retour.lower() == 'n':
        #move up
    elif retour.lower() == 's':
        #move down
    elif retour.lower() == 'e':
        #move right
    elif retour.lower() == 'o':
        #move left
    else:
        print("erreur, votre entrée est incorrecte")
        return carte

def save(carte):
    with open("cartes/save.txt", "w+") as fichier:
        list = carte.labyrinthe.grille_to_chaine()
        for ligne in list :
            fichier.write(ligne)
    sys.exit()
