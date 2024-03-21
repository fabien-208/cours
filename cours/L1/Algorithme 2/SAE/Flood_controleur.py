import vue_flood
import modele_flood

class controle:

    def __init__(self, vue=None , modele=None) -> None:
        

        self.__cntrl = {'Retry' : True, 'Quit' : True}
        self.__modele = modele_flood.Modele()
        self.__vue = vue_flood.Vue(self.__modele, self.__cntrl)

    def quit(self):
        self.__vue.fenetre.destroy

    def retry(self):
        self.__modele.reinit_jeu()
        self.__vue.init_image()

    def demarre(self):
        while self.__cntrl['Quit'] == True and self.__cntrl['Retry'] ==True:
            if self.__cntrl['Quit'] ==False:
                self.quit()
            if self.__cntrl['Retry'] == False:
                self.retry()
            else:
                self.__vue.demarre()
