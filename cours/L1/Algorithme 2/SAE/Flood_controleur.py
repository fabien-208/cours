import vue_flood
import modele_flood

class controle:

    def __init__(self, vue=None , modele=None) -> None:
        

        self.__modele = modele_flood.Modele()
        self.__cntrl = self.fonction_button()
        self.__vue = vue_flood.Vue(self.__modele, self.__cntrl)


    def creer_controleur_bouton(self):
        pass


    def fonction_button(self, q = False, r= False):
        if q == True:
            def quit(self):
                self.__vue.fenetre.destroy
        if r == True:
            def retry(self):
                self.__modele.reinit_jeu()
                self.__vue.init_image()

    def demarre(self) -> None:
        self.__modele.init_jeu()
        self.__vue.demarre()
        