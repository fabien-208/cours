#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Tictactoe():
    """
    classe qui permet de jouer et d'afficher le jeu tic tac toe
    
    >>> partie = Tictactoe()
    >>> joueur1 = partie.tour_de()
    >>> partie.joue(joueur1, 5)
    >>> partie.joue(partie.tour_de(), 6)
    >>> partie.joue(partie.tour_de(), 9)
    >>> print(partie.to_str())
    """
    
    def __init__(self, jeu = [" "]*9, joueur = 'X'):
        self.jeu = jeu[:]
        self.joueur = joueur    

    def tour_de(self):
        return self.joueur
        

    def joue(self, joueur, pos):
        pos -= 1

        if self.jeu_gagner():
            return
        
        if self.joueur != joueur:
            return self.joueur

        if self.pos_libre(pos + 1):
            self.jeu[pos] = joueur
            self.joueur = 'X' if self.joueur == 'O' else 'O'
            return True

        return False

    def jeu_gagner(self, joueur):
        for i in range(3):
            if self.jeu[i] == self.jeu[i + 3] == self.jeu[i + 6] != ' ':
                return self.jeu[i]

            if self.jeu[i * 3] == self.jeu[i * 3 + 1] == self.jeu[i * 3 + 2] != ' ':
                return self.jeu[i * 3]

        if self.jeu[2] == self.jeu[4] == self.jeu[6] != ' ':
            return self.jeu[2]
        
        if self.jeu[0] == self.jeu[4] == self.jeu[8] != ' ':
            return self.jeu[0]

        
        if not " " in self.jeu:
            return None

        return False

    def to_str(self):
        """
        affiche le jeu Tictactoe
        """ 
        return "{} | {} | {}\n---------\n{} | {} | {}\n---------\n{} | {} | {}".format(
            self.jeu[6], self.jeu[7], self.jeu[8],
            self.jeu[3], self.jeu[4], self.jeu[5],
            self.jeu[0], self.jeu[1], self.jeu[2]
        )
    




    def pos_libre(self, pos):
        return self.jeu[pos - 1] != "X" and self.jeu[pos - 1] != "O"















if __name__=="__main__":
    import doctest
    doctest.testmod(verbose = True)
