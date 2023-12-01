#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Introduction à la programmation orientée objet

 *Réalisation d'une classe pour représenter un point à deux dimensions *

 Un point est définie par :

- un nom
- une abscisse
- une ordonnée

"""


class Point():
    """
    >>> Point(1, 1.2, 2)
    Traceback (most recent call last):
        ...
    TypeError: name doit être de type str

    >>> Point('A', '1.2', 2)
    Traceback (most recent call last):
        ...
    TypeError: x doit être un int ou float
    >>> p = Point("A", 5, 2)
    >>> print(p)
    A:(5; 2)
    >>> p.x()
    5
    >>> p.y()
    2
    >>> p.name()
    'A'
    """

    def __init__(self, name, x, y):
        """
        Création de l'objet point:

        :name str: Nom du point
        :x float: abscisse
        :y float: ordonnée
        usage : obj("A", 1, 4)
        """

        if not isinstance(name, str):
            raise TypeError('name doit être de type str')
        if not isinstance(x, (int, float)):
            raise TypeError('x doit être un int ou float')
        if not isinstance(y, (int, float)):
            raise TypeError('y doit être un int ou float')
        self.__x = x
        self.__y = y
        self.__name = name

    def x(self):
        "Retourne l'abscisse du point"
        return self.__x

    def y(self):
        "Retourne l'ordonnée du point"
        return self.__y

    def name(self):
        "Retourne le nom du point"
        return self.__name

    def __repr__(self):
        return '{}:({}; {})'.format(self.name(),
                                    str(self.x()),
                                    str(self.y()))

    def __str__(self):
        "Représentation du point"
        return str(self.__repr__())

    def distance(self, point):
        """
        retourne la distance entre le point
        >>> pt1 = Point('A', -1, -2)
        >>> pt2 = Point('A', 2, 2)
        >>> print(pt1.distance(pt2))
        5.0
        """
        import math
        dx = self.x() - point.x()
        dy = self.y() - point.y()
        return math.sqrt(dx**2 + dy**2)

    def coordo(self):
        """Retour les coordonnées du point : (x; y)
        
        >>> p1 = Point('A', 1, 2)
        >>> p1.coordo()
        '(1, 2)'
        """
        return (self.x(), self.y())

    def __eq__(self, other):
        """Retourne True si l'objet self est égal à l'objet other
        
        >>> p1 = Point('A', 1, 2)
        >>> p2 = Point('B', -1, 2)
        >>> p3 = Point('C', 1, 2)
        >>> p1 == p2
        False
        >>> p1 == p3
        True
        """
        return self.coordo() == other.coordo()
    
    def __x(self):
        """retourne la valeur de x"""
        return self.__x

    x = property(fget=__x)
    
    def __y(self):
        """retourne la valeur de y"""
        return self.__y
    
    y = property(fget=__y)
    
    def __name(self):
        """retourne la valeur de name"""
        return self.__name
    
    name = property(fget=__name)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


