
import tkinter

class vueMessage2:
    
    def __init__(self):
        fenetre = tkinter.Tk()
        fenetre.title("exemple 2")
        lbl_message = tkinter.Label(fenetre, 
                           text="bonjour a tou",
                           fg="red")
        
        lbl_message.pack()
        
        self.__zn_saise = tkinter.Entry(fenetre ,fg="green", bg="light grey")
        self.__zn_saise.pack()
        
        btn_valide = tkinter.Button(fenetre, text="OK", command = self.saisie_texte)
        btn_valide.pack()
        
        self.__lbl_texte = tkinter.Label(fenetre, text="bonjour", fg="blue")
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
        message = self.__zn_saise.get() 
        # affiche ce texte dans lbl_texte
        self.__lbl_texte.config(text=message) 
        # efface le contenu de la zone de saisie
        self.__zn_saise.delete(0,len((message)))     
    
        
if __name__ == '__main__' :
    mon_appli = vueMessage2()