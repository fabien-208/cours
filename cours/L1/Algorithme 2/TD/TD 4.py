
class matrice:

    def __init__(self, mat:list[list[int]]) -> None:
        """
        >>> bfrh = [[2, 4, 7],[6, 7, 2],[5, 6, 9]]
        >>> tr = matrice(bfrh)
        >>> tr.__str__()

        """
        self.__mat = mat

    def __str__(self) -> None:
        for lis in self.__mat:
            mat = '| '
            for i in range(len(lis)):
                mat += '{} '.format(lis[i])
            mat += '|'
            print(mat) 


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)