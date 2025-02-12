import time

#|--------------------------------------|
#|              Exercice 1              |
#|--------------------------------------|

# question 1

def pgcd(a: int, b:int)-> int:
    while b:
        a, b = b, a % b
    return a


# question 2

def pgcd_rec(a:int, b:int) ->int:
    if b == 0:
        return a
    else:
        pgcd_rec(b, a % b)


# question 3

def compare_performance():
    pairs = [(2100, 1050), (2100, 700), (2100, 350), (2100, 1400)]
    
    for a, b in pairs:
        start_time = time.time()
        pgcd(a, b)
        iterative_time = time.time() - start_time
        
        start_time = time.time()
        pgcd_rec(a, b)
        recursive_time = time.time() - start_time
        
        print(f"PGCD({a}, {b}): Iterative = {iterative_time:.10f} secondes, Recursive = {recursive_time:.10f} secondes")
    print()

#|--------------------------------------|
#|              Exercice 2              |
#|--------------------------------------|

# question 1

def fibo_rec(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
    

# question 2


def fibo_terminal(n: int, a: int = 0, b: int = 1):
    if n == 0:
        return a
    elif n == 1:
        return b
    return fibo_terminal(n - 1, b, a + b)

# question 3

def compare():
    lis = [5, 10, 12]

    for elt in lis:
        start_time = time.time()
        fibo_rec(elt)
        end_time = time.time()
        rec_time = end_time - start_time

        start_time = time.time()
        fibo_rec(elt)
        end_time = time.time()
        ter_time = end_time - start_time

        print(f"Suite de Fibonnaci de({elt}): récursive arborescente = {rec_time:.10f} secondes, récursive terminale = {ter_time:.10f} secondes")
    print()
#|--------------------------------------|
#|              Exercice 3              |
#|--------------------------------------|

# question 1
def permutations(n, vals=None):
    if n == 1:
        return [1]
    else:
        result = []
        perms = permutations(n-1)
        for elt in perms:
            pass





#|--------------------------------|
#|              TEST              |
#|--------------------------------|

def main():
    compare_performance()
    compare()
    print(permutations(2))



main()