# -*-coding:Utf-8 -*

import os
import sys

from carte import Carte
from labyrinthe import Labyrinthe


""" Ce module contient toutes les fonctions nécessaires au bon déroulement d'une
    partie.  Entre autre la boucle principale du jeu"""

def play(carte):

    """Cette fonction contient la boucle principale du jeu.

    De plus, elle vérifie que les entrées des joueurs sont correctes, et
    sinon leur réimprime les règles du jeu."""

    print("Vous avez lancé la carte : {}".format(carte.nom))
    print("Les commandes sont : 'Q' quitter la partie,'N' vers le haut, 'E' vers \
la droite, 'S' vers le bas, 'O' vers la gauche.  Si vous faites suivre votre \
commande par un chiffre, elle sera répétée autant de fois que votre chiffre. \
Votre personnages est représenté par le token 'X' et les murs par le token 'O'")

    while True:
        carte.labyrinthe.affiche_labyrinthe()
        retour = input("")
        if len(retour) == 1:
            if retour.lower() == 'q':
                #sauvegarde et quitte la partie
                save(carte)
                sys.exit()
            else:
                carte = move_switch(retour, carte)
        elif len(retour) == 2:
            if retour[0].lower() == 'q':
                #sauvegarde et quitte la partie
                save(carte)
                sys.exit()
            else:
                try:
                    carte = move_switch(retour[0], carte, int(retour[1]))
                except ValueError:
                    print("erreur votre deuxième élément doit être un chiffre.")
        else:
            print("erreur, votre entrée est incorrecte")
            print("Les commandes sont : 'Q' quitter la partie,'N' vers le haut, 'E' vers \
la droite, 'S' vers le bas, 'O' vers la gauche.  Si vous faites suivre votre \
commande par un chiffre, elle sera répétée autant de fois que votre chiffre. \
Votre personnages est représenté par le token 'X' et les murs par le token 'O'")

def move_switch(lettre, carte, count = 1):

    """Cette fonction sert principalement à choisir entre les 4 directions de
        déplacement.

        choisi entre Nord, Sud, Est, Ouest et teste en même temps les conditions
        de colisions à l'aide des différentes méthodes 'move' du module
        labyrinthe.  En cas de victoire, lance la méthode 'victory'."""

    if lettre.lower() == 'n':
        if carte.labyrinthe.move_haut(count):
            erase()
            victory(carte)
        else:
            save(carte)
            return carte
    elif lettre.lower() == 's':
        if carte.labyrinthe.move_bas(count):
            erase()
            victory(carte)
        else:
            save(carte)
            return carte
    elif lettre.lower() == 'e':
        if carte.labyrinthe.move_droite(count):
            erase()
            victory(carte)
        else:
            save(carte)
            return carte
    elif lettre.lower() == 'o':
        if carte.labyrinthe.move_gauche(count):
            erase()
            victory(carte)
        else:
            save(carte)
            return carte
    else:
        print("erreur, votre entrée est incorrecte")
        return carte

def save(carte):

    """Sauvegarde la carte passer en paramètre dans le fichier 'save.txt'"""

    with open("cartes/save.txt", "w+") as fichier:
        list = carte.labyrinthe.grille_to_chaine()
        for ligne in list :
            fichier.write(ligne)

def erase():

    """Ecrase le fichier de sauvegarde"""

    with open("cartes/save.txt", "w") as fichier:
        pass

def victory(carte):

    """Affiche un message de victoire puis quitte le jeu"""

    carte.labyrinthe.affiche_labyrinthe()
    print("victoire, vous avez gagné la partie, vous êtes sortis du labyrinthe !!!")
    sys.exit()
