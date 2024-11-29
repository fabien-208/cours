class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_maximum(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val


def cherche(node, value):
    current = node
    if current.val == value:
        return True
    else:
        if current.val < value and current.left != None:
            cherche(current.left)
        if current.val > value and current.right != None:
            cherche(current.right)
    return False


def estABR(self):
    if self.__racine ==None:
        return True
    f = file()
    f.ajouter(self.__racine)
    while not f.est_vide():
        sommet = f.supprimer()
        maxG, minD = sommet.get(), sommet.get()
        if sommet.afg():
            f.ajouter(sommet.fg())
            maxG = sommet.fg().maximum_rec()
        if sommet.afd():
            f.ajouter(sommet.fd())
            minD = sommet.fd().minimum_rec()
        
        if not (maxG <= sommet.get() <= minD):
            return False
        return True


def tri_arbre(l):
    abr = arbrebinaireR()
    for i  in range(len(l)):
        abr.ajouter(l[i])
    l2= abr.parcours_infixe()
    for i in range(len(l)):
        l[i] = l2[i]