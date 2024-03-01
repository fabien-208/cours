
class pile:

    def __init__(self, pile:list) -> None:
        """
        >>> lsit = [1, 2, 3, 4]
        >>> pil = pile(lsit)
        >>> pil.aff_pile()
        [1, 2, 3, 4]
        >>> pil.push(5)
        >>> pil.aff_pile()
        [1, 2, 3, 4, 5]
        >>> pil.pop()
        5
        >>> pil.aff_pile()
        [1, 2, 3, 4]
        """
        self.__pile = pile

    def aff_pile(self):
        return self.__pile

    def push(self, carte):
        self.__pile.append(carte)


    def pop(self):
        g = self.__pile[-1]
        del(self.__pile[-1])
        return g
    


    def separe_couleur(self):
        pass



if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose = True)