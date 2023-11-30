import pygame
from pygame.locals import *
import scenario

def main():
    pygame.init()
    surface = pygame.display.set_mode((1000, 800))
    pygame.display. set_caption ('montgene')
    scen  = scenario.init()
    continuer = True
    while continuer :
        for event in pygame.event.get():
            scenario.update()
            scenario.dessine(surface, scen)
            if event.type == QUIT:
                continuer = False
            pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()
