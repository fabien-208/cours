

class demineur:

    def __init__(self, nb_llgne = 10, nb_colonne = 20) -> None:
        """
        >>> dem = demineur()
        >>> dem.affiche_ligne()
        
        """
        self.__nb_ligne = nb_llgne
        self.__nb_colonne = nb_colonne
        self.plateau = []
        
        for i in range(self.__nb_colonne):
            cs = []
            for j in range(self.__nb_ligne):
                cs.append(Case())
            self.plateau.append(cs)


        
        def affiche_plateau(self):
            pass

        def affiche_ligne(self):
            ls = '+'
            for elt in self.plateau:
                for i in range(len(elt)):
                    ls += '--+'
            return ls
        






if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    