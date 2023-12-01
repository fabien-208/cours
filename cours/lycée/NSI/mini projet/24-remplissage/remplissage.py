#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Grille():
    
    "Classe pour implémenter une grille ascii art"

    def __init__(self, filename):
        self.__grille = self.__read_grille(filename)
        self.__height = len(self.__grille)
        self.__width = len(self.__grille[0])

    def __read_grille(self, filename):
        
        """Renvoie une liste des lignes du fichier"""
        
        data = []
        with open(filename, encoding="UTF-8") as fichier:
            for line in fichier:
                data.append(line.strip('\n'))
        return data

    def __str__(self):
        chaine = ''
        for ligne in self.__grille:
            chaine += '{}\n'.format(ligne)
        return chaine

    def __getitem__(self, index):
        
        "Retourne la valeur de objet[index]"
        
        return self.__grille[index]

    def __in_grille(self, case):
        
        """Renvoie True si case est dans la grille"""
        
        (x, y) = case
        test = True

        if y < 0 or y >= self.__height:
            test = False
        elif x < 0 or x >= len(self.__grille[y]):
            test = False
        return test

    def __len__(self):
        return self.__height

    def get(self, case):
        
        "Renvoie le contenu de la case"
        
        if not self.__in_grille(case):
            raise IndexError("Out of the range")
        (x, y) = case
        return self.__grille[y][x]

    def set(self, case, value):
        
        "Modifie le contenu de la case"

        if not self.__in_grille(case):
            raise IndexError("Out of the range")
        (x, y) = case
        ligne = list(self.__grille[y])
        ligne[x] = value
        self.__grille[y] = ''.join(ligne)

    def outil(self, case, value=' '):
        data = []
        offset = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        (x, y) = case
        if not self.__in_grille(case):
            raise IndexError("Out of the range")
        for (dx, dy) in offset:
            n = (x + dx, y + dy)
            if self.__in_grille(n):
                if self.get(n) == value:
                    data.append(n)
        return data



