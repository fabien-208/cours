
import pygame
import couleur


def init():
    return {}


def update():
    pass


def dessine(surface, scenario):
    dessine_ciel(surface)
    dessine_soleil(surface)
    dessine_montagne(surface)
    dessine_sol(surface)
    dessine_nuage(surface)
    dessine_arbre(surface, 100, 600)
    
    
    
    
def dessine_ciel(surface):
  surface.fill(couleur.bleu)



def dessine_soleil(surface):
   pygame.draw.circle(surface, couleur.jaune, (700, 180), 60)
   pygame.draw.circle(surface, couleur.orange, (700, 180), 45)
   
   
   
def dessine_montagne(surface):
    pygame.draw.polygon(surface,couleur.vert, ((-200, 800),(330,240),(900,800)), 0)
    pygame.draw.polygon(surface,couleur.vert, ((200, 700),(760,290),(1300, 700)), 0)
    pygame.draw.polygon(surface, couleur.blanc, ((200, 380), (330, 240), (498, 405)), 0)
    pygame.draw.polygon(surface, couleur.blanc, ((623, 390), (760, 290), (840, 350)), 0)



def dessine_sol(surface):
    pygame.draw.rect(surface, couleur.blanc, [0, 650, 1000, 200], 0)
    
    
def dessine_arbre(surface, X,Y):
    for i in range(4):
        pygame.draw.polygon(surface, couleur.vert_clair, ((X+0, Y+50), (X+20, Y+0), (X+40, Y+50)))
        Y += 23o
        
        
def dessine_nuage(surface):
    coord = [[290, 140],[900, 220],[31, 357],[600,200],[460, 320]]
    for elt in coord:    
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]),30)
        pygame.draw.circle(surface,couleur.blanc,(elt[0]-20,elt[1]),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0]+20,elt[1]),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]-15),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]+15),20)
        
        
        
def met_a_jour():
    pass