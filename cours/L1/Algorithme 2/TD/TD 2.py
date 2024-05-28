class domino():
    
    def __init__(self, A=0, B=0):
        self.A = A
        self.B = B
        
    def valeur(self):
        return self.A + self.B
    
    
    def renverse(self):
        self.A, self.B = self.B, self.A
        
    def str(self):
        return("'[{}|{}]'".format(self.A, self.B))
        
    
    def affiche(self):
        print(self.str())


def affiche_dominos(liste):
    """
    >>> d1 = domino(3, 5)
    >>> d2 = domino(4, 2)
    >>> affiche_dominos([d1, d2])
    '[3|5]' - '[4|2]'

    """
    print(' - '.join(domino.str() for domino in liste))




def nbre_points(liste):
    """
    >>> d1 = domino(3, 5)
    >>> d2 = domino(4, 2)
    >>> nbre_points([d1, d2])
    14
    """
    point = 0
    for elt in liste:
        point += elt.valeur()
    return point



def cree_jeu_domino():
    """
    >>> l = cree_jeu_domino()
    >>> affiche_dominos(l)
    '[0|0]' - '[1|0]' - '[2|0]' - '[3|0]' - '[4|0]' - '[5|0]' - '[6|0]' - '[1|1]' - '[2|1]' - '[3|1]' - '[4|1]' - '[5|1]' - '[6|1]' - '[2|2]' - '[3|2]' - '[4|2]' - '[5|2]' - '[6|2]' - '[3|3]' - '[4|3]' - '[5|3]' - '[6|3]' - '[4|4]' - '[5|4]' - '[6|4]' - '[5|5]' - '[6|5]' - '[6|6]'
    >>> nbre_points(l)
    168
    """
    liste = []
    for i in range(7):
        for j in range(i, 7):
            liste.append(domino(j, i))
    return liste
            


         
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
    