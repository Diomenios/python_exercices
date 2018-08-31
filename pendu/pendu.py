#!/usr/local/bin/python3.6
#! -*-coding:Utf-8 -*

import donnee
import fonctions
import os

play = 'o'
playerName = fonctions.getPlayerName()
life = donnee.chanceMax
scores = fonctions.getScore()

if playerName not in scores.keys() :
    scores[playerName] = 0

while play != 'n' :
    motChoisi = fonctions.gotWord()
    lettreTrouvee = []
    motRetour = fonctions.returnMotCache(motChoisi, lettreTrouvee)

    print("bienvenu dans ce jeu de pendu, pour commencer " \
    + "votre nombre de chances avant le game over est de : {} \n".format(donnee.chanceMax))

    while life > 0 and motRetour != motChoisi :
        print("Voici l'état actuel du mot que vous cherchez : {} \n".format(motRetour))
        print("Voici vos lettres trouvées : {} \n".format(lettreTrouvee))
        lettre = fonctions.getALetter()
        if lettre in lettreTrouvee :
            print("erreur, vous avez déjà essayer cette lettre veuillez réessayer ! \n")
        else :
            lettreTrouvee.append(lettre)
            if lettre in motChoisi :
                print("Félicitation la lettre se trouvait dans le mot ! \n")
                motRetour = fonctions.returnMotCache(motChoisi, lettreTrouvee)
            else :
                life -= 1
                print("Echec, cette lettre n'était pas dans le mot !\n")
                print("Il vous reste {} vie(s) \n".format(life))

    if life == 0 :
        print("Game over : vus avez perdu toutes vos vies !\n")
        play = False
    else :
        scores[playerName] += life
        print ("{} votre score vaut maintenant {} \n".format(playerName, scores[playerName]))
        play = input("voulez vous continuer à jouer ? (O/N) \n")
        play = play.lower()

fonctions.saveScore(scores)

print("vous finissez la partie avec un score de {} \n".format(scores[playerName]))
