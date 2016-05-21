# Créé par victor, le 20/05/2016 en Python 3.2
import pygame
from pygame.locals import *

from classs import *
from constant import *

continu=1
pygame.init()

while(continu):
    window=pygame.display.set_mode((window_width, window_width))

    background=pygame.image.load(picture_background).convert()
    window.blit(background,(0,0))
    
    # printing the environment of the level
    level= Level('l1')
    level.create()
    level.print(window)
    
    #printing the player in the first place in which it will be

    worm=Player()
    window.blit(worm.player,(0,0)) #the worm is initialized at the coordonates (0,0)
    
    #the window is refreshed
    
    pygame.display.flip()
