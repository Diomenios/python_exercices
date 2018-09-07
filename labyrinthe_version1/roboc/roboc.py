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

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

#todo effacer les 2 lignes ci-dessous
#for i,carte in enumerate(cartes):
#    carte.labyrinthe.affiche_labyrinthe()

# On verifie si une sauvegarde a ete trouvee
gameSave = False
if save != None:
    print("une sauvegarde a été trouvée")
    while True :
        retour = input("voulez-vous charger la sauvegarde ?(n\o)")
        if retour.lower() == 'o':
            gameSave = True
            #todo effacer le dossier de la sauvegarde et effacer le print ci-dessous
            print("chargement de la partie")
            break
        elif retour.lower() == 'n':
            break
        else :
            print("votre entrée est incorrecte veuillez recommencer !")

gameMap = None
if gameSave:
    print("load the savefile")
    # todo ecrire le code chargeant la sauvagarde.
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

    #todo launch the game with gameMap
