
# Exercice 1

class compte_bancaire:
    
    def __init__(self, nom, solde=1000):
        """
        >>> compte1 = compte_bancaire('Michu', 800)
        >>> compte1.depot(350)
        >>> compte1.retrait(200)
        >>> compte1.affiche()
        le solde du compte bancaire de Michu est de 950 euros
        """
        self.nom = nom
        self.solde = solde
        
        
        
    def depot(self, somme):
        self.solde += somme
        
    
    def retrait(self, somme):
        self.solde -= somme
        
    def affiche(self):
        print('le solde du compte bancaire de {} est de {} euros'.format(self.nom, self.solde))
        
        
# Exercice 2

class voiture:
    def __init__(self, nom, couleur, vitesse=0, tu=None):
        """
        >>> voitu = voiture('ede', 'rouge')
        >>> voitu.accelere(60)
        >>> print(voitu.vitesse)
        60
        >>> voitu.freine(49)
        >>> print(voitu.vitesse)
        11
        >>> print(voitu.str())
        ['ede', 'rouge', 11]
        >>> voitu.affiche()
        la voiture s'apelle ede, elle est de couleur rouge et sa vitesse est de 11 km/h
        """
        self.nom = nom
        self.couleur = couleur
        self.vitesse= vitesse
        self.tu = tu
        
    
    def accelere(self, inc):
        while inc >= 10:
            if self.vitesse < 130:
                self.vitesse += 10
                inc -= 10
            else:
                break
        if self.vitesse < 130:
            self.vitesse += inc
        
        
    def freine(self, dec):
        if dec >= self.vitesse:
            self.vitesse = 0
        else:
            self.vitesse -= dec
        
        
    def str(self):
        self.tu=[self.nom, self.couleur, self.vitesse]
        return self.tu
        
        
        
    def affiche(self):
        print("la voiture s'apelle {}, elle est de couleur {} et sa vitesse est de {} km/h".format(self.nom, self.couleur, self.vitesse))
    

                
# Exercice 3

# Question 1

import random 

class Carte:
    def __init__(self):
        """
        >>> ch = Carte
        >>> ch.affiche()
        """
        
        coul = ['trèfle', 'carreau', 'coeur', 'pique']
        haut = [7,8,9,'Valet','Dame', 'Roi', 10, 'As']
        point = [0, 0, 0, 2, 3, 4, 10, 11]
        atout = [7, 8, 'Dame', 'Roi', 10, 'As', 9, 'Valet']
        point_atout = [0, 0, 0, 2, 3, 4, 14, 20]
        ch_coul = random.randint(0,len(coul))
        ch_haut = random.randint(0, len(haut))
        
        self.couleur = coul[ch_coul]
        self.hauteur = haut[ch_haut]
        self.nb_point = point[ch_haut]
        
        
    def affiche(self):
        print('{} de {}'.format(self.hauteur, self.couleur))

    def cou():
        pass
                
    
if '__main__' ==__name__:
    import doctest
    doctest.testmod(verbose=True)
                