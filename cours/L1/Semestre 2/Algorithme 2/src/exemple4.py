# -*- coding: utf-8 -*-
# une première application graphique
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
        fenetre.title("Les sphères")

        # on créé les images : elles sont mémorisées dans une liste de PhotoImage
        self.__images = []
        for i in range(1,9) :
            img = tkinter.PhotoImage(file="sphere"+str(i)+".gif")
            self.__images.append(img)

        # on mémorise les indices des images affichées
        self.__lesIndices = []
        for i in range(4):
            self.__lesIndices.append(randint(0,len(self.__images)-1))

        ## puis on créé chaque composant graphique et on les pose
        # on mémorise tous les boutons dans une liste de boutons
        self.__boutonImages = []
        for i in range(4) :
            btn = tkinter.Button(fenetre, 
                                 image=self.__images[self.__lesIndices[i]])
            btn["command"] = change_image_bouton(i,self.__lesIndices,btn,self.__images)
            self.__boutonImages.append(btn)
            self.__boutonImages[i].grid(row=0,column=i)

        btnQuitter = tkinter.Button(fenetre, text="Au revoir", command = fenetre.destroy)
        btnQuitter.grid(row=1,columnspan=4)
        
        # on lance la boucle d'écoute des événements
        fenetre.mainloop()

### fin de la classe Vue

def change_image_bouton(i,lesIndices,btn,lesImages):
    """change_image_bouton : int,list(int),Button,list(PhotoImage) -> Fct"""
    def change_image():
        """changeImage : (rien) -> (rien)"""
        lesIndices[i] = (lesIndices[i] + 1)%len(lesImages)
        btn["image"] = lesImages[lesIndices[i]]
    return change_image


### script principal
if __name__ == '__main__' :
    monAppli = VueSphere()




