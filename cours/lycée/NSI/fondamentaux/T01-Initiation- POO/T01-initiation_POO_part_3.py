#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tableau

class Pile():
    """
    Implémentation d'une pile avec un tableau
    """

    def __init__(self, size_def=10, type_def=int):
        self.__data = tableau.Tab(size_def, type_def)
        self.__sp = 0  # Pointeur sur le prochain élément
        self.__count = 0  # Taille de la pile


    def is_empty(self):
        "Renvoie Vrai si la pile est vide"
        return self.__count == 0

    def __last(self):
        "Renvoie le dernier élément sans le dépiler"
        if not self.is_empty():
            return self.__data[self.__sp - 1]

    def __repr__(self):
        "Affichage de la pile"
        return "P :[{}]".format(self.__last())

    def __str__(self):
        return repr(self)


    def push(self, element):
        """Empile l'element à la pile

        >>> p=Pile()
        >>> p.is_empty()
        True
        >>> p.push(314)
        >>> p.is_empty()
        False
        """
        self.__data[self.__sp] = element
        self.__sp += 1
        self.__count += 1 

    def pop(self):
        """Dépile le dernier élément

        >>> p=Pile()
        >>> p.push(314)
        >>> p.push(1024)
        >>> p.push(2021)
        >>> p.pop()
        2021
        >>> p.pop()
        1024
        >>> p.pop()
        314
        """
        print(self.__data[self.__sp-1])
        self.__sp -= 1
        self.__count -= 1 




class File():
    """
    implémentation d'une file dans un tableau
    """

    def __init__(self, size_def=10, type_def=int):
        self.__data = tableau.Tab(size_def, type_def)
        self.__sp = 0  # Pointeur sur le prochain élément
        self.__count = 0

    def is_empty(self):
        "Renvoie Vrai si la pile est vide"
        return self.__count == 0

        



if __name__=="__main__":
    import doctest
    doctest.testmod(verbose = True)