import tkinter

class VueCommande:
    '''Modélise une application pour prendre des commandes dans un restaurant.
    '''

    def __init__(self):
        fen = tkinter.Tk()
        fen.title("Mon Restau")
        

        ## pour le nom du client
        fr_client = tkinter.Frame(fen) 
        lbl = tkinter.Label(fr_client,text="Nom du client : ")
        lbl.pack(side="left")
        zn_saisie = tkinter.Entry(fr_client,width=15)
        zn_saisie.pack(side="left")
        fr_client.pack()

        ## les trois frames
        fr_menu = tkinter.Frame(fen)
        fr_entree = tkinter.Frame(fr_menu)
        fr_plat = tkinter.Frame(fr_menu)
        fr_dessert = tkinter.Frame(fr_menu)
        fr_entree.grid(row=0,column=0)
        fr_plat.grid(row=0,column=1)
        fr_dessert.grid(row=0,column=2)
        fr_menu.pack()

        ## formule entrée, plat, ou dessert ?
        # Entree
        self.__choix_entree = tkinter.BooleanVar() 
        chk_entree = tkinter.Checkbutton(fr_entree,text="Entrée",
                                        variable=self.__choix_entree,
                                        command=self.choisit_entree)
        ## pour l'entrée, deux choix
        radio_var = tkinter.IntVar() 
        rad_carottes = tkinter.Radiobutton(fr_entree, text="Carottes rapées",
                                          variable=radio_var, value=1,justify="left", 
                                          state="disable") 
        rad_betteraves = tkinter.Radiobutton(fr_entree, text="Betteraves cuites",
                                            variable=radio_var, value=2, state="disable")
        chk_entree.grid(row=0,column=0)
        rad_carottes.grid(row=1,column=0,sticky="W")
        rad_betteraves.grid(row=2,column=0,sticky="W")
        self.__les_entrees = [rad_carottes, rad_betteraves]

        # Plat
        self.__choix_plat = tkinter.BooleanVar() 
        chk_plat = tkinter.Checkbutton(fr_plat,text="Plat",
                                      variable=self.__choix_plat,
                                      command=self.choisit_plat)
        ## pour le plat, deux choix
        radio_var = tkinter.IntVar() 
        rad_poulet = tkinter.Radiobutton(fr_plat, text="Poulet frites",
                                        variable=radio_var, value=1, state="disable") 
        rad_lasagnes = tkinter.Radiobutton(fr_plat, text="Lasagnes aux épinards",
                                          variable=radio_var, value=2, state="disable")
        chk_plat.grid(row=0,column=0)
        rad_poulet.grid(row=1,column=0,sticky="W")
        rad_lasagnes.grid(row=2,column=0,sticky="W")
        self.__les_plats = [rad_poulet, rad_lasagnes]

        # Dessert
        self.__choix_dessert = tkinter.BooleanVar() 
        chk_dessert = tkinter.Checkbutton(fr_dessert,text="Dessert",
                                         variable=self.__choix_dessert,
                                         command=self.choisit_dessert)
        ## pour le dessert, deux choix
        radio_var = tkinter.IntVar() 
        rad_pommes = tkinter.Radiobutton(fr_dessert, text="Tarte aux pommes",
                                        variable=radio_var, value=1, state="disable") 
        rad_profiterolles = tkinter.Radiobutton(fr_dessert, text="Profiterolles",
                                               variable=radio_var, value=2, state="disable")
        chk_dessert.grid(row=0,column=0)
        rad_pommes.grid(row=1,column=0,sticky="W")
        rad_profiterolles.grid(row=2,column=0,sticky="W")
        self.__les_desserts = [rad_pommes, rad_profiterolles]
        
        # on lance la boucle d'écoute des événements
        fen.mainloop()


    def choisit_entree(self):
        '''VueCommande -> None
        l'entrée vient d'etre sélectionnée ou désélectionnée
        '''
        if not self.__choix_entree.get() :
            for radio in self.__les_entrees :
                radio.deselect()
                radio['state'] = "disable"
        else : 
            for radio in self.__les_entrees :
                radio['state'] = "normal"

    def choisit_plat(self):
        '''VueCommande -> None
        le plat vient d'etre sélectionné ou désélectionné
        '''
        if not self.__choix_plat.get() :
            for radio in self.__les_plats :
                radio.deselect()
                radio['state'] = "disable"
        else : 
            for radio in self.__les_plats :
                radio['state'] = "normal"

    def choisit_dessert(self):
        '''VueCommande -> None
        le dessert vient d'etre sélectionné ou désélectionné
        '''
        if not self.__choix_dessert.get() :
            for radio in self.__les_desserts :
                radio.deselect()
                radio['state'] = "disable"
        else : 
            for radio in self.__les_desserts :
                radio['state'] = "normal"


if __name__ == "__main__" :
    mon_restau = VueCommande()