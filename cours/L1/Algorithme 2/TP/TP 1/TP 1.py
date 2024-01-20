import math

# Exercice 1

def distance(point1: tuple, point2: tuple)-> float:
    return math.sqrt((point1[0]- point2[0])**2 + (point1[1]- point2[1])**2)



def perimetre(figure:list[tuple[int]]) -> float:
    peri = 0
    for i in range(len(figure)-1):
        peri += distance(figure[i], figure[i+1])
    peri += distance(figure[-1], figure[0])
    return peri


def max_distance(figure:list[tuple[int]]) -> float:
    max_dist = 0
    for i in range(len(figure)):
        for j in range(len(figure)):
            if distance(figure[i], figure[j]) > max_dist:
                max_dist = distance(figure[i], figure[j])
    return max_dist
        
    
    
# Exercice 2