
import tkinter
import Flood_controleur


class Vue:

     def __init__(self, modele , cntrl) -> None:
         self.__modele = modele
         self.__cntrl = cntrl
         self.fenetre = tkinter.Tk()
        

     def demarre(self):
          self.fenetre.title('Flood')
          lbl_message = tkinter.Label(self.fenetre, 
                              text=('score :{}'.format(self.__modele.score())),
                              fg="black")
          lbl_message.grid(row=self.__modele.nb_lig()//2-1, column= self.__modele.nb_col()+1)
    
          btn_quitter = tkinter.Button(self.fenetre,text="Quit",command = self.__cntrl.quit())  # type: ignore
          
          btn_quitter.grid(row=self.__modele.nb_lig()//2 +1, column=self.__modele.nb_col()+1, padx=10)

          btn_retry = tkinter.Button(self.fenetre,text = 'Retry',command= self.__cntrl.retry()) # type: ignore
          
          btn_retry.grid(row=self.__modele.nb_lig()//2, column=self.__modele.nb_col()+1, padx=10)
          self.init_image()
          self.fenetre.mainloop()
          return None

     def init_image(self):
          for i in range(1, self.__modele.nb_lig()+1):
               for j in range(1, self.__modele.nb_col()+1):
                    case = tkinter.IntVar()
                    can_image = tkinter.Button(self.fenetre, bg=self.couleur_case(i-1, j-1), padx=8) # type: ignore
                    can_image.grid(row=i, column=j)


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
        
     def quit(self):
          self.fenetre.destroy

          
     def retry(self):
          self.__modele.reinit_jeu()
          self.init_image()