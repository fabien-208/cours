
import modele_flood
import Flood_controleur
import tkinter

class Vue:

    def __init__(self, modele = modele_flood.Modele(), cntrl = None) -> None:
        self.__modele = modele
        self.__cntrl = Flood_controleur.controle()
        self.fenetre = tkinter.Tk()
        self.fenetre.title('Flood')
        lbl_message = tkinter.Label(self.fenetre, 
                           text=('score :'),
                           fg="black")
        lbl_message.grid(row=self.__modele.nb_lig()//2-1, column= self.__modele.nb_col()+1)
    
        btn_quitter = tkinter.Button(self.fenetre, 
                            text="Quit",
                            command = self.__cntrl.quit())  # type: ignore
        btn_quitter.grid(row=self.__modele.nb_lig()//2 +1, column=self.__modele.nb_col()+1)
        btn_retry = tkinter.Button(self.fenetre,
                                   text = 'Retry',
                                   command= self.__cntrl.retry()) # type: ignore
        btn_retry.grid(row=self.__modele.nb_lig()//2, column=self.__modele.nb_col()+1)
        self.init_image()
        self.fenetre.mainloop()

    def init_image(self):
            for i in range(1, self.__modele.nb_lig()+1):
                for j in range(1, self.__modele.nb_col()+1):
                    case = tkinter.IntVar()
                    can_image = tkinter.Button(self.fenetre, text='   ', bg=self.couleur_case(i-1, j-1)) # type: ignore
                    can_image.grid(row=i, column=j, sticky='NSEW')


    def couleur_case(self, l, c):
        coul = self.__modele.valeur_couleur(l, c)
        if coul == 0:
             return 'yellow'
        if coul == 1:
             return 'red'
        if coul == 2:
             return 'blue'
        if coul == 3:
             return 'green'
        if coul == 4:
             return 'purple'
        if coul == 5:
             return 'orange'
        

if __name__ == '__main__' :
    mon_appli = Vue()