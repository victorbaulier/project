# Créé par victor, le 20/05/2016 en Python 3.2

import pygame
from pygame.locals import *
from constant import *


class Level:
    def __init__(self,file):
        self.file=file
        self.structure=0

    def create(self):
        with open(self.file, "r") as file:
            level_structure = []
            for(line)in file:
                level_line=[]
                for sprite in line:
                    #on ignore les "\n" de fin de ligne
                    if sprite!='\n':
                        #letters are add to the line's array
                        level_line.append(sprite)
                #we add the line to the array af the level
                level_structure.append(level_line)
            # we save this structure
            self.structure=level_structure
            print(self.structure)

    def print(self, window):

        #images are loaded
        wall=pygame.image.load(picture_wall).convert()

        line_number=0
        for line in self.structure:
            case_number=0
            for letter in line:
                x=case_number*sprite_size
                y=line_number*sprite_size
                if letter=='m':
                    window.blit(wall,(x,y))
                case_number+=1
            line_number+=1
    
    class Player:    #we creatte a class with all informations and fonctions of the worm

    def __init__(self):

        self.player=pygame.image.load('pictures/worms.png').convert_alpha() #picture of the worm


