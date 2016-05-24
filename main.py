# Créé par victor, le 20/05/2016 en Python 3.2
import pygame
from pygame.locals import *

from classs import *
from constant import *

continu_game=1

pygame.init()

window=pygame.display.set_mode((window_width, window_width))

background=pygame.image.load(picture_background).convert()
window.blit(background,(0,0))

level= Level('l1')
level.create()
level.print(window)


worm=Player(level)
trolley=Trolley(level,level.structure)

trolley.put_initial_position()   #we collect the initial coordonates of the trolley
window.blit(worm.player,(0,0))      #the worm is printed at the coordonates (0,0)

while(continu_game):            #this is the playing loop

    for event in pygame.event.get():
        if event.type== KEYDOWN:
            if event.key==K_RIGHT:
                worm.movements('right')
                trolley.movement(worm.place_x,worm.place_y,'right')
            elif event.key==K_LEFT:
                worm.movements('left')
                trolley.movement(worm.place_x,worm.place_y,'left')
            elif event.key==K_UP:
                worm.movements('up')



    window.blit(background,(0,0))   #the background is printed again
    level.print(window)             #the environment is printed again
    window.blit(worm.player,(worm.x,worm.y))    #the worm is printed at his new position
    window.blit(trolley.trolley,(trolley.x,trolley.y)) # the trolley is printed at its initial position
    pygame.display.flip()           #the page is refreshed