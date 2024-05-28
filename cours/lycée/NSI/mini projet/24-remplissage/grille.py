import remplissage

Grille1 = remplissage.Grille('grille8.txt')

def remplissage(Grille, coordonnés=(0,0), valeur='.'):

    (x, y) = coordonnés

    if Grille.get(coordonnés) == ' ':
        contour = Grille.outil(coordonnés)
        Grille.set(coordonnés, valeur)

        for coordonnés in contour:
            remplissage(Grille, coordonnés, valeur)

    return Grille



def remplissage_tout(Grille, valeur):
    for y in Grille(self.__height):
        for x in Grille(self.__width):
            


Grille = remplissage(Grille1)
print(Grille1)