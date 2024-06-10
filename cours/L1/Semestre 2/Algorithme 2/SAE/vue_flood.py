import tkinter 
import modele_flood



TAILLE=25
class Vue():

    def __init__(self,modele:modele_flood.Modele,cntrl)->None:
        self.__modele = modele
        self.__taille_X = TAILLE*self.__modele.nb_lig()
        self.__taille_Y = TAILLE*self.__modele.nb_col()
        self.__cntrl = cntrl
        self.__fenetre = tkinter.Tk()
        self.__fenetre.geometry(str(self.__taille_X+90) + "x" + str(self.__taille_Y))
        self.__fenetre.title("Flood Game")
        self.__boutons = []
        self.__couleurs = ["cyan","blue","yellow","purple","orange","red","green"]
        self.__grille = tkinter.Canvas(width = self.__modele.nb_col() * TAILLE, height = self.__modele.nb_lig() * TAILLE)

        for i in range(self.__modele.nb_lig()):
            self.__boutons.append([])
            for j in range(self.__modele.nb_col()):
                control = self.__cntrl.creer_controleur_bouton(i,j)
                self.__boutons[i].append(tkinter.Button(self.__grille,bg=self.__couleurs[self.__modele.couleur(i,j)], width = TAILLE, height = TAILLE, command = control))
                self.__boutons[i][j].place(x = j*TAILLE,y = i*TAILLE)
        self.__grille.pack(side = "left")
        self.__scorevar = tkinter.StringVar(self.__fenetre, "score : " + str(self.__modele.score()))
        score = tkinter.Label(self.__fenetre, textvariable = self.__scorevar,fg = "green")
        score.place(x = self.__taille_X + 20, y = self.__taille_Y / 2 - 25)
        self.__btn_quitter = tkinter.Button(self.__fenetre,text = "Quit",command = self.__fenetre.destroy)
        self.__btn_reset = tkinter.Button(self.__fenetre, text = "Retry", command = self.__cntrl.nouvelle_partie)
        self.__btn_reset.place(x = self.__taille_X + 10, y = self.__taille_Y / 2)
        self.__btn_quitter.place(x = self.__taille_X + 50, y = self.__taille_Y / 2)
        max_score = tkinter.Label(self.__fenetre, text = 'Score Max : ' + str(self.__modele.max_coups()), fg = 'red')
        max_score.place(x = self.__taille_X + 5, y = self.__taille_Y // 2 - 70)
        self.__bouton_Undo = tkinter.Button(self.__fenetre, text='Undo', command= self.__cntrl.Undo)
        self.__bouton_Undo.place(x= self.__taille_X + 28, y = self.__taille_Y / 2 + 28)


        self.__bouton_reinit = tkinter.Button(self.__fenetre, text='reinit partielle', command=self.__cntrl.reinit_partielle)
        self.__bouton_reinit.place(x=self.__taille_X + 5, y=self.__taille_Y / 2 + 53)
        self.__var_reinit = tkinter.StringVar(self.__fenetre, "Reste : " + str(self.__modele.nb_reinit()))
        self.__reinit = tkinter.Label(self.__fenetre, textvariable= self.__var_reinit, fg='black')
        self.__reinit.place(x= self.__taille_X+ 21, y=self.__taille_Y / 2 + 80)

    
    def redessine(self)->None:
        self.__grille.delete("all")
        self.__scorevar.set("score : "+str(self.__modele.score()))
        self.__var_reinit.set("Reste : " + str(self.__modele.nb_reinit()))
        for i in range(self.__modele.nb_lig()):
            for j in range(self.__modele.nb_col()):
                self.__boutons[i][j].config(bg=self.__couleurs[self.__modele.couleur(i,j)])
        max_score = tkinter.Label(self.__fenetre, text = 'Score Max : ' + str(self.__modele.max_coups()), fg = 'red')
        max_score.place(x = self.__taille_X + 5, y = self.__taille_Y // 2 - 70)

    def demarre(self)->None:
        self.__fenetre.mainloop()
    
    def partie_finie(self, win:bool):
        if win == True:
            finie = tkinter.Label(self.__fenetre,text="Partie Finie !")
            finie.place(x = self.__taille_X + 12, y = self.__taille_Y / 2 - 90)
            frbh = tkinter.Label(self.__fenetre, text='You Won !!!')
            frbh.place(x = self.__taille_X +12, y = self.__taille_Y /2 -50)
            finie.after(6000, finie.destroy)
            frbh.after(6000, frbh.destroy)
        else:
            finie = tkinter.Label(self.__fenetre,text="Partie Finie !")
            finie.place(x = self.__taille_X + 12, y = self.__taille_Y / 2 - 90)
            finie.after(6000, finie.destroy)
        