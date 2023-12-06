
import pygame
import couleur
import random


def init(nombre):
    att = {'vit' : 3, 'lim' : [800, 800], 'objs' : []}
    for i in range(nombre):
        frf = [random.randint(0, 1000), random.randint(0, 650)]
        att['objs'].append(frf)    
    return att





def dessine_nuage(surface, scene):
    coord = scene['objs']
    for elt in coord:    
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]),30)
        pygame.draw.circle(surface,couleur.blanc,(elt[0]-20,elt[1]),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0]+20,elt[1]),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]-15),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]+15),20)
        
        
        
        
def met_a_jour(att):
    for i in range(len(att['objs'])):
        if att['objs'][i][0] > att['lim'][0] or att['objs'][i][1] > att['lim'][1]:
            att['objs'][i][0] = -20
            att['objs'][i][1] = random.randint(0, 450)
        att['objs'][i][0] += att['vit']
        
            
            
                   