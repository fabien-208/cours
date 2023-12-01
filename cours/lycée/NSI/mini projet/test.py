#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Grille:
    """
    >>> g = Grille(3, 3)
    >>> g
    +----+----+----+
    | 1  | 2  | 3  |
    +----+----+----+
    | 4  | 5  | 6  |
    +----+----+----+
    | 7  | 8  | 9  |
    +----+----+----+
    >>> g.mouvement_possible()
    {'LEFT': (1, 2), 'UP': (2, 1)}
    >>> g.mouvement_possible().values()
    dict_values([(1, 2), (2, 1)])
    >>> list(g.mouvement_possible().values())
    [(1, 2), (2, 1)]
    >>> random.seed(2022)
    >>> random.choice(list(g.mouvement_possible().values()))
    (2, 1)
    >>> g.mouvement((2, 1))
    >>> g
    +----+----+----+
    | 1  | 2  | 3  |
    +----+----+----+
    | 4  | 5  | 9  |
    +----+----+----+
    | 7  | 8  | 6  |
    +----+----+----+
    >>> list(g.mouvement_possible().values())
    [(1, 1), (2, 0), (2, 2)]
    >>> g.mouvement((2, 0))
    >>> g
    +----+----+----+
    | 1  | 2  | 9  |
    +----+----+----+
    | 4  | 5  | 3  |
    +----+----+----+
    | 7  | 8  | 6  |
    +----+----+----+
    >>> list(g.mouvement_possible().values())
    [(1, 0), (2, 1)]
    >>> g.zero
    (2, 0)
    >>> g.melange(1235)
    >>> g
    +----+----+----+
    | 1  | 4  | 5  |
    +----+----+----+
    | 9  | 6  | 3  |
    +----+----+----+
    | 8  | 7  | 2  |
    +----+----+----+
    >>> g.place_en_bas_droite()
    >>> g
    +----+----+----+
    | 1  | 4  | 5  |
    +----+----+----+
    | 6  | 3  | 2  |
    +----+----+----+
    | 8  | 7  | 9  |
    +----+----+----+
    """
    
    def __init__(self, width, height, valeurs=None):
        
        self.width = width
        self.height = height
        self.zero = (width - 1, height - 1)
        self.grille = []

        valeurs = valeurs or list(range(1, width * height + 1))

        while valeurs:
            ligne = []
            for _ in range(height):
                ligne.append(valeurs.pop(0))
            self.grille.append(ligne)

    def __repr__(self) -> str:
        

        g = ""
        for i in range(self.width):
            g += "+----" * self.height + "+\n"
            for j in range(self.height):
                g += f"| {self.grille[i][j]:^2} "
            g += "|\n"
        g += "+----" * self.height + "+"
        return g

    def est_dans_grille(self, abscisse, ordonnée):
        
        return 0 <= abscisse < self.width and 0 <= ordonnée < self.height

    def mouvement_possible(self):
        
        directions = {
            "LEFT": (self.zero[0] - 1, self.zero[1]),
            "RIGHT": (self.zero[0] + 1, self.zero[1]),
            "UP": (self.zero[0], self.zero[1] - 1),
            "DOWN": (self.zero[0], self.zero[1] + 1),
        }

        mouvements = {}
        for direction, point in directions.items():
            if self.est_dans_grille(point[0], point[1]):
                mouvements[direction] = point

        return mouvements

    def mouvement(self, point):
        
        case_point = self.grille[point[1]][point[0]]
        case_zero = self.grille[self.zero[1]][self.zero[0]]

        self.grille[self.zero[1]][self.zero[0]] = case_point
        self.grille[point[1]][point[0]] = case_zero

        self.zero = point

    
    
    def melange(self, count):
        
        i = 0
        while i < count:
            mouvements = self.mouvement_possible()
            mouvement = random.choice(list(mouvements.values()))
            self.mouvement(mouvement)
            i += 1

    def place_en_bas_droite(self):

        while self.zero[0] != (self.width - 1):
            self.mouvement((self.zero[0] + 1, self.zero[1]))
        while self.zero[1] != (self.height - 1):
            self.mouvement((self.zero[0], self.zero[1] + 1))

    def est_dans_l_ordre(self):
    
        for i in range(self.width):
            for j in range(self.height):
                if self.grille[i][j] != (i + 1) + j * self.width:
                    return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
