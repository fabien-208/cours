
class matrice:

    def __init__(self, mat:list[list[int]]) -> None:
        """
        >>> bfrh = [[1 , 2],[3, 4],[5, 6]]
        >>> fru = [[1, 3], [1, 0], [1, 2]]
        >>> bfrrergt = [[ 0, 0],[7, 5],[ 2, 1]]
        >>> tru = matrice(bfrrergt)
        >>> tr = matrice(bfrh)
        >>> hg = matrice(fru)
        >>> tr.__str__()
        >>> tru.__str__()
        >>> frhg = hg.add_mat(tru)
        >>> frhg.__str__()
        >>> nv = tr.transpose_mat()
        >>> nv.__str__()

        >>> mul1 = matrice([[1, 2, 3], [4, 5, 6]])
        >>> mul2 = matrice([[7, 8], [9, -1], [-2, -3]])
        >>> res = mul1.mul_mat(mul2)
        >>> res.__str__()
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
    

    
    def mul_mat(self, mat2):
        if mat2.nb_lignes() != self.nb_colonne():
            print("imposible")
        else:
            mat = []
            for i in range(len(self.__mat)):
                lig = []
                for j in range(len(self.__mat)):
                    somme = 0
                    for k in range(len(self.__mat[0])):
                        somme += self.__mat[i][k] * mat2.__mat[k][j]
                    lig.append(somme)
                mat.append(lig)
            return matrice(mat)




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)