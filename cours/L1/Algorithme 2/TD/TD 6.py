# exerice 1

class cartere:

    def __init__(self, nom:str, pix=[], nb_lig:int = 8, nb_col:int = 16) -> None:
        """
        >>> car = cartere('A')
        >>> car.get_pixel(0, 0)
        0
        >>> car2 = cartere('Z')
        >>> car.comparaison_pix(car2)
        0
        >>> car.car_egaux(car2)
        True
        """
        self.__pixel = pix
        self.__nom = nom
        self.__nb_lig = nb_lig
        self.__nb_col = nb_col
        if self.__pixel ==[]:
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

    def comparaison_pix(self, car) ->int:
        diff = 0
        for i in range(self.__nb_lig):
            for j in range(self.__nb_col):
                if self.get_pixel(i*self.__nb_lig, j) != car.get_pixel(i*self.__nb_lig, j):
                    diff += 1
        return diff
    
# exercice 4

    def car_egaux(self, pixels)-> bool:
        return self.comparaison_pix(pixels) == 0
    

# exercice 5

    def car_proche(self, pixels)-> bool:
        return self.comparaison_pix(pixels) < (5*(self.__nb_lig*self.__nb_lig+ self.__nb_col))/100

# exercice 6
    

    def retourne_car_proche(self, alphabet):
        car = []
        for i in range(len(alphabet)):
            if self.car_egaux(alphabet[i]) == True or self.car_proche(alphabet[i]) == True:
                car.append(alphabet[i].nom())
        return car
    


if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose=True)