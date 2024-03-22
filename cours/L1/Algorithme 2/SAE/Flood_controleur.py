import vue_flood
import modele_flood

class controle:

    def __init__(self, vue=None , modele=None) -> None:
        

        self.__cntrl = self
        self.__modele = modele_flood.Modele()
        self.__vue = vue_flood.Vue(self.__modele, self.__cntrl)

    def quit(self) -> None:
        self.__vue.fenetre.destroy

    def retry(self) -> None:
        self.__modele.reinit_jeu()
        self.__vue.init_image()
        self.demarre()

    def demarre(self) -> None:
        self.__modele.init_jeu()
        self.__vue.demarre()
        