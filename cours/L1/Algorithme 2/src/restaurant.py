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

        ## les quatre frames
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
        choix_entree = tkinter.BooleanVar() 
        chk_entree = tkinter.Checkbutton(fr_entree,text="Entrée",
                                variable=choix_entree)
        ## pour l'entrée, deux choix
        radio_var = tkinter.IntVar() 
        rad_carottes = tkinter.Radiobutton(fr_entree, text="Carottes rapées",
                                          variable=radio_var, value=1,justify="left") 
        rad_betteraves = tkinter.Radiobutton(fr_entree, text="Betteraves cuites",
                               variable=radio_var, value=2)
        chk_entree.grid(row=0,column=0)
        rad_carottes.grid(row=1,column=0,sticky="W")
        rad_betteraves.grid(row=2,column=0,sticky="W")

        # Plat
        choix_plat = tkinter.BooleanVar() 
        chk_plat = tkinter.Checkbutton(fr_plat,text="Plat",
                                variable=choix_plat)
        ## pour le plat, deux choix
        radio_var = tkinter.IntVar() 
        rad_poulet = tkinter.Radiobutton(fr_plat, text="Poulet frites",
                              variable=radio_var, value=1) 
        rad_lasagnes = tkinter.Radiobutton(fr_plat, text="Lasagnes aux épinards",
                               variable=radio_var, value=2)
        chk_plat.grid(row=0,column=0)
        rad_poulet.grid(row=1,column=0,sticky="W")
        rad_lasagnes.grid(row=2,column=0,sticky="W")

        # Dessert
        choix_dessert = tkinter.BooleanVar() 
        chk_dessert = tkinter.Checkbutton(fr_dessert,text="Dessert",
                                         variable=choix_dessert)
        ## pour le dessert, deux choix
        radio_var = tkinter.IntVar() 
        rad_pommes = tkinter.Radiobutton(fr_dessert, text="Tarte aux pommes",
                              variable=radio_var, value=1) 
        rad_profiterolles = tkinter.Radiobutton(fr_dessert, text="Profiterolles",
                               variable=radio_var, value=2)
        chk_dessert.grid(row=0,column=0)
        rad_pommes.grid(row=1,column=0,sticky="W")
        rad_profiterolles.grid(row=2,column=0,sticky="W")
        

        
        fen.mainloop()



if __name__ == "__main__" :
    mon_restau = VueCommande()
