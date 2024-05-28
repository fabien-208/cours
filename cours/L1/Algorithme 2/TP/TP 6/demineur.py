# -*- coding: utf-8 -*-
import random
import tkinter
from tkinter.messagebox import RETRY
from turtle import left

from setuptools import Command

class Case :
    '''Case d'un jeu de démineur.
    '''

    def __init__(self, valeur=0) :
        '''Case, int -> Case
        Constructeur d'une case
        '''
        if -1 <= valeur <= 0 :
            self.__valeur = valeur
        else :
            self.__valeur = 0
        self.__cache = True

    def est_cache(self) :
        '''Case -> boolean
        retourne vrai si la case est cachée.
        ''' 
        return self.__cache

    def est_visible(self) :
        '''Case -> boolean
        retourne faux si la case est cachée.
        ''' 
        return not self.__cache

    def est_bombe(self) :
        '''Case -> boolean
        retourne vrai si la case contient une bombe.
        ''' 
        return self.__valeur == -1

    def est_vide(self) :
        '''Case -> boolean
        retourne vrai si la case ne contient pas de bombe 
        et n'est pas voisine d'une bombe.
        ''' 
        return self.__valeur == 0

    def incremente_valeur(self) :
        '''Case(inout) -> None
        met à jour la valeur de self.
        '''
        if not self.est_bombe() :
            self.__valeur = self.__valeur + 1

    def str(self) :
        '''Case -> str
        retourne une représentation sosu forme textuelle d'une case.
        '''
        if self.est_cache() :
            return '-'
        elif self.est_vide() :
            return ' '
        elif self.est_bombe() :
            return '*'
        else :
            return str(self.__valeur)

    def montre_toi(self) :
        '''Case (inout) -> None
        rend visible la case.
        '''
        self.__cache = False

    def valeur(self) :
        '''Case -> int
        retourne la valeur contenue dans une case.
        '''
        return self.__valeur

