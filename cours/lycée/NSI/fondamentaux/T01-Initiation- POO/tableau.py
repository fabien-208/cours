#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Introduction à la programmation orintée objet

 *Réalisation d'une classe tableau*

"""


class Tab():
    """
>>> Tab(-1)
Traceback (most recent call last):
    ...
ValueError: La taille du tableau doit être un entier > 0

>>> t=Tab(3)
>>> t
<class 'int'>:<None, None, None>

>>> t[0] = 5
>>> t
<class 'int'>:<5, None, None>

>>> t[3]
Traceback (most recent call last):
    ...
ValueError: Index out of range

>>> t[2] = 3.14
Traceback (most recent call last):
    ...
TypeError: La valeur n'est pas du bon type

"""
    def __init__(self, size, types=int):
        """
        Création de l'objet tableau par défaut de type int
        usage : Tab(size) , Tab(size, int), Tab(size, str)

        size (int) > 0
        """

        if not isinstance(size, int) or size < 1:
            raise ValueError('La taille du tableau doit être un entier > 0')
        self.__valeurs = [None for _ in range(size)]
        self.__size = size
        self.__types = types

    def __getitem__(self, index):
        "Retourne la valeur de objet[index]"
        if not isinstance(index, int):
            raise ValueError('Index not type int')
        if index >= self.__size or index < 0:
            raise ValueError('Index out of range')
        return self.__valeurs[index]

    def __len__(self):
        "Retourne la taille du tableau"
        return self.__size

    def __setitem__(self, index, value):
        "Affecte la valeur : objet[index] = value"
        if not isinstance(index, int):
            raise ValueError('Index not type int')
        if index >= self.__size or index < 0:
            raise ValueError('Index out of range')

        if not isinstance(value, self.__types):
            raise TypeError("La valeur n'est pas du bon type")
        self.__valeurs[index] = value

    def __repr__(self):
        chaine = ['{}, '.format(k) for k in self.__valeurs]
        chaine = ''.join(chaine)[:-2]
        return '{}:<{}>'.format(self.__types, chaine)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
