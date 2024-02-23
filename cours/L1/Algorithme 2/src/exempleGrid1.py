import tkinter

class VueCommande:
    '''Modélise une application pour prendre des commandes dans un restaurant.
    '''

    def __init__(self):
        fen = tkinter.Tk()
        fen.title("Mon Restau")
        
        ## pour l'entrée, deux choix
        radio_var = tkinter.IntVar() 
        rad_carottes = tkinter.Radiobutton(fen, text="Carottes rapées",
                                          variable=radio_var, value=1, bg="dark grey") 
        rad_betteraves = tkinter.Radiobutton(fen, text="Betteraves cuites",
                               variable=radio_var, value=2)
        rad_carottes.grid(row=0,column=0, sticky="NSEW")
        rad_betteraves.grid(row=1,column=0, sticky="NSEW")

        ## pour le plat, deux choix
        radio_var = tkinter.IntVar() 
        rad_poulet = tkinter.Radiobutton(fen, text="Poulet frites",
                              variable=radio_var, value=1) 
        rad_lasagnes = tkinter.Radiobutton(fen, text="Lasagnes\n aux épinards",
                                          variable=radio_var, value=2, bg="dark grey")
        rad_poulet.grid(row=0,column=1, sticky="NSEW")
        rad_lasagnes.grid(row=1,column=1, sticky="NSEW")

        ## pour le dessert, deux choix
        radio_var = tkinter.IntVar() 
        rad_pommes = tkinter.Radiobutton(fen, text="Tarte aux pommes",
                                        variable=radio_var, value=1, bg="dark grey") 
        rad_profiterolles = tkinter.Radiobutton(fen, text="Profiterolles",
                               variable=radio_var, value=2)
        rad_pommes.grid(row=0,column=2, sticky="NSEW")
        rad_profiterolles.grid(row=1,column=2, sticky="NSEW")
        
        fen.mainloop()



if __name__ == "__main__" :
    mon_restau = VueCommande()
