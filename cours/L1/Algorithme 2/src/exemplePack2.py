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

        # on créé les images : elles sont mémorisées dans un objet PhotoImage
        img = tkinter.PhotoImage(file="C:/Users/fabie/OneDrive/Documents/cours/cours/L1/Algorithme 2/TP/TP 5/images_demineur/mine.png")


        ## puis on créé chaque composant graphique et on les pose

        lbl_gauche = tkinter.Label(fenetre,text="à gauche")
        lbl_droit = tkinter.Label(fenetre,text="à droite")
        lbl_gauche.pack(side="left")
        lbl_droit.pack(side="right")

        # celui qui contient une image est un canevas
        # ce composant appartient à la fenetre principale
        can_image = tkinter.Canvas(fenetre, width=img.width(),height=img.height())
        can_image.create_image(0,0,anchor=tkinter.NW,image=img)
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

