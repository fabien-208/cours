
import pygame


BLANC = ( 255, 255, 255)
NOIR = ( 0, 0, 0)
VERT = ( 0, 192, 0)
ROUGE = ( 192, 0, 0)

GRIS = (96, 96, 96)

L_CARRE = 10
VITESSE = 10




def init():
    pygame.init()
    surface = pygame.display.set_mode((800, 800))
    pygame.display. set_caption ('Snake')
    horloge = pygame.time.Clock ()
    continuer = True
    scene = {'surface' : surface, 'horloge' : horloge, 'dim_fen' : (800, 800), 'continuer': continuer}
    scene['niveau'] = niveau_init(scene)
    return scene

    
    
    
    
def boucle(scene):
    ouverture(scene['surface'])
    pygame.display.update()
    scene['horloge'].tick(60)
    pygame.time.wait(1000)
    while scene['continuer'] :
        dessine(scene)
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
 
 
 
def dessine(scene):
    scene['surface'].fill(NOIR)
    dessine_niveau(scene)

    


    
def ouverture(surface):    
    police = pygame.font.SysFont('freesanbold.ttf', 30)
    police_snake = pygame.font.SysFont('freesanbold.ttf', 200)
    surface.blit(police_snake.render('SNAKE', 1, VERT), (135,100))
    surface.blit(police.render('utilisez les flèches directionelles pour deplacer le serpent en attrapant ', 1, BLANC), (60,300))
    surface.blit(police.render('les pommes', 1, BLANC), (340,330))
    surface.blit(police.render('version : 1.0.1.45', 1, BLANC), (320,750))
    
    
    
def niveau_init(scene):
    niveau = {'score' : 0, 'surface' : scene['surface'], 'max_score' : 0, 'rect_score' : [80, 80, 610, 100], 'rect_jeu': [150, 200 ,500, 500]}
    return niveau
    
    
def dessine_niveau(scene):
    scene['surface'].fill(GRIS)
    pygame.draw.rect(scene['surface'],NOIR, [scene['niveau']['rect_jeu'][0], scene['niveau']['rect_jeu'][1], scene['niveau']['rect_jeu'][2], scene['niveau']['rect_jeu'][3]], 0)
    pygame.draw.rect(scene['surface'],BLANC, [scene['niveau']['rect_jeu'][0], scene['niveau']['rect_jeu'][1], scene['niveau']['rect_jeu'][2], scene['niveau']['rect_jeu'][3]], 5)
    pygame.draw.rect(scene['surface'],BLANC, [scene['niveau']['rect_score'][0], scene['niveau']['rect_score'][1], scene['niveau']['rect_score'][2], scene['niveau']['rect_score'][3]], 5)
    police = pygame.font.SysFont('freesanbold.ttf', 70)
    scene['surface'].blit(police.render('score: {}       best score: {}'.format(scene['niveau']['score'],scene['niveau']['max_score']), 1, BLANC), (100,100))



def snake_init(scene):
    scene['snake'] = {'vit' : 10, 'niv': scene['niveau'], 'depl_x' : 0, 'depl_y' : 0, }


    