# -*-coding:Utf-8 -*

import os

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, grille, size):
        self.robot = robot      #tuple représentant la position du robot dans le labyrinthe
        self.grille = grille
        self.size = size
        
    def affiche_labyrinthe(self):

        """Affiche le labyrinthe ligne par ligne."""

        for i in range(0, self.size[0]):
            array = ""
            for j in range(0, self.size[1]):
                array += self.grille[(i, j)]
            print(array)

    def grille_to_chaine(self):

        """Transforme la grille stockée dans l'objet en une chaine de Strings

            La grille est initialement stockée sous forme d'un dictionnaire dans
            cet objet.  Cette methode va constituer une liste de Strings où
            chaque String correspond à une ligne du labyrinthe.  """

        list = []
        for i in range(0, self.size[0]):
            array = ""
            for j in range(0, self.size[1]):
                array += self.grille[(i, j)]
            array+= '\n'
            list.append(array)
        return list

#ci-dessous se trouve les 4 methodes gerant les deplacements du token 'X'

    def move_droite(self, number):

        """ se charge de décaler le token 'X' d'une colonne vers la droite """

        while number > 0:
            new_position = (self.robot[0], self.robot[1]+1)
            if new_position[1] >= self.size[1]:
                return False
            elif self.grille[new_position].upper() == 'O':
                return False
            elif self.grille[new_position].upper() == 'U':
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                return True
            else:
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                number-=1
        return False

    def move_gauche(self, number):

        """ se charge de décaler le token 'X' d'une colonne vers la gauche """

        while number > 0:
            new_position = (self.robot[0], self.robot[1]-1)
            if new_position[1] < 0:
                return False
            elif self.grille[new_position].upper() == 'O':
                return False
            elif self.grille[new_position].upper() == 'U':
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                return True
            else:
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                number-=1
        return False

    def move_haut(self, number):

        """ se charge de décaler le token 'X' d'une ligne vers le haut """

        while number > 0:
            new_position = (self.robot[0]-1, self.robot[1])
            if new_position[0] < 0:
                return False
            elif self.grille[new_position].upper() == 'O':
                return False
            elif self.grille[new_position].upper() == 'U':
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                return True
            else:
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                number-=1
        return False

    def move_bas(self, number):

        """ se charge de décaler le token 'X' d'une ligne vers le bas """

        while number > 0:
            new_position = (self.robot[0]+1, self.robot[1])
            if new_position[0] >= self.size[0]:
                return False
            elif self.grille[new_position].upper() == 'O':
                return False
            elif self.grille[new_position].upper() == 'U':
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                return True
            else:
                self.grille[self.robot] = " "
                self.grille[new_position] = "X"
                self.robot = new_position
                number-=1
        return False
