
class pile:

    def __init__(self, pile:list) -> None:
        """
        
        """
        self.__pile = pile

    def aff_pile(self):
        return self.__pile

    def push(self, carte):
        self.__pile.append(carte)


    def pop(self):
        if len(self.__pile) == 0:
            return None
        return self.__pile.pop()
    
    def __len__(self):
        return len(self.__pile)


def vider_couleur(pile, couleur, pile2):
    for i in range(pile.__len__(), 0, -1):
        if pile.__pile[i].couleur() == couleur:
            pile2.push(pile.__pile[i])
            pile.pop()
        else:
            break




if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose = True)