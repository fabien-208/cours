
import modele_flood
import Flood_controleur
import tkinter

class Vue:

    def __init__(self, modele = modele_flood.Modele(), cntrl = Flood_controleur.cntrl()) -> None:
        self.__modele = modele
        self.__cntrl = cntrl
        self.fenetre = tkinter.Tk()
        self.fenetre.title('Flood')

    
        btn_quitter = tkinter.Button(self.fenetre, 
                            text="Quit",
                            command = self.fenetre.destroy) 
        btn_quitter.grid()
        btn_retry = tkinter.Button(self.fenetre,
                                   text = 'Retry',
                                   command= '')
        btn_retry.grid()
        self.init_image()
        self.fenetre.mainloop()

    def init_image(self):
            for i in range(1, self.__modele.nb_lig()+1):
                for j in range(1, self.__modele.nb_col()+1):
                    case = tkinter.IntVar()
                    can_image = tkinter.Button(self.fenetre, text=self.__modele.valeur_couleur(i-1, j-1))
                    can_image.grid(row=i, column=j, sticky='NSEW')


if __name__ == '__main__' :
    mon_appli = Vue()