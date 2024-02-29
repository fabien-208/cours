class caractere:

    def __init__(self, nom, nb_lig = 8, nb_col = 16) -> None:
        """
        >>> car = caractere('A')
        >>> car.valeur_pixel(0, 0)
        0
        >>> car2 = caractere('Z')
        >>> car.nb_pix_diff(car2)
        0
        """
        self.__liste = []
        self.__nom = nom
        self.nb_lig = nb_lig
        self.nb_col = nb_col
        for i in range(self.nb_col):
            for j in range(self.nb_lig):
                self.__liste.append(0)
    


    def valeur_pixel(self, l:int, c:int):
        return self.__liste[(8*l + c)]
    

    def nb_pix_diff(self, carac) ->int:
        diff = 0
        for i in range(self.nb_lig):
            for j in range(self.nb_col):
                if self.valeur_pixel(i*8, j) != carac.valeur_pixel(i*8, j):
                    diff += 1
        return diff
    


    def carac_egaux(self, carac):
        if self.nb_pix_diff(carac) == 0:
            return True
        return False
    


if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose=True)