import couleur
import pygame
import random


def dessine(surface):
    dessine_ciel(surface)
    dessine_nuage(surface)
    dessine_soleil(surface)
    dessine_sol(surface)
    dessine_route(surface)
    dessine_maison(surface)


def dessine_ciel(surface):
  surface.fill(couleur.bleu)



def dessine_soleil(surface):
   pygame.draw.circle(surface, couleur.jaune, (580, 130), 50)
   pygame.draw.circle(surface, couleur.orange, (580, 130), 40)
   
   
def dessine_sol(surface):
   pygame.draw.rect(surface, couleur.vert, [0, 380, 800, 220], 0)
   
   
   
def dessine_route(surface):
    pygame.draw.rect(surface, couleur.gris, [0, 490, 800, 70], 0)


def dessine_maison(surface):
   dec = 0
   for i in range(6):
      pygame.draw.rect(surface, couleur.gris_cl, [25+dec, 300, 120, 150], 0)
      pygame.draw.circle(surface, couleur.jaune, (57+dec, 390), 18)
      pygame.draw.rect(surface, couleur.noir, [35+dec, 315, 44, 44], 0)
      pygame.draw.rect(surface, couleur.noir, [89+dec, 315, 44, 44], 0)
      pygame.draw.rect(surface, couleur.rouge, [38+dec, 385, 38, 65], 0)
      pygame.draw.circle(surface, couleur.noir, (40+dec, 421), 3)
      pygame.draw.rect(surface, couleur.jaune, [89+dec, 385, 44, 44], 0)
      pygame.draw.polygon(surface,couleur.noir, ((25+dec,300),(85+dec,225),(145+dec,300)), 0)
      pygame.draw.polygon(surface,couleur.gris, ((38+dec,450),(78+dec,450),(88+dec,490), (48+dec, 490)), 0)

      dec += 150


        
        
def dessine_nuage(surface):
    coord = [[320, 180],[450, 50],[21, 97],[600,200],[450, 420]]
    for elt in coord:    
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]),30)
        pygame.draw.circle(surface,couleur.blanc,(elt[0]-20,elt[1]),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0]+20,elt[1]),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]-15),20)
        pygame.draw.circle(surface,couleur.blanc,(elt[0],elt[1]+15),20)



        
        
