# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

from labyrinthe import Labyrinthe

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)
        #variable de test
        self.chaine = chaine

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def creer_labyrinthe_depuis_chaine(self, chaine):

        """ cette methode permet de creer un labyrinthe a partir d'une chaine.

            Pour se faire, nous allons creer une grille dont le coin haut/gauche
            le point (0,0) que nous parcourerons element par element,
            ligne par ligne"""

        split_chaine = chaine.strip("\n").split("\n")
        robot = None
        carte = {}
        for i,morceau in enumerate(split_chaine):
            for j,elem in enumerate(morceau):
                if elem == 'X':
                    robot = (i,j)
                carte[(i,j)] = elem
                j+=1
            i+=1
        size = (len(split_chaine), len(split_chaine[0]))
        return Labyrinthe(robot, carte, size)

    #methode de test
    def chaine_print(self):
        split_chaine = self.chaine.strip("\n").split("\n")
        print("lenght = "+str(len(split_chaine)))
