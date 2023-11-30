import pygame
from pygame.locals import *
import dessin


def main():
    pygame.init()
    surface = pygame.display.set_mode((800, 600))
    pygame.display. set_caption ('maison')
    continuer = True
    while continuer :
        for event in pygame.event.get():
            dessin.dessine(surface)
            if event.type == QUIT:
                continuer = False
            pygame.display.update()
    pygame.quit()



if __name__ == "__main__":
    main()
