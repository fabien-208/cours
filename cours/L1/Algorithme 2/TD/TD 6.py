# exerice 1

class caractere:

    def __init__(self, nom:str, pix=None, nb_lig:int = 8, nb_col:int = 16) -> None:
        """
        >>> car = caractere('A')
        >>> car.get_pixel(0, 0)
        0
        >>> car2 = caractere('Z')
        >>> car.comparaison_pix(car2)
        0
        >>> car.carac_egaux(car2)
        True
        """
        self.__pixel = pix
        self.__nom = nom
        self.__nb_lig = nb_lig
        self.__nb_col = nb_col
        if self.__pixel ==None:
            self.__pixel = []
            for i in range(self.__nb_col):
                for j in range(self.__nb_lig):
                    self.__pixel.append(0)
        
    def nom(self) -> str:
        return self.__nom
    
# exercice 2

    def get_pixel(self, l:int, c:int):
        if l <= self.__nb_lig:
            return self.__pixel[(self.__nb_lig*l + c)]
    
# exercice 3

    def comparaison_pix(self, carac) ->int:
        diff = 0
        for i in range(self.__nb_lig):
            for j in range(self.__nb_col):
                if self.get_pixel(i*self.__nb_lig, j) != carac.get_pixel(i*self.__nb_lig, j):
                    diff += 1
        return diff
    
# exercice 4

    def carac_egaux(self, pixels)-> bool:
        if self.comparaison_pix(pixels) == 0:
            return True
        return False
    
# exercice 5

    def carac_proche(self, pixels)-> bool:
        if self.comparaison_pix(pixels) < (5*(self.__nb_lig*self.__nb_lig+ self.__nb_col))/100:
            return True
        return False

# exercice 6
    

    def retourne_carac_proche(self, alphabet):
        car = []
        for i in range(len(alphabet)):
            if self.carac_egaux(alphabet[i]) == True or self.carac_proche(alphabet[i]) == True:
                car.append(alphabet[i].nom())

        return car
    


if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose=True)