class Demineur :
    '''modélise le jeu du démineur.
    '''
  
    def __init__(self,nb_lig=10,nb_col=20) :
        '''Demineur, int, int -> Demineur
        Construit un démineur de nb_lig lignes et de nb_col colonnes.
        '''
        self.__nb_lig = nb_lig
        self.__nb_col = nb_col
        self.__plateau = []
        for i in range(nb_lig) :
            self.__plateau.append([])
            for j in range(nb_col) :
                self.__plateau[i].append(Case())

    def reinit(self) :
        '''
        Demineur (inout) -> None
        réinitialise le plateau de jeu du démineur
        '''
        self.__plateau = []
        for i in range(self.__nb_lig) :
            self.__plateau.append([])
            for j in range(self.__nb_col) :
                self.__plateau[i].append(Case())
        self.pose_bombes()

    def pose_bombes(self,nb_bombes=15) :
        '''Demineur (inout), int -> None
        pose nb_bombes sur le playeau du démineur.
        met à jour les cases voisines de chaque bombe.
        '''
        for i in range(nb_bombes) :
            c = random.randint(0,self.__nb_col - 1)
            l = random.randint(0,self.__nb_lig - 1)
            while self.__plateau[l][c].est_bombe() :
                c = random.randint(0,self.__nb_col-1)
                l = random.randint(0,self.__nb_lig-1)
            self.__plateau[l][c] = Case(-1)
            if c > 0 :
                self.__plateau[l][c-1].incremente_valeur()
                if l > 0 :
                    self.__plateau[l-1][c-1].incremente_valeur()
                if l < self.__nb_lig-1 :
                    self.__plateau[l+1][c-1].incremente_valeur()
            if c < self.__nb_col-1 :
                self.__plateau[l][c+1].incremente_valeur()
                if l > 0 :
                    self.__plateau[l-1][c+1].incremente_valeur()
                if l < self.__nb_lig-1 :
                    self.__plateau[l+1][c+1].incremente_valeur()
            if l > 0 :
                self.__plateau[l-1][c].incremente_valeur()
            if l < self.__nb_lig-1 :
                self.__plateau[l+1][c].incremente_valeur()


    def affiche_ligne_traits(self) :
        '''Demineur -> None
        affiche une ligne de traits pour le jeu en mode texte.
        '''
        res = "  "
        for i in range(self.__nb_col) :
            res += "+-"
        res += "+"
        print(res)

    def affiche_ligne(self,lig) :
        '''Demineur, int -> None
        affiche une ligne du plateau pour le jeu en mode texte.
        '''
        res = str(lig)+" |"
        for i in range(self.__nb_col) :
            res += self.__plateau[lig][i].str()
            res += "|"
        print(res)

    def affiche_numeros_colonnes(self) :
        '''Demineur -> None
        affiche les numéros de colonnes pour la version en mode texte.
        '''
        res = "   "
        if self.__nb_col <= 10 :
            for i in range(self.__nb_col) :
                res +=str(i)+" "
        else :
            for i in range(self.__nb_col) :
                if i < 10 :
                    res +=str(i)+" "
                else :
                    res += "1 "
            print(res)
            res = "   "
            for i in range(self.__nb_col) :
                if i < 10 :
                    res += "  "
                else :
                    res += str(i%10) + " "
        print(res)
        
    def affiche_plateau(self) :
        '''Demineur -> None
        affiche le plateau de jeu pour la version en mode texte.
        '''
        self.affiche_numeros_colonnes()
        self.affiche_ligne_traits()
        for i in range(self.__nb_lig) :
            self.affiche_ligne(i)
            self.affiche_ligne_traits()

    def montre_case(self,l,c) :
        '''Demineur (inout), int, int, -> None

        découvre la case (l,c) et ses voisines le cas échéant. 
        l et c doivent être positfs et inférieurs à, respectivement, 
        __nb_lig et __nb_col.
        '''
        if not self.__plateau[l][c].est_visible() :
            self.__plateau[l][c].montre_toi()
            if self.__plateau[l][c].est_bombe() :
                return False
            elif self.__plateau[l][c].est_vide() :
                if c > 0 :
                    self.montre_case(l,c-1)
                    if l > 0 :
                        self.montre_case(l-1,c-1)
                    if l < self.__nb_lig-1 :
                        self.montre_case(l+1,c-1)
                if c < self.__nb_col-1 :
                    self.montre_case(l,c+1)
                    if l > 0 :
                        self.montre_case(l-1,c+1)
                    if l < self.__nb_lig-1 :
                        self.montre_case(l+1,c+1)
                if l > 0 :
                    self.montre_case(l-1,c)
                if l < self.__nb_lig-1 :
                    self.montre_case(l+1,c)
            return True

    def montre(self,l,c) :
        '''Demineur, int, int, -> None

        découvre la case (l,c) et affiche le plateau.
        l et c doivent être positfs et inférieurs à, respectivement, 
        __nb_lig et __nb_col.
        '''
        self.montre_case(l,c)
        self.affiche_plateau()


    def partie_finie(self,l,c) :
        '''Demineur, int, int  -> boolean
        retourne vrai si la partie est finie (on vient de sauter sur une mine
        ou au contraire on les a toutes évitées.
        '''
        if self.__plateau[l][c].est_bombe() :
            return True
        else :
            for i in range(self.__nb_lig) :
                for case in self.__plateau[i] :
                    if case.est_cache() and not case.est_bombe() :
                        return False
            return True
    
    def valeur(self, l, c):
        return self.__plateau[l][c].valeur()
    

    def lig(self):
        return self.__nb_lig
    

    def col(self):
        return self.__nb_col
    
    def est_cache(self, l, c):
        return self.__plateau[l][c].est_cache()
    

class vuedemineur:

    def __init__(self) -> None:
        self.dem = Demineur()
        
        self.fenetre = tkinter.Tk()
        self.fenetre.title("Demineur")
        self.img = tkinter.PhotoImage(file="C:/Users/fabie/OneDrive/Documents/cours/cours/L1/Algorithme 2/TP/TP 5/images_demineur/cache.gif")
        self.btn_quit= tkinter.Button(self.fenetre , text = "Quitter" , command = quit)
        self.btn_quit.grid(row =self.dem.lig()+1, column= self.dem.col()//2+1, sticky= 'N')
        self.btn_retry = tkinter.Button(self.fenetre, text='retry', command = self.cntrl_reinit)
        self.btn_retry.grid(row =self.dem.lig()+1, column= self.dem.col()//2, sticky= 'S')

        self.init_image()
        self.fenetre.mainloop()


    def init_image(self):
        for i in range(1, self.dem.lig()+1):
            for j in range(1, self.dem.col()+1):
                case = tkinter.IntVar()
                can_image = tkinter.Button(self.fenetre, image=self.img)
                can_image.grid(row=i, column=j, sticky='NSEW')

    def crer_cntrl_case(self, l, c):
        if self.dem.est_cache(l, c):
            pass
        else:
            val = self.dem.valeur(l, c)



    def cntrl_reinit(self):
        self.init_image()


if '__main__' == __name__:
    mon_app = vuedemineur()