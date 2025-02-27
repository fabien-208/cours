def sauter(i: int, j: int, l = [1]):
    l.append(l[i]+l[j])



def strategie_naive(k:int):
    l=[1]
    for i in range(k-1):
        sauter(0,i,l)
    return len(l)-1


def strategie_bin(k:int):
    l=[1]
    for i in range(1, k):
        if i**2 <= k:
            for j in range(i, k-1):
                sauter(0, j, l)
        else:
            if i**2 < len(l):
                sauter(0, i**2, l)
            else:
                sauter(0, len(l)-1, l)
    return len(l)-1


def strategie_bin_2(k: int):
    l = [1]
    i = 1

    while 2**i <= k:
        sauter(0, 2**i - 1, l)
        print(2**i)
        i += 1

    for j in range(i, k-1):
        sauter(0, j, l)
    return len(l) - 1

def main():
    print(strategie_naive(5))
    print(strategie_naive(15))
    print(strategie_naive(199))
    print(strategie_bin(5))
    print(strategie_bin(15))
    print(strategie_bin(199))



main()