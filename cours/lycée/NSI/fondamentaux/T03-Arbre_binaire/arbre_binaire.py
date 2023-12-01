#title: Fondamentaux - Arbre binaire



#🛠 Le nœud racine
#"+"
#🛠 La ou les feuille·s
#"4;2;5"
#🛠 Le ou les fils du nœud '+'
#"*;5"
#🛠 si c'est un arbre binaire
#oui, c est un arbre binaire

class Binary_tree():
    """
    >>> BT = Binary_tree()
    >>> BT
    ()
    >>> BT('E1')
    (E1)
    >>> BT('E1', BT('G'), BT('D'))
    E1:[(G), (D)]
    >>> BT('+', BT('*', BT('4'), BT('2')), BT('5'))
    (+:[(*:[(4), (2)]), (5)]
    """
    def __init__(self, *args):
        CLS = type(self)
        etiquette = None
        left = None
        right = None

        if len(args) > 3:
            raise TypeError("Nombre d'argument incorrect")
   
        if len(args) > 0:
            etiquette = args[0]
            if not isinstance(etiquette, str):
                raise TypeError("L'étiquette doit être de type <str>")

        if len(args) > 1:
            left = args[1]
            if left is not None and not isinstance(left, CLS):
                msg = "Le nœud left doit etre de type {}".format(CLS)
                raise TypeError(msg)

        if len(args) == 3:
            right = args[2]
            if right is not None and not isinstance(right, CLS):
                msg = "Le nœud right doit etre de type {}".format(CLS)
                raise TypeError(msg)

        if etiquette is not None:
            if left == None:
                left = CLS()
            if right == None:
                right = CLS()

        self.__data = (etiquette, left, right)
    
    def est_vide(self):
        return self.etiquette == None

    def est_une_feuille(self):
        return self.left == None and self.right == None
    
    def __str__(self):
        if self.est_vide == None:
            return '()'
        if self.est_une_feuille == None:
            return
        
    





if __name__ == __name__:
    import doctest
    doctest.testmod(verbose=True)

