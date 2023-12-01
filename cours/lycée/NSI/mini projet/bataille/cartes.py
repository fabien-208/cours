#!/usr/bin/env python3
# -*- coding : utf-8 -*-

"""
Simulateur de jeu de 52 cartes
"""
couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

from random import randrange
import random


class JeuDeCartes():

    def __init__(self, nom, couleur):
        """Construction du jeu de carte"""
        if nom in noms:
            self.nom = nom
            self.valeur = valeurs[nom]
        else:
            print("erreur de nom")
        if couleur in couleurs:
            self.couleur = couleur
        else:
            print("erreur de couleur")

    def creer_jeu_52(self):
        """ Permet de céer un jeu de 52 cartes"""
        for couleur in couleurs:
            for nom in valeurs:
                if (self.nbCartes == 32 and nom not in ['2','3','4','5','6']):
                    self.jeu.append(nom, couleur)
                if (self.nbCartes == 52):
                    self.jeu.append(nom, couleur)

    def nomCarte(self, c):
        """Renvoie le nom de la carte (<c> doit être un tuple !!!)"""
        return "%s de %s" (self.valeur[c[0]], self.couleur[c[1]])

    def battre(self):
        """Mélange les cartes"""
        a = 0
        b = len(self.jeu)
        while a < randrange(100, 200):
            i = randrange(b)
            n = randrange(b)
            self.jeu[i], self.jeu[n] = self.jeu[n], self.jeu[i]
            a = a + 1


    def tirer(self):
        """Retire une carte du jeu"""
        t = len(self.jeu)
        if t >0:
            carte = self.jeu[0]
            del(self.jeu[0])
            return carte
 

    def nb_cartes(self):
        """ compte le nombre de cartes dans le paquet"""
        return len(self.jeu_carte)


def sep():
    print()
    print('-*-'*15)
    print()


if __name__ == "__main__":
    # Initialisation de la classe « JeuDeCartes »
    jeux = JeuDeCartes()
    print(jeux.cartes)

    # Affichage du nom de la carte
    sep()
    jeux = JeuDeCartes()
    jeux.nomCarte((1, 2))
    jeux.nomCarte((12, 1))

    # Battre les cartes
    sep()
    jeux = JeuDeCartes()
    jeux.creer_jeu_52()
    jeux.battre()
    print(jeux.cartes)

    # Tirer une carte
    sep()
    print(' TIRER UNE CARTE ')
    random.seed(2022)
    jeux = JeuDeCartes()
    jeux.creer_jeu_52()
    jeux.battre()
    print(jeux.cartes[0])
    c = jeux.tirer()
    print(jeux.cartes[0])
    print(jeux.nomCarte(c))

    # Tirage de toutes le cartes
    sep()
    jeux = JeuDeCartes()
    random.seed(2022)
    jeux.creer_jeu_52()
    jeux.battre()
    # A compléter

    # Q5 Simuler un jeu de bataille entre 2 joueurs (robots)

    # A compléter
