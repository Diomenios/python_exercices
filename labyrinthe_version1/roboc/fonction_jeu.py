# -*-coding:Utf-8 -*

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
    while !endGame:
        carte.labyrinthe.affiche_labyrinthe()
        input("")
