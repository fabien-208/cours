import tkinter

TAILLE=21


class Vue():
    def __init__(self,modele,cntrl)->None:

        self.__modele = modele
        X = TAILLE * self.__modele.nb_lig()
        Y = TAILLE * self.__modele.nb_col()
        self.__ctrl = cntrl
        self.__fenetre = tkinter.Tk()
        self.__fenetre.geometry(str(X + 70)+"x"+str(Y))
        self.__fenetre.title("Flood Game")
        self.__bouton = []
        self.__couleurs = ["red","orange","yellow","cyan","purple","blue","green"]
        self.__fenetre = tkinter.Canvas(width = self.__modele.nb_col()*TAILLE, height = self.__modele.nb_lig()*TAILLE)

        for i in range(self.__modele.nb_lig()):
            self.__bouton.append([])

            for j in range(self.__modele.nb_col()):
                control = self.__ctrl.creer_controleur_bouton(i,j)
                self.__bouton[i].append(tkinter.Button(self.__fenetre,bg=self.__couleurs[self.__modele.val_coul(i, j)], width = TAILLE, height = TAILLE, command = control))
                self.__bouton[i][j].place(x=j*TAILLE,y=i*TAILLE)
        self.__fenetre.pack(side = "left")
        self.__score=tkinter.StringVar(self.__fenetre, "score : "+str(self.__modele.score()))
        score = tkinter.Label(self.__fenetre,textvariable=self.__score,fg = "green")
        score.place(x=X+15, y=Y/2 - 42)
        self.__btn_quitter = tkinter.Button(self.__fenetre,text="Quit",command = self.__fenetre.destroy)
        self.__btn_retry = tkinter.Button(self.__fenetre, text = "Retry", command = self.__ctrl.nouvelle_partie())
        self.__btn_retry.place(x=X + 10, y=Y/2 - 20)
        self.__btn_quitter.place(x=X + 10, y=Y/2 + 10)
    
    def redessine(self)->None:
        self.__fenetre.delete("all")
        self.__score.set("score : "+str(self.__modele.score()))
        self.__boutons = []
        for i in range(self.__modele.nb_lig()):
            self.__boutons.append([])
            for j in range(self.__modele.nb_col()):
                control = self.__ctrl.creer_controleur_bouton(i,j)
                self.__boutons[i].append(tkinter.Button(self.__fenetre,bg=self.__couleurs[self.__modele.val_coul(i,j)], width = TAILLE, height = TAILLE, command= control))
                self.__boutons[i][j].place(x=j*TAILLE,y=i*TAILLE)

    def demarre(self)->None:
        self.__fenetre.mainloop()
    
    def partie_finie(self):
        finie = tkinter.Label(self.__fenetre,text="Partie finie!")
        taillex = TAILLE*self.__modele.nblig()
        tailley = TAILLE*self.__modele.nbcol()
        finie.place(x=taillex+8, y=tailley/2-70)
        for i in self.__boutons:
            for j in i:
                j.config(state = "disabled")