import vue_flood
import modele_flood

class controle:

    def __init__(self, vue= vue_flood.Vue(), modele =modele_flood.Modele()) -> None:
        self.vue = vue
        self.modele = modele

    def quit(self):
        self.vue.fenetre.destroy

    def retry(self):
        self.modele.__score = 0
        self.modele.init_jeu()
        self.vue.init_image()