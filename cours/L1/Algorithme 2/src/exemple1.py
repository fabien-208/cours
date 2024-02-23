# -*- coding: utf-8 -*-
# une première application graphique
import tkinter


class Vue :
    '''Classe qui définit et met en place une interface graphique.
    '''
    
    def __init__(self,texte="Bonjour à tous"):
        '''Vue, str -> Vue
        construit l'interface graphique et la lance.
        '''
        # première chose, créer la fenetre principale
        fenetre = tkinter.Tk()
        # on peut lui mettre un titre
        fenetre.title("Premier exemple")

        ## puis on créé chaque composant graphique
        # le premier est un Label : une zone avec un texte ou une image
        # ce composant appartient à la fenetre principale
        lbl_message = tkinter.Label(fenetre, 
                           text=texte,
                           fg="red")
        # on pose le composant sur la fenetre
        lbl_message.pack()
        
        # le deuxième composant est un Button
        # il appartient également à la fenetre principale
        # un clic sur le bouton fait quitter l'appli
        btn_quitter = tkinter.Button(fenetre, 
                            text="Au revoir",
                            command = fenetre.destroy) 
        # on pose le composant sur la fenetre
        btn_quitter.pack()
        
        # on lance la boucle d'écoute des événements
        fenetre.mainloop()

### fin de la classe Vue

### script principal
if __name__ == '__main__' :
    mon_appli = Vue("j'espère qu evous avez passé de bonnes vacnces")





