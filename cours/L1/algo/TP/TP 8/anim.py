import pygame
from pygame.locals import *
import scenario
import nuage
import random

def init():
    pygame.init()
    surface = pygame.display.set_mode((1000, 800))
    pygame.display. set_caption ('montagne')
    horloge = pygame.time.Clock ()
    scen  = scenario.init()
    continuer = True
    scene = {'surface' : surface, 'horloge' : horloge, 'dim_fen' : (1000, 800), 'continuer': continuer, 'scen' : scen}
    scene['nuage'] = nuage.init(random.randint(2, 6))
    return scene


    
    
def boucle(scene):
    while scene['continuer'] :
        for event in pygame.event.get():
            scenario.dessine(scene['surface'], scene)
            if event.type == QUIT:
                scene['continuer'] = False
            pygame.display.update()
    pygame.quit()









