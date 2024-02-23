# -*- coding: utf-8 -*-
import tkinter
from random import randint

class VueSphere :
    '''Classe qui définit et met en place une interface graphique.
    On y affiche une image de sphère, qui change à chaque clic.
    '''
    
    def __init__(self):
        '''Vue, str -> Vue
        construit l'interface graphique et la lance.
        '''
        # première chose, créer la fenetre principale
        fenetre = tkinter.Tk()
        fenetre.title("Sphere")

        # on créé les images : elles sont mémorisées dans une liste de PhotoImage
        self.__images = []
        for i in range(1,9) :
            img = tkinter.PhotoImage(file="sphere"+str(i)+".gif")
            self.__images.append(img)

        # on mémorise l'indice de l'image affichée
        self.__indice = randint(0,len(self.__images)-1)

        ## puis on créé chaque composant graphique et on les pose
        # on va modifier l'image affichée, donc on mémorise 
        # dans un attribut le composant qui affiche l'image
        self.__btn_image = tkinter.Button(fenetre, image=self.__images[self.__indice], 
                                         command = self.change_image)
        self.__btn_image.pack()

        btn_quitter = tkinter.Button(fenetre, text="Au revoir", command = fenetre.destroy)
        btn_quitter.pack()
        
        # on lance la boucle d'écoute des événements
        fenetre.mainloop()


    def change_image(self):
        '''VueSphere -> None'''
        self.__indice = (self.__indice + 1)%len(self.__images)
        self.__btn_image["image"] = self.__images[self.__indice]

### fin de la classe Vue


### script principal
if __name__ == '__main__' :
    mon_appli = VueSphere()


