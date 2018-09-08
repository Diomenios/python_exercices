# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte
import labyrinthe
from fonction_jeu import play

# On charge les cartes existantes
cartes = []
save = None
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        print(chemin)
        nom_carte = nom_fichier[:-3].lower()
        # Regarde si une sauvegarde existe
        if nom_carte == "save.":
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                if contenu != "":
                    save = Carte(nom_carte, contenu)
                else:
                    save = None
        else:
             with open(chemin, "r") as fichier:
                 contenu = fichier.read()
                 carte = Carte(nom_carte, contenu)
                 cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# On verifie si une sauvegarde a ete trouvee
gameSave = False
if save != None:
    print("une sauvegarde a été trouvée")
    while True :
        retour = input("voulez-vous charger la sauvegarde ?(n\o)")
        if retour.lower() == 'o':
            gameSave = True
            break
        elif retour.lower() == 'n':
            break
        else :
            print("votre entrée est incorrecte veuillez recommencer !")

gameMap = None
if gameSave:
    #todo : à retirer
    print("chargement de la sauvegarde")
    play(save)
else :
    while True:
        retour = input("Veuillez choisir le numéro de la carte que vous voulez jouer :")
        try:
            #lors de la conversion de 'retour', il peut avoir une erreur si
            #retour n'est pas un chiffre en base 10 (lettre 'a' par exemple)
            if int(retour) in range(1, len(cartes)+1) :
                gameMap = int(retour)
                print("carte choisie : {}".format(gameMap))
                break
            else:
                print("Votre entrée est incorrecte, veuillez recommencer !")
        except ValueError:
            print("veuillez rentrer un chiffre !")
    play(cartes[gameMap-1])
