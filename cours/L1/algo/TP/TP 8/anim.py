import pygame
from pygame.locals import *
import scenario
import nuage
import random

def init():
    pygame.init()
    surface = pygame.display.set_mode((800, 800))
    pygame.display. set_caption ('montagne')
    horloge = pygame.time.Clock ()
    scen  = scenario.init()
    continuer = True
    scene = {'surface' : surface, 'horloge' : horloge, 'dim_fen' : (1000, 800), 'continuer': continuer, 'scen' : scen}
    scene['nuage'] = nuage.init(random.randint(2, 6))
    return scene


    
    
def boucle(scene):
    while scene['continuer'] :
            scenario.dessine(scene['surface'], scene)
            pygame.display.update()
            quitte(scene)
    pygame.quit()



def quitte(scene):
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            scene['continuer'] = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE : 
                scene['continuer'] = False






