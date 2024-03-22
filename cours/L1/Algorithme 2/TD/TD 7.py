
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

def separer_couleur_2(pile, pile2, pile3, pile4):
    for i in range(pile.__len__(), 0, -1):
        if pile[i].couleur == 'Coeur':
            pile2.push(pile[i])
            pile.pop()
        if pile[i].couleur == 'Careaux':
            pile3.push(pile[i])
            pile.pop()
        if pile[i].couleur == 'Pique':
            pile4.push(pile[i])
            pile.pop()

        
def separer_couleur(pile, pile2, pile3, pile4):
    dic = {'trefle': pile(), 'careau' : pile3, 'Coeur' : pile2, 'Pique':pile4}
    while(len(pile)) !=0:
        carte = pile.pop()
        dic[carte.couleur()].push(carte)
    while(len(dic['trefle'])) != 0:
        carte = dic['trefle'].pop()
        pile.push(carte)
    


def vider_plus_petit(carte, pile, pile2):
    while(len(pile)) != 0:
        car = pile.pop()
        if car.couleur == carte.couleur and car.hauteur > carte.hauteur:
            pile.push(car)
        else:
            break



def vider_plus_petit_2(carte, pile, pile2):
    for i in range(pile.__len___(), 0, -1):
        if pile[i].couleur == carte[0] and pile[i].hauteur > carte.hauteur:
            pile2.push(pile[i])
            pile.pop()
        else:
            break


def trier(pile):
    pile_min, mile_trier = pile(), pile()
    while len(pile) != len(pile_min):
        carte = pile.pop()
        while len(pile) != 0:
            car = pile.pop()
            if car.est_plus_grand(carte):
                carte, car = car, carte
            pile_min.push(car)
        mile_trier.push(carte)



if "__main__" == __name__:
    import doctest
    doctest.testmod(verbose = True)