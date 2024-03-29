# exercice 1

from pickle import FALSE


def retirer_max(p):
    pile = Pile()
    if len(p) == 0:
        return None
    max = p.pop()
    while len(pile) != 0:
        elt = p.pop()
        if elt > max:
            pile.push(max)
            max = elt
        else:
            pile.pop(elt)
    while len(pile) != 0:
        p.push(pile.pop())
    return max



# exercice 2

def inverse_der_prem(mafile):
    last = mafile.pop()
    file = File()
    while not mafile.est_vide():
        elt = mafile.pop()
        if mafile.est_vide():
            first = elt
        else:
            file.push(elt)
    mafile.push(first)
    while not file.est_vide():
        mafile.push(file.pop())
    mafile.push(last)




class filecinema:

    def __init__(self) -> None:
        self.__file = []

    def est_vide(self):
        return len(self.__file) == 0
    
    def ajoute(self, n:int)->None:
        fait = False
        for i in range(len(self.__file)):
            if self.__file[i][0] == n:
                self.__file[i] = (self.__file[i][0], self.__file[i][1] + 1)
                return None
            if not fait:
                self.__file.append((n, 1))

    def enleve(self):
        return self.__file.pop(0)
    
def ouvreguichet(file, nb_place):
    nb_place2 = nb_place
    while nb_place != 0:
        if file[len(file)][1] <= nb_place:
            nb_plaace -= file[len(file)][1]
            file.pop(len(file))
        else:
            pass
    return nb_place2 - nb_place
        



def ouvre_guichet(file, nb_place):
    nb_place2 = nb_place
    while not file.est_vide():
        pers = file.enleve()
        if pers <= nb_place:
            nb_place -= pers
        return nb_place2 -nb_place
