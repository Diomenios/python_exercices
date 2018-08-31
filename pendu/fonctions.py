#!/usr/local/bin/python3.6
#! -*-coding:Utf-8 -*

from donnee import *
from random import choice
import os
import pickle

def gotWord():
    """This function return a random word from a list of word"""
    try :
        return choice(dictionnaire)
    except IndexError :
        print("error the list is empty !")

def saveScore(score) :
    """This function save the dictionnary of scores in a byteFile name 'score' """
    scoreFile = open("scores", "wb")
    MonPickler = pickle.Pickler(scoreFile)
    MonPickler.dump(score)
    scoreFile.close

def getScore() :
    """This function return a score dictionnary from the byteFile 'score' """
    if os.path.exists("scores") :
        scoreFile = open("scores", "rb")
        monDepickler = pickle.Unpickler(scoreFile)
        scores = monDepickler.load()
        scoreFile.close
    else :
        scores = {}
    return scores

def getPlayerName():
    playerName = input("veuillez introduire votre nom d'utilisateur : ")
    playerName = playerName.capitalize() #permet de mettre la première lettre en majuscule et les autres en minuscules

    if not playerName.isalnum() or len(playerName)<4 :
        print("ce nom n'est pas valide veuillez recommencer ! \n")
        return getPlayerName()
    else :
        return playerName

def getALetter():
    lettre = input("insérez la lettre que vous souhaitez essayer : ")
    lettre =  lettre.lower()
    if len(lettre)>1 or not lettre.isalpha() :
        return getALetter()
    else :
        return lettre

def returnMotCache(mot, lettreTrouvee) :
    mot_masque = ""
    for lettre in mot :
        if lettre in lettreTrouvee :
            mot_masque += lettre
        else :
            mot_masque += "*"

    return mot_masque
