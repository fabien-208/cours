
import pygame
import couleur
import nuage


def init():
    return {}


def met_a_jour(scene):
    scene['horloge'].tick(60)
    nuage.met_a_jour(scene['nuage'])

def dessine(surface, scenario):
    dessine_ciel(surface)
    dessine_soleil(surface)
    dessine_montagne(surface)
    dessine_sol(surface)
    dessine_arbre(surface)
    nuage.dessine_nuage(surface, scenario['nuage'])
    met_a_jour(scenario)
    
    
    
    
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
    
    
def dessine_arbre(surface):
    arbre = [(87, 600), (739, 692), (234, 615), (567, 534), (344 , 569)] 
    for e in range(5):
        X = arbre[e][0]
        Y = arbre[e][1]
        for i in range(4):
            pygame.draw.polygon(surface, couleur.vert_clair, ((X+0, Y+50), (X+20, Y+0), (X+40, Y+50)))
            Y += 23
            
        
    