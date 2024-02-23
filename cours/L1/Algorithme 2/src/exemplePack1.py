import tkinter

class VueCommande:
    '''Modélise une application pour prendre des commandes dans un restaurant.
    '''

    def __init__(self):
        fen = tkinter.Tk()
        fen.title("Mon Restau")
        

        ## formule entrée, plat, ou dessert ?
        choix_entree = tkinter.BooleanVar() 
        chk_entree = tkinter.Checkbutton(fen,text="Entrée",
                                variable=choix_entree)
        choix_plat = tkinter.BooleanVar() 
        chk_plat = tkinter.Checkbutton(fen,text="Plat",
                                variable=choix_plat)
        choix_dessert = tkinter.BooleanVar() 
        chk_dessert = tkinter.Checkbutton(fen,text="Dessert",
                                variable=choix_dessert)
        chk_entree.pack(side="left")
        chk_plat.pack(side="left")
        chk_dessert.pack(side="left")
        
        
        fen.mainloop()



if __name__ == "__main__" :
    mon_restau = VueCommande()
