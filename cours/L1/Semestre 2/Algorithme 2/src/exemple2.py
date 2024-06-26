# -*- coding: utf-8 -*-
# une première application graphique
import tkinter

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

        # on créé les images : elles sont mémorisées 
        # dans un objet PhotoImage pour les .gif
        img = tkinter.PhotoImage(file="sphere1.gif")
        
        ## puis on créé chaque composant graphique et on les pose

        # le premier est un Label, ici il contient une image
        # ce composant appartient à la fenetre principale
        lbl_image = tkinter.Label(fenetre, image=img)
        lbl_image.pack()
        
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

