import random

class proposition:

    def __init__(self, code:list) -> None:
        """
        >>> p = proposition([1,2,3,4])
        >>> p.calcule_bp_mp([1, 5, 0, 4])
        (2, 0)
        >>> p.calcule_bp_mp([3, 4, 2, 5])
        (0, 3)
        >>> p.calcule_bp_mp([1, 2, 4, 3])
        (2, 2)
        >>> p.calcule_bp_mp([1, 2, 3, 4])
        (4, 0)
        >>> p.calcule_bp_mp([1, 1, 1, 1])
        (1, 0)
        """
        self.code = code


    def calcule_bp_mp(self, code:list[int]):
        bp = 0
        mp = 0
        gtj = []
        bb = self.code
        for i in range(len(self.code)):
            if code[i] == self.code[i]:
                bp += 1
            else:
                gtj.append(self.code[i])
        for k in range(len(gtj)):
            if gtj[k] in code:
                mp += 1
        return bp, mp
    

    def __str__(self):
        print(self.code)
            


class Mastermind:

    def __init__(self, nb_couleur = 6, len_code = 4) -> None:
        """
        >>> mast = Mastermind
        >>> mast.bp_mp([3, 2, 1, 4])
        >>> mast.bp_mp([5, 0, 1, 3])
        """
        self.__nb_couleur = nb_couleur
        self.__taille_code = len_code
        self.__mystere = proposition(self.lancer())


    def dim(self):
        return self.__taille_code
    

    def lancer(self):
        iri = []
        for i in range(self.__taille_code):
            iri.append(random.randint(0, self.__nb_couleur))
        return iri


    def bp_mp(self, code:list[int]):
        self.__mystere.calcule_bp_mp(code)


if '__main__' == __name__:
    import doctest
    doctest.testmod(verbose=True)

