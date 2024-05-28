import tkinter
DIM = 21


class vueDemineur:
    
    def __init__(self):
        fenetre = tkinter.Tk()
        fenetre.title("demineur")
        img = tkinter.PhotoImage(file="C:/Users/fabie/OneDrive/Documents/cours/cours/L1/Algorithme 2/TP/TP 5/images_demineur/mine.gif")
        
        can_image = tkinter.Canvas(fenetre, width= DIM,height= DIM)
        can_image.create_image(0,0,anchor = tkinter.NW,image = img)
        can_image.pack()
        
        btn_quitter = tkinter.Button(fenetre, 
                            text="Au revoir",
                            command = fenetre.destroy) 
        btn_quitter.pack()
        fenetre.mainloop()
        
        
        
        

class vueDemineur2:
    
    def __init__(self):
        fenetre = tkinter.Tk()
        fenetre.title("demineur")
        img = tkinter.PhotoImage(file="C:/Users/fabie/OneDrive/Documents/cours/cours/L1/Algorithme 2/TP/TP 5/images_demineur/mine.gif")
        dec = 0
        for i in range(5):
            can_image = tkinter.Canvas(fenetre, width= DIM,height= DIM)
            can_image.create_image(0,0,anchor = tkinter.NW,image = img)
            can_image.pack()
            dec += DIM
        btn_quitter = tkinter.Button(fenetre, 
                            text="Au revoir",
                            command = fenetre.destroy) 
        btn_quitter.pack()
        fenetre.mainloop()
        
        
        
        

if __name__ == '__main__' :
    mon_appli = vueDemineur2()