
import pygame

import random

BLANC = ( 255, 255, 255)
NOIR = ( 0, 0, 0)
VERT = ( 0, 192, 0)
ROUGE = ( 192, 0, 0)

GRIS = (67, 67, 67)

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
    snake_init(scene)
    scene['fruit'] = init_fruit(scene)

    return scene

    
    
    
    
def boucle(scene):
    ouverture(scene['surface'])
    pygame.display.update()
    scene['horloge'].tick(20)
    pygame.time.wait(1000)
    while scene['continuer'] :
        dessine(scene)
        pygame.display.update()
        quitte(scene)
    fermeture(scene['surface'])
    pygame.display.update()
    pygame.time.wait(1000)
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
    dessine_snake(scene)
    dessine_fruit(scene)
    snake_perdu(scene)
    


    
def ouverture(surface):    
    police = pygame.font.SysFont('freesanbold.ttf', 30)
    police_snake = pygame.font.SysFont('freesanbold.ttf', 200)
    surface.blit(police_snake.render('SNAKE', 1, VERT), (135,100))
    surface.blit(police.render('utilisez les flèches directionelles pour deplacer le serpent en attrapant ', 1, BLANC), (60,300))
    surface.blit(police.render('les pommes', 1, BLANC), (340,330))
    surface.blit(police.render('version : 1.0.1.45', 1, BLANC), (320,750))
    

def fermeture(surface):
    police = pygame.font.SysFont('freesanbold.ttf', 250)
    surface.blit(police.render('GAME', 1, ROUGE), (200,250))
    surface.blit(police.render('OVER', 1, ROUGE), (200,450))



    
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
    scene['snake'] = {'vit' : 1, 'niv': scene['niveau'], 'depl_x' : 0, 'depl_y' : 0, 'corps' :[[400, 400], [400, 408], [400, 416], [400, 424]], 'larg' : 7, 'direction' : 'bas'}
    return scene


def sens_snake(scene):
    clé = pygame.key.get_pressed()
    if clé[pygame.K_LEFT]:
        scene['snake']['direction'] = 'gauche'
    elif clé[pygame.K_RIGHT]:
        scene['snake']['direction'] = 'droite'
    elif clé[pygame.K_UP]:
        scene['snake']['direction'] = 'haut'
    elif clé[pygame.K_DOWN]:
        scene['snake']['direction'] = 'bas'
    
    return scene




def dessine_snake(scene):
    sens_snake(scene)
    snake_mange(scene)
    if scene['snake']['direction'] == 'bas':
        for i in range(len(scene['snake']['corps'])):
            pygame.draw.rect(scene['surface'], VERT, (scene['snake']['corps'][i][0],scene['snake']['corps'][i][1],scene['snake']['larg'] ,scene['snake']['larg']))
            scene['snake']['corps'][i][1] += scene['snake']['vit']
    
    elif scene['snake']['direction'] == 'haut':
        for i in range(len(scene['snake']['corps'])):
            pygame.draw.rect(scene['surface'], VERT, (scene['snake']['corps'][i][0],scene['snake']['corps'][i][1],scene['snake']['larg'] ,scene['snake']['larg']))
            scene['snake']['corps'][i][1] -= scene['snake']['vit']
    
    elif scene['snake']['direction'] == 'droite':
        for i in range(len(scene['snake']['corps'])):
            pygame.draw.rect(scene['surface'], VERT, (scene['snake']['corps'][i][0],scene['snake']['corps'][i][1],scene['snake']['larg'] ,scene['snake']['larg']))
            scene['snake']['corps'][i][0] += scene['snake']['vit']
        
    elif scene['snake']['direction'] == 'gauche':
        for i in range(len(scene['snake']['corps'])):
            pygame.draw.rect(scene['surface'], VERT, (scene['snake']['corps'][i][0],scene['snake']['corps'][i][1],scene['snake']['larg'] ,scene['snake']['larg']))
            scene['snake']['corps'][i][0] -= scene['snake']['vit']
            
            
            
def snake_mange(scene):
    if scene['fruit']['pos']in scene['snake']['corps']:
        scene['fruit'] = init_fruit(scene)
        scene['snake']['corps'].append(([scene['snake']['corps'][-1][0] , scene['snake']['corps'][-1][1]+ scene['snake']['larg']]))
        scene['niveau']['score'] += 1
            
            
def init_fruit(scene):
    fruit = {'niv': scene['niveau'], 'pos': [random.randrange(150, 650, scene['snake']['larg']), random.randrange(200, 700, scene['snake']['larg'])], 'larg' : scene['snake']['larg']}
    return fruit


def dessine_fruit(scene):
    pygame.draw.rect(scene['surface'], ROUGE, (scene['fruit']['pos'][0], scene['fruit']['pos'][1],scene['snake']['larg'],scene['fruit']['larg']), scene['fruit']['larg'])
    
    
def snake_perdu(scene):
    for i in range(len(scene['snake']['corps'])):
        if scene['snake']['corps'][i][0] < scene['niveau']['rect_jeu'][0] or scene['snake']['corps'][i][1] < scene['niveau']['rect_jeu'][1] or scene['snake']['corps'][i][0] > scene['niveau']['rect_jeu'][0] + scene['niveau']['rect_jeu'][2] or scene['snake']['corps'][i][1] > scene['niveau']['rect_jeu'][0] + scene['niveau']['rect_jeu'][3]:
            scene['continuer'] = False
    return scene