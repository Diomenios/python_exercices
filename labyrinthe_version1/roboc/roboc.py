# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
import labyrinthe

# On charge les cartes existantes
cartes = []
global save
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        # Regarde si une sauvegarde existe
        if nom_carte == "save.":
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                if contenu != "":
                    carte = Carte(nom_carte, contenu)
                    save = carte
                else:
                    save = None
        else:
             with open(chemin, "r") as fichier:
                 contenu = fichier.read()
                 carte = Carte(nom_carte, contenu)
                 cartes.append(carte)
            # Création d'une carte, à compléter

# On verifie si une sauvegarde a ete trouvee
# todo si la sauvegarde est trouvee, ecrire le code pour la chargee
if save != None:
    print("une sauvegarde a été trouvée")

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))
#todo effacer les 2 lignes ci-dessous
for i,carte in enumerate(cartes):
    carte.labyrinthe.affiche_labyrinthe()


# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
