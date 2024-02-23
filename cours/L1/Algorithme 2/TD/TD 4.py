
class matrice:

    def __init__(self, mat:list[list[int]]) -> None:
        """
        >>> bfrh = [[2, 4, 7],[6, 2],[5, 6, 9]]
        >>> bfrrergt = [[6, 4, 4],[4, 1],[0, 8, 4]]
        >>> tru = matrice(bfrrergt)
        >>> tr = matrice(bfrh)
        >>> tr.__str__()
        >>> tru.__str__()
        """
        self.taille = 0
        for i in range(len(mat)):
            if len(mat[i]) > self.taille:
                self.taille = len(mat[i])


        for j in range(len(mat)):
            if len(mat[j]) != self.taille:
                mat[j].append(0)
        self.__mat = mat

    def __str__(self) -> None:
        for lis in self.__mat:
            mat = '| '
            for i in range(len(lis)):
                mat += '{} '.format(lis[i])
            mat += '|'
            print(mat) 

    def nb_lignes(self) -> int:
        return len(self.__mat)
    
    def nb_colonne(self) -> int:
        return len(self.__mat[0])
    


    def est_matrice_carre(self) -> bool:
        return self.nb_colonne() == self.nb_lignes()
    
#    def est_mat_sym(self) ->bool:
        if not(self.est_matrice_carre()):
            return False
        else:
            for i in range(self.nb_lignes()):
                for j in range(self.nb_colonne):
                    pass



    def add_mat(self, mat2):
        mat = []
        for i in range(len(self.__mat)):
            lit = []
            for j in range(len(self.__mat[i])):
                lit.append(mat2.__mat[i][j] + self.__mat[i][j])
            mat.append(lit)
        return matrice(mat)
    


    def transpose_mat(self):
        mat = []
        for i in range(len(self.__mat[0])):
            lig = []
            for j in range(len(self.__mat)):
                lig.append(self.__mat[j][i])
            mat.append(lig)
        return matrice(mat)
        


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)