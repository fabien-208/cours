#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
un vecteur est definie par :
-une abscisse
-une ordonnée
"""

class Vec():
    """
    >>> v1 = Vec(2, 3)
    >>> v1
    V(2, 3)
    >>> v2 = Vec(-2, 3)
    >>> v3 = Vec(-2, -3)
    >>> v1 + v2   # Utilisation de la méthode __add__
    V(0, 6)
    >>> v1*2    # Utilisation de la méthode __mul__
    V(4, 6)
    >>> v1*0
    V(0, 0)
    >>> v1.iscol(v2)  # v1 est-il colinéaire à v2 ?
    False
    >>> v1.iscol(v3)
    True
    >>> abs(Vec(3, 4)) # Utilisation de la méthode __abs__
    5.0
    """
    
    def __init__(self,x, y):
        """
        Création de l'objet point:
        :x float: abscisse
        :y float: ordonnée
        usage : obj(1, 4)
        """
        if not isinstance(x, (int, float)):
            raise TypeError('x doit être un int ou float')
        if not isinstance(y, (int, float)):
            raise TypeError('y doit être un int ou float')
        self.__x = x
        self.__y = y


    def __x(self):
        "Retourne l'abscisse du point"
        return self.__x
    
    x = property(fget=__x)

    def __y(self):
        "Retourne l'ordonnée du point"
        return self.__y
    
    y = property(fget=__y)
    
    def __repr__(self):
        return 'V({}; {})'.format(str(self.__x), str(self.__y))

    def __add__(self, other):
        return (self.x + other.x, self.y+ other.y)
    
    def __mul__(self, n):
        return (self.x* n, self.y* n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)