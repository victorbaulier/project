# Créé par victor, le 20/05/2016 en Python 3.2

import pygame
from pygame.locals import *


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

    def print(self, window):

          #images are loaded
        wall=pygame.image.load(image_mur).convert()
        start= pygame.image.load(image_depart).convert()
        finish= pygame.image.load(image_arrivee).convert()
        trolley=pygame.image.load(image_caisse).convert()
        teleport=pygame.image.load(image_teleport).convert()    #avec teleport

        line_number=0
        for line in self.structure:
            case_number=0
            for letter in line:
                x=case_number*sprite_size
                y=line_number*sprite_size
                if letter=='m':
                    fenetre.blit(wall,(x,y))
                elif letter=='d':
                    fenetre.blit(start,(x,y))
                elif letter=='a':
                    fenetre.blit(finish,(x,y))

                elif letter == 'E' or letter == 'S':        #avec teleport
                    fenetre.blit(teleport, (x,y))           #avec teleport
                case_number+=1
            line_number+=1

