import random
class Modele:

    def __init__(self, nb_colonne:int = 12, nb_lignes:int = 12, coul:int = 6) -> None:
        """
        >>> mod = Modele()
        >>> mod.nb_lig()
        12
        >>> mod.nb_col()
        12
        >>> mod.nb_coul()
        6
        >>> print(mod)
        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11|
        ----------------------------------------------------
        0| 1 | 1 | 0 | 2 | 4 | 0 | 0 | 2 | 0 | 3 | 3 | 0 |
        ----------------------------------------------------
        1| 5 | 1 | 0 | 5 | 2 | 5 | 1 | 3 | 5 | 1 | 4 | 3 |
        ----------------------------------------------------
        2| 1 | 2 | 5 | 4 | 5 | 1 | 5 | 2 | 2 | 4 | 1 | 1 |
        ----------------------------------------------------
        3| 2 | 2 | 0 | 1 | 2 | 4 | 3 | 4 | 0 | 0 | 1 | 0 |
        ----------------------------------------------------
        4| 3 | 0 | 0 | 3 | 3 | 3 | 2 | 0 | 1 | 4 | 4 | 0 |
        ----------------------------------------------------
        5| 5 | 5 | 1 | 5 | 4 | 0 | 4 | 3 | 5 | 5 | 0 | 5 |
        ----------------------------------------------------
        6| 0 | 5 | 4 | 2 | 4 | 5 | 5 | 5 | 0 | 4 | 1 | 3 |
        ----------------------------------------------------
        7| 2 | 0 | 5 | 0 | 1 | 0 | 3 | 5 | 3 | 2 | 2 | 2 |
        ----------------------------------------------------
        8| 4 | 4 | 1 | 2 | 0 | 2 | 5 | 3 | 3 | 2 | 5 | 0 |
        ----------------------------------------------------
        9| 5 | 4 | 4 | 3 | 3 | 2 | 0 | 1 | 2 | 5 | 1 | 2 |
        ----------------------------------------------------
        10| 3 | 4 | 1 | 4 | 3 | 5 | 3 | 0 | 4 | 1 | 4 | 0 |
        ----------------------------------------------------
        11| 2 | 5 | 3 | 2 | 1 | 2 | 1 | 0 | 4 | 2 | 4 | 4 |
        ----------------------------------------------------
        >>> mod.valeur_couleur(0,9)
        3
        >>> mod.valeur_couleur(0,0)
        1
        >>> mod.choisit_couleur(0,9)
        >>> mod.valeur_couleur(0,0)
        3
        """
        self.__nb_colonne = nb_colonne
        self.__nb_ligne = nb_lignes
        self.__coul = coul
        self.__score = 0
        self.__jeu = self.init_jeu()

    def init_jeu(self):
        self.__score = 0
        plateau = []
        for i in range(self.__nb_colonne):
            lig = []
            for j in range(self.__nb_ligne):
                lig.append(Case(random.randint(0, self.__coul-1),False, i, j)) 
            plateau.append(lig)
        return plateau
    
    
    def score(self):
        return self.__score
    
    def nb_lig(self) -> int:
        return self.__nb_ligne
    
    def nb_col(self) -> int:
        return self.__nb_colonne
    
    def nb_coul(self) -> int:
        return self.__coul


    def valeur_couleur(self, l:int, c:int) -> int:
        return self.__jeu[l][c].coul()
    

    def choisit_couleur(self, c:int, l:int) -> None:
        self.__jeu[0][0] = self.__jeu[c][l]


    def reinit_jeu(self):
        self.__score = 0
        self.__jeu = self.init_jeu()

    def __str__(self) -> str:
        plateau = ' |'
        for i in range(self.__nb_colonne):
            plateau += (' {} |'.format(i))
        plateau += '\n'
        for l in range(self.__nb_ligne):
            for j in range(self.__nb_ligne):
                plateau += '----'
            plateau += '\n'
            plateau += ('{}'.format(l))
            for k in range(self.__nb_colonne):
                plateau+= ('| {} '.format(self.__jeu[l][k]))
            plateau += '\n'
        return plateau
    
    def pose_couleur(self, coul:int, i:int, j:int):
        self.__jeu[i][j].changer_coul(self)


    def partie_finie(self):
        coul = self.__jeu[0][0].coul()
        for i in range(self.nb_lig()):
            for j in range(self.nb_col()):
                if self.__jeu[i][j].coul() != coul:
                    return False
        return True


class Case:

    def __init__(self, couleur:int, touché:bool = False, l = 0, c = 0, ) -> None:
        self.__couleur  = couleur
        self.__coord = (l, c)
        self.__touché = touché
                


    def coul(self):
        return self.__couleur

    def coord(self):
        return self.__coord

    def val_touché(self):
        return self.__touché    

    def voisine(self, l, c):
        if l <= self.nb_lig() and c<= self.nb_col():
            return ((l, c + 1), (l + 1, c))
        if l >= self.nb_lig() and c<= self.nb_col():
            return ((l, c + 1), (l - 1, c))
        if l <= self.nb_lig() and c>= self.nb_col():
            return ((l, c - 1), (l + 1, c))
        if l >= self.nb_lig() and c>= self.nb_col():
            return ((l, c - 1), (l - 1, c))
        
        if l<= self.nb_lig():
            return ((l, c + 1), (l + 1, c-1), (l + 1, c))
        if c <= self.nb_col():
            return ((l, c + 1), (l + 1, c), (l-1,c))
        if l>= self.nb_lig():
            return ((l, c + 1), (l - 1, c-1), (l - 1, c))
        if c >= self.nb_col():
            return ((l, c - 1), (l + 1, c), (l-1,c))
        
        else:
            return ((l, c + 1),(l + 1, c),(l, c - 1),(l - 1, c))

    def changer_coul(self, coul):
        self.__couleur = coul

    def touché(self):
        self.__touché =True


if '__main__' == __name__:
    import doctest
    doctest.testmod(verbose=True)