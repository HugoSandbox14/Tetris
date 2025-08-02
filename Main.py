import pygame
from Parametres import *
from Class import *
import Parametres

pygame.init()
pygame.display.set_caption("Tetris")

speed = False
running = True
start = True
start2 = True
count = 0

while running:
    if start:
        tas = Tas()
        suivant = next_block()
        start = False
        score = Score()
    if start2 :
        block = suivant.new_block()
        suivant = next_block()
        start2 = False
    base(score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                block.rotation(tas)
                # block.get_position()
            if event.key == pygame.K_RIGHT:
                block.droite(tas)
            if event.key == pygame.K_LEFT:
                block.gauche(tas)
            if event.key == pygame.K_DOWN:
                speed = not speed

    tas.dessin_tas()
    block.dessin_block()
    suivant.dessin()
    count = block.chute(count,tas,speed)
    if count == -1:
        tas.add(block.forme,block.x,block.y)
        liste = tas.destruct()
        score.add(liste)
        block = suivant.new_block()
        suivant = next_block()
        count = 0
    if tas.lose() == True:
        running = False 

    pygame.display.flip()
    pygame.time.Clock().tick(60)   


pygame.quit()




