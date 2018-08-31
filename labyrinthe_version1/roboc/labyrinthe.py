# -*-coding:Utf-8 -*

import os

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, grille, size):
        self.robot = robot
        self.grille = grille
        self.size = size

    def printLab(self):
        print(self.grille)
        print(self.size)

    def affiche_labyrinthe(self):
        print(self.size)
        for i in range(0, self.size[0]):
            array = ""
            for j in range(0, self.size[1]):
                array += self.grille[(i, j)]
            print(array)
