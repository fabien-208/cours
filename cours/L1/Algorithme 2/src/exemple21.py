# -*- coding: utf-8 -*-
# une première application graphique
import tkinter


class Vue :
    '''Classe qui définit et met en place une interface graphique.
    '''
    
    def __init__(self,texte="Votre message"):
        '''Vue, str -> Vue
        construit l'interface graphique et la lance.
        '''
        fenetre = tkinter.Tk()
        
        fenetre.title("Exemple zone de saisie")

        lbl_message = tkinter.Label(fenetre, 
                           text=texte,
                           fg="red")
        
        lbl_message.pack()
        
        self.__zn_saisie = tkinter.Entry(fenetre,fg="green", bg="light grey")
        self.__zn_saisie.pack()
        
        btn_valide = tkinter.Button(fenetre, text="OK", command = self.saisie_texte)
        btn_valide.pack()

        self.__lbl_texte = tkinter.Label(fenetre, text="", fg="blue")
        self.__lbl_texte.pack()
        
        btn_quitter = tkinter.Button(fenetre, 
                            text="Au revoir",
                            command = fenetre.destroy) 
        btn_quitter.pack()
        fenetre.mainloop()

    def saisie_texte(self) :
        '''Vue -> None
        récupère le texte saisi par l'utilisateur, 
        l'affiche dans __lbl_texte et réinitialise __sn_saisie.
        '''
        # retourne le texte saisi par l'utilisateur
        message = self.__zn_saisie.get() 
        # affiche ce texte dans lbl_texte
        self.__lbl_texte.config(text=message) 
        # efface le contenu de la zone de saisie
        self.__zn_saisie.delete(0,len((message))) 


### fin de la classe Vue

### script principal
if __name__ == '__main__' :
    mon_appli = Vue()





