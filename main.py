# Créé par victor, le 20/05/2016 en Python 3.2
import pygame
from pygame.locals import *

from classs import *
from constant import *


pygame.init()

window=pygame.display.set_mode((window_width, window_width))

background=pygame.image.load(picture_background).convert()
level= Level('l1')
level.create()
level.print(window)
