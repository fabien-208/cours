import modele_flood
import Vue_Flood

class floodcontroleur():
    def __init__(self) -> None:
        self.__modele = modele_flood.Modele()
        self.__vue = Vue_Flood.Vue(self.__modele,self)
    
    def creer_controleur_bouton(self,l:int,c:int):
        #self.__modele.push()
        def controleur_bouton() -> None:
            self.__modele.pose_couleur(self.__modele.couleur(l,c))
            self.__vue.redessine()
            self.partie_finie()

        return controleur_bouton
    

    def demarre(self)->None:
        self.__vue.demarre()

    def nouvelle_partie(self) -> None:
        self.__modele.reinit()
        self.__vue.redessine()

    
    def partie_finie(self) -> None:
        if self.__modele.finie():
            if self.__modele.win():
                self.__vue.partie_finie(True)
            else:
                self.__vue.partie_finie(False)

    def Undo(self):
        print('jerjugzrt')
        self.__modele.pop()
        self.__vue.redessine()

    def reinit_partielle(self):
        self.__modele.enleve_reinit()
        self.__modele.reinit_partielle()
        self.__vue.redessine()
        


