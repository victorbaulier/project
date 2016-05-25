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
teleport=Teleport(level.structure)
bad=Ennemy(level.structure,level)

teleport.find_position()        #we collect the coordonates of the out-door of the teleport
trolley.put_initial_position()  #we collect the initial coordonates of the trolley
window.blit(worm.player,(0,0))      #the worm is printed at the coordonates (0,0)
bad.find_position_init()

count=0                         # we create a counter to be able to create ennemy's movements.

while(continu_game):
    pygame.time.Clock().tick(30)    #this is the playing loop

    count+=1

    bad.movement(trolley.place_x, trolley.place_y, bad.find_direction(count)) #the ennemy moves end his movement depends on the direction defined by the function "find_direction"

    for event in pygame.event.get():
        if event.type== KEYDOWN:
            if event.key==K_RIGHT:
                worm.movements(trolley.place_x,trolley.place_y,'right')
                trolley.movement(worm.place_x,worm.place_y,'right')
                worm.teleport(teleport.position_out_x,teleport.position_out_y,'right')
            elif event.key==K_LEFT:
                worm.movements(trolley.place_x,trolley.place_y,'left')
                trolley.movement(worm.place_x,worm.place_y,'left')
            elif event.key==K_UP:
                worm.movements(trolley.place_x,trolley.place_y,'up')




    window.blit(background,(0,0))   #the background is printed again
    level.print(window)             #the environment is printed again
    window.blit(worm.player,(worm.x,worm.y))    #the worm is printed at his new position
    window.blit(trolley.trolley,(trolley.x,trolley.y))
    window.blit(bad.picture,(bad.x,bad.y)) # the trolley is printed at its initial position
    pygame.display.flip()           #the page is refreshed
