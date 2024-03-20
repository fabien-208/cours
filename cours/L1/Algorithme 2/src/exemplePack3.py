# -*- coding: utf-8 -*-
# une première application graphique
import tkinter
import random

class VueSphere :
    '''Classe qui définit et met en place une interface graphique.
    On y affiche une image de sphère.
    '''
    
    def __init__(self):
        '''Vue, str -> Vue
        construit l'interface graphique et la lance.
        '''
        # première chose, créer la fenetre principale
        fenetre = tkinter.Tk()
        fenetre.title("Sphere")

        # on créé les images : elles sont mémorisées dans un objet PhotoIma
        largeur = img[0].width()+1
        hauteur = img[0].height()

        # le composant graphique qui contient les images est un canevas
        # ce composant appartient à la fenetre principale
        can_image = tkinter.Canvas(fenetre, width=2*largeur,height=hauteur)
        for i in  range(2) :
            ind = random.randint(0,len(img)-1)
            can_image.create_image(i*largeur,0,anchor=tkinter.NW,image=img[ind])
        can_image.pack()
        

        # le deuxième composant est un Button
        # il appartient également à la fenetre principale
        # un clic sur le bouton fait quitter l'appli
        btn_quitter = tkinter.Button(fenetre,
                            text="Au revoir",
                            command = fenetre.destroy)
        btn_quitter.pack()
        
        # on lance la boucle d'écoute des événements
        fenetre.mainloop()

### fin de la classe Vue


### script principal
if __name__ == '__main__' :
    mon_appli = VueSphere()